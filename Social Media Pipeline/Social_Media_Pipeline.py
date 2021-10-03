import csv
import datetime
import tweepy
import random
import string
from textblob import TextBlob
import TW_Listen
import sys 
import pypyodbc as odbc
from Clean_Text import clean_tweet
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


class Social_Media_Text_Pipeline():
  #Authorization
  #TODO: MAKE KEYS ARGS  
  def __init__(self,social_platform,topics):

    self.social_platform = social_platform
    self.topics = topics
    
    if (self.social_platform == 'Twitter'):
      try:
        consumer_key = input("Enter Consumer Key: ")
        consumer_secret = input("Enter Consumer Secret:")
        access_token = input("Enter Access Token:")
        access_token_secret = input("Enter Access Token Secret:")

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)


        self.auth = auth
        
        #FOR BATCH PROCESSING 
        self.api = tweepy.API(self.auth)

      except:
        print("Unable to get authroization")

 
  def Extract(self, dataFlow, result_type, count):
    if (dataFlow == "stream"):
        if(self.social_platform == 'Twitter'):
            twitter_stream = tweepy.Stream(auth = self.auth, listener = TW_Listen.Listener(), tweet_mode = "extended")
            twitter_stream.filter(track = self.topics, languages=["en"])
    else: 
        data = list()
        if (self.social_platform == 'Twitter'):
            for topic in self.topics:
                tweet_info = tweepy.Cursor(self.api.search,q=topic+ " -filter:retweets",lang="en",result_type = result_type,since=str(datetime.datetime.now()).split(' ')[0], tweet_mode = "extended").items(count)

                for tweet in tweet_info:                  
                    text = clean_tweet(tweet.full_text)
                    data.append([tweet.user.id_str,str(tweet.id),str(tweet.created_at).split()[0],text,tweet.favorite_count,tweet.retweet_count])

            return data
        
  def Analyze(self, key, endpoint, row):
    try: 
        ta_credential = AzureKeyCredential(key)
        text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, 
        credential=ta_credential)
    except Exception as e:
        print(e)
        print("Task Failed")
    else:
        client = text_analytics_client


    sent_scores = [] 
    tweet = [row[3]]
    response = client.analyze_sentiment(documents = tweet)[0]
    sent_scores = [response.confidence_scores.positive, response.confidence_scores.negative, response.confidence_scores.neutral]

    if (sent_scores.index(max(sent_scores)) == 0):
        row.append("Positive")
    elif (sent_scores.index(max(sent_scores)) == 1):
        row.append("Negative")
    else: 
        row.append("Neutral")



  def Load(self,data):
      DRIVER = 'SQL Server'
      SERVER_NAME = ''
      DATABASE_NAME = 'Social Media Research' 
    
      try: 
          con = odbc.connect(driver = '{SQL Server}', server = SERVER_NAME, database = DATABASE_NAME, trust_connection = 'yes')
      except Exception as e: 
          print(e)
          print('Connection Failed')
      else: 
          cursor = con.cursor()

      
      table_name ='Tweets_%s' % ''.join(random.choice(string.digits) for i in range(5)) 
      create_table_statement = "CREATE TABLE %s(UserID varchar(30) NOT NULL,TweetID varchar(30),TweetDate DATE,TWText VARCHAR(280),Likes INT, Retweets INT,Overall_Sent varchar(10),PRIMARY KEY(TweetID));" %table_name 
      insert_statement = """insert into %s values (?,?,?,?,?,?,?)""" % table_name


      try: 
        cursor.execute(create_table_statement)
        con.commit()
      except Exception as e: 
        print(e)
        print("creating table failed")
        cursor.rollback()
      else: 
        for row in data: 
            cursor.execute(insert_statement, row)
        print("inserted rows successfully into %s!" % table_name)
        con.commit()
        cursor.close()
        con.close()
