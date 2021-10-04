# Bitcoin Dashboard
 A Bitcoin dashboard that incorporates sentiment analysis using Twitter data. The dashboard also displays the top news headlines, a candle stick graph for bitcoin pricing, and options to buy or sell Bitcoin. This dashboard is meant to gauge public opinion in order to understand the market's behavior. The hope for this tool is to be able to make better investment decisions as well as lower the anxiety of dealing with such a volatile market that is heavily influenced by human emotion. 

## File Descriptions:  


* **Social_Media_Pipeline.py** - ETL pipeline; stores data in MS Server


* **TW_Listen.py** - Stream real time data from Twitter


* **Clean_Text.py** - Clean data from pipeline


* **NewsHeadlines.py** - Get top news stories about Bitcoin 


* **BiDailySentimentETL.py** - script that executes every 12 hours to allow for batch processing data from Social_Media_Pipeline.py


* **DashboardUI.py** - Dashboard UI using Dash 

