import datetime
import tweepy
import random
import string 
import pypyodbc as odbc
from Clean_Text import clean_tweet



class Social_Media_Text_Pipeline(): 
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
        
        self.api = tweepy.API(self.auth)

      except:
        print("Unable to get authroization")

 
  def Extract(self, result_type, count) -> list():

    if (self.social_platform == 'Twitter'):
        data = list()
        raw_tweets = list()
        clean_tweets = list()
        for topic in self.topics:
            curr_date = str(datetime.datetime.now()).split(" ")[0]
            tweet_info = tweepy.Cursor(self.api.search,q=topic+ " -filter:retweets",lang="en",result_type = result_type,since= curr_date, tweet_mode = "extended").items(count)
                

            for tweet in tweet_info: 
                clean_text = clean_tweet(tweet.full_text)
                row = [tweet.user.id_str,str(tweet.id),str(tweet.created_at).split()[0],str(tweet.created_at).split()[1],clean_text,tweet.favorite_count,tweet.retweet_count, result_type,topic]
                raw_tweets.append([tweet.full_text])
                clean_tweets.append([clean_text])
                data.append(row)

        return data,raw_tweets,clean_tweets
        
  def Load(self,data):
      DRIVER = 'SQL Server'
      SERVER_NAME = ''
      DB_NAME = 'Crypto SMR'

      try: 
          con = odbc.connect(driver = '{SQL Server}', server = SERVER_NAME, database = DB_NAME, trust_connection = 'yes')
      except Exception as e: 
          print(e)
          print('Connection Failed')
      else: 
          cursor = con.cursor()

      
      self.table_name ='Tweets_%s' % ''.join(random.choice(string.digits) for i in range(5))
      create_table_statement = "CREATE TABLE %s(UserID varchar(30) NOT NULL,TweetID varchar(30),TweetDate DATE, TweetTime TIME,Clean_Tweet VARCHAR(300),Likes INT, Retweets INT, ResultType VARCHAR(10),Topic VARCHAR(20),NegScore DECIMAL(5,4),NeuScore DECIMAL(5,4),PosScore DECIMAL(5,4), OverallSent VARCHAR(10),MFI VARCHAR(9),MFI_Score INT,ETH_Count INT,SOL_Count INT,BNB_Count INT,ADA_Count INT,AVAX_Count INT,DOGE_Count INT,PRIMARY KEY(TweetID));" %self.table_name 
      insert_statement = """insert into %s values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""" % self.table_name


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
        print("inserted rows successfully into %s!" % self.table_name)
        con.commit()
        cursor.close()
        con.close()
    
