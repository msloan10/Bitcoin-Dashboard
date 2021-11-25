from Social_Media_Pipeline import Social_Media_Text_Pipeline 
from SentimentAnalysis import SentimentAnalysis_MFI
from WordCount import WordCount
 
TOTAL_ROWS = 850

Twitter_ETL = Social_Media_Text_Pipeline(social_platform='Twitter', topics = ["bitcoin"])
Tweet_data = Twitter_ETL.Extract(result_type = 'recent', count = TOTAL_ROWS)

raw_tweets = []
clean_tweets = []

for i in range(len(Tweet_data)):
    raw_tweets.append([Tweet_data[i][4]])
    clean_tweets.append([Tweet_data[i][5]])

sentiment = SentimentAnalysis_MFI(clean_tweets).analyze()

Market_indicator = SentimentAnalysis_MFI(clean_tweets).Market_Forecast_Indicator()

coin_count = WordCount(raw_tweets).crypto_count()

ALL_DATA = []

for i in range(len(Tweet_data)):
    ALL_DATA.append(Tweet_data[i] + sentiment[i] + Market_indicator[i] + coin_count[i])
    print(ALL_DATA[i])

Twitter_ETL.Load(ALL_DATA)










