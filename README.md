# Social Bitcoin Dashboard

## Overview

A Social Bitcoin Dashboard that gauges public opinion, displays current prices, retrieves top headlines, and gives options to buy or sell Bitcoin. The Twitter data retrieved from the ETL pipeline is extracted via Tweepy API, transformed through cleaning processes, analyzed using Microsoft Azure Text Analytics services, and loaded into a MS Server database. The pipeline is also automated to retrieve batches of data in 12-hour intervals, and this process is done using Widows Task Manager. The results are displayed in a web-based dashboard using the Dash framework. 

The purpose of this Dashboard is to leverage public opinion to make better informed decisions. Cryptocurrencies are extremely volatile markets that are heavily influenced by the opinions of others. In order to have a better understanding of the general opinion around Bitcoin, it would be useful to have some insight on what the general public is talking about and what the overall attitude  of that message is. 


## File Descriptions


* **Social_Media_Pipeline.py** - ETL pipeline class; stores data in MS Server


* **TW_Listen.py** - Stream real time data from Twitter


* **Clean_Text.py** - Clean data from pipeline


* **NewsHeadlines.py** - Get top news stories about Bitcoin 


* **BiDailySentimentETL.py** - Executes every 12 hours to allow for batch processing data


* **DashboardUI.py** - Dashboard UI using Dash 

