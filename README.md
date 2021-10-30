# Bitcoin Social Media Sentiment Analysis ETL

## Overview


The impact social media is having on the world in undeniable. Millions of users login to engage in online discussions and communities everyday. This results in an overwhelming amount of data that can be used to in numerous ways. One way we can use this data is by conducting sentiment analysis over a specified topic. By conducting sentiment analysis, we are able to detect the feelings an audience or market may have over a certain topic. This can be useful when investing in financial assets/ stocks. If we are able to detect how society feels about a certain asset, it can help indicate the type of market the stock is in (bearish or bullish) and lead to better decision making. 


The Bitcoin Sentiment Analysis ETL in this repository extracts, transforms, analyzes, and loads data from Twitter into a MS SQL Server database. The analysis portion of the data includes individual scores for positive, negative, and neutral polarity as well as overall sentiment. Other attributes include tweet id, user id, text, retweets, likes, result type, and time. 

NEXT STEP: Visualize data in Power BI  


## File Descriptions


* **Social_Media_Pipeline.py** - ETL Pipeline to retrieve social media data


* **SentimentAnalysis.py** - NLP pre-processing and sentiment analysis pipeline


* **AutomatedETLAnalysis.py** - Automatic ETL and sentiment analysis processing; executes every 15 minutes


* **Sample Batch** - Table output for ETL and Analysis 


* **Clean_Text.py** - Clean raw text from Social Media Pipeline (removes lists of hashtags, special characters, emojis)


* **TW_Listen.py** - Stream real time data from Twitter 








