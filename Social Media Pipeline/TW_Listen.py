import json
import tweepy
import time 
from Clean_Text import clean_tweet

class Listener(tweepy.StreamListener):

  def on_data(self, data):
    raw_data = json.loads(data)
    tw_tweet = str()
    clean_data = str() 

    if raw_data['text'].startswith("RT") == False:

        if (raw_data['truncated'] == True):
            tw_tweet = raw_data['extended_tweet']['full_text']
        
        else: 
            tw_tweet = raw_data['text']

        print(tw_tweet)
        sleep(5)

  def on_error(self, status):
    print(status)
