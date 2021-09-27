import csv
import datetime
import tweepy
import random
import string
from textblob import TextBlob
import TW_Listen
from Clean_Text import clean_tweet


class Social_Media_Text_Pipeline():
  #Authorization 
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

      
 
  def Extract(self, type):
    if (type == "stream"):
        if(self.social_platform == 'Twitter'):
            twitter_stream = tweepy.Stream(auth = self.auth, listener = TW_Listen.Listener(), tweet_mode = "extended")
            twitter_stream.filter(track = self.topics, languages=["en"])
    else: 
        count = 83
        result_type = input("Result type (mixed, popular, recent):")
        data = list()
        if (self.social_platform == 'Twitter'):
            for topic in self.topics:
                tweet_info = tweepy.Cursor(self.api.search,q=topic+ " -filter:retweets",lang="en",result_type = result_type,since=str(datetime.datetime.now()).split(' ')[0], tweet_mode = "extended").items(count)

                for tweet in tweet_info:                  
                    text = clean_tweet(tweet.full_text)
                    data.append([tweet.user.id_str,str(tweet.id),str(tweet.created_at).split()[0],text,tweet.favorite_count,tweet.retweet_count])
            
            letters = string.digits
            file_name = "Twitter_" +result_type+"_"+''.join(random.choice(letters) for i in range(6))+".csv"
            self.Load(file = file_name , data = data)

            
            
  #ONLY USED WHEN TYPE == BATCH 
  #TODO: ADD COLUMNS FOR NLP [ATTRIBUTES: SENTIMENT, SCORE]
  def Load(self,file, data):
      if (self.social_platform == 'Twitter'):
          with open(file, 'w',newline='') as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(["User ID","Tweet ID", "Date" ,"Text","Likes","Retweets"])
            for row in data:
                writer.writerow(row)
          print("\nDone writing to %s..." % file)
           



if __name__ == '__main__':

  Twitter_pipeline = Social_Media_Text_Pipeline(social_platform='Twitter', topics = ["Bitcoin"])
  #Twitter_pipeline.Extract(type = "stream")
  Twitter_pipeline.Extract(type = "batch")

 