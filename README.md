# Social Media Bitcoin Sentiment Analysis Pipeline (ETL)

## Overview


The impact social media is having on the world is undeniable. Everyday, millions of users login to engage in online discussions resulting in an overwhelming amount of unstructured, text data that can potentially be used to uncover valuable insights. One method of extracting meaning from this data is to conduct sentiment analysis in order to detect how an audience feels about a certain item or topic. This type of analysis can be extremely beneficial because if a company or entity is able to detect how people feel about a given topic / item, they will have a strategic advantage in the market that may allow them to take early action and make better informed decisions. With this concept in mind, I would like to introduce my project: The Bitcoin Sentiment Analysis Pipeline (ETL).

The Bitcoin Sentiment Analysis Pipeline (ETL) in this repository automatically extracts tweets mentioning Bitcoin along with relative Twitter user data, transforms the text into a uniform format, loads the clean data into a MS SQL Server database, and analyzes the sentiment of over 800 tweets in 15 minute intervals. The analysis portion includes assigning each tweet a sentiment direction (positive, negative or neutral) and giving each tweet a Market Forecast Indicator score. This is a mathematical formula I developed to indicate what type of market the tweet is implying: Bearish, Bullish, or Stable (neither bear or bull). In addition, the pipeline monitors mentions of other top cryptocurrencies to give a better sense of which coins may also have changed perceptions. 

Aggregated experiment results are displayed using a Power BI dashboard.

 
 

## File Descriptions


* **Social_Media_Pipeline.py** - ETL Pipeline to retrieve social media data


* **SentimentAnalysis.py** - NLP pre-processing and sentiment analysis pipeline; Returns MFI

* **ETLAnalysis_BTC.py** - Automatic ETL and sentiment analysis processing; executes every 15 minutes


* **Sample Batch** - Table output for ETL and Analysis 


* **Clean_Text.py** - Clean raw text from Social Media Pipeline (removes lists of hashtags, special characters, emojis)


* **WordCount.py** - Counts number of occurrences of top alt coins per tweet 
