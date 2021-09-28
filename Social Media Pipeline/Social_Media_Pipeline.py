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
        
  def Analyze_Data(self, key, endpoint):

    def authenticate_Azure_client():
        ta_credential = AzureKeyCredential(key)
        text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, 
        credential=ta_credential)

        return text_analytics_client

    self.client = authenticate_client()


  def Load(self,data):
      columns = ["User ID","Tweet ID", "Date" ,"Text","Likes","Retweets", "Sentiment", "Positive Score", "Negative Score"]
      DRIVER = 'SQL Server'
      SERVER_NAME = 'LAPTOP-5A0QRM9K'
      DATABASE_NAME = 'Social Media Research'


      #edit this 
      conn_string ="Driver = {{{DRIVER}};\nServer={SERVER_NAME};\nTrust_Coonnection = yes;"
      print(conn_string)

      #con = odbc.connect()