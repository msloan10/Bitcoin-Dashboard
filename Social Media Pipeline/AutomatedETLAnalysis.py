from Social_Media_Pipeline import Social_Media_Text_Pipeline 
from SentimentAnalysis import SentimentAnalysis

TOTAL_ROWS = 800
POP_ROWS = 50

Twitter_ETL = Social_Media_Text_Pipeline(social_platform='Twitter', topics = ["bitcoin"])
pop_tweets = Twitter_ETL.Extract(dataFlow = "batch", result_type = 'popular', count = POP_ROWS)


num_recent = TOTAL_ROWS - len(pop_tweets)
Tweet_data = []

if (num_recent > 0):

    recent_tweets= Twitter_ETL.Extract(dataFlow = "batch", result_type = 'recent', count = num_recent)
    Tweet_data = pop_tweets + recent_tweets

else:

    Tweet_data = pop_tweets


tweets = []
for i in range(len(Tweet_data)):
    tweets.append([Tweet_data[i][4]])

sentiment = SentimentAnalysis(tweets).analyze()


ALL_DATA = []

for i in range(len(Tweet_data)):
    ALL_DATA.append(Tweet_data[i] + sentiment[i])


Twitter_ETL.Load(ALL_DATA)










