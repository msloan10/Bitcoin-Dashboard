# Bitcoin Social Media Sentiment Analysis ETL

## Overview


The impact social media is having on the world in undeniable. Millions of users login to engage in online discussions and communities everyday, and this results in an overwhelming amount of data that can be used in numerous ways. One way we can use this data is by conducting sentiment analysis over a specified topic. By doing this, we are able to detect the feelings an audience or market may have over a certain product, topic, event, etc. This can be extremely beneficial when investing in financial assets/ stocks. If we are able to detect how people feel about a certain asset, we can identify the state of the market (bear or bull) and have better decision making. 


The Bitcoin Sentiment Analysis ETL in this repository extracts, transforms, analyzes, and loads data from Twitter into a MS SQL Server database. The analysis portion includes individual scores for positive, negative, and neutral polarity as well as overall sentiment. Other attributes include tweet id, user id, text, retweets, likes, result type, time, and mentions of other top cryptocurrencies. In addition to this, I constructed my own metric known as the Market Forecast Indicator (MFI). The MFI indicates whether a tweet is implying that the current market is Bearish, Bullish, or Stable (neither bear or bull).  

Experiment results are displayed using Power BI. 
 

## File Descriptions


* **Social_Media_Pipeline.py** - ETL Pipeline to retrieve social media data


* **SentimentAnalysis.py** - NLP pre-processing and sentiment analysis pipeline; Returns MFI

* **ETLAnalysis_BTC.py** - Automatic ETL and sentiment analysis processing; executes every 15 minutes


* **Sample Batch** - Table output for ETL and Analysis 


* **Clean_Text.py** - Clean raw text from Social Media Pipeline (removes lists of hashtags, special characters, emojis)


* **WordCount.py** - Counts number of occurrences of top alt coins per tweet 
