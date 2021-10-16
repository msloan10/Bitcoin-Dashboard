from Social_Media_Pipeline import Social_Media_Text_Pipeline 
import pypyodbc as odbc
#import SentimentAnalysis

TOTAL_ROWS = 800
POP_ROWS = 50

Twitter_pipeline = Social_Media_Text_Pipeline(social_platform='Twitter', topics = ["bitcoin"])
popular_tweets = Twitter_pipeline.Extract(dataFlow = "batch", result_type = 'popular', count = POP_ROWS)


recent_rows = TOTAL_ROWS - len(popular_tweets)
all_tweets = []

if (recent_rows > 0):

    recent_tweets = Twitter_pipeline.Extract(dataFlow = "batch", result_type = 'recent', count = recent_rows)
    Twitter_pipeline.Load(data = popular_tweets + recent_tweets)

else:

    Twitter_pipeline.Load(data = popular_tweets) 

