import json
import re
import tweepy
import nltk
import time 
from Clean_Text import clean_tweet
from nltk.corpus import stopwords

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

        clean_data = clean_tweet(text = tw_tweet)
        print(clean_data, "\n")

  def on_error(self, status):
    print(status)
