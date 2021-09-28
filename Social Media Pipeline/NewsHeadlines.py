from GoogleNews import GoogleNews
import datetime
import pandas as pd

class NewsHeadlines():
    def __init__(self, topic):
        result = []
        date = datetime.datetime.now()
        date = date.strftime("%m/%d/%Y")
        news = GoogleNews(start =date, end = date)
        news.search(topic)
        for i in range(5):
            result.append([news.get_texts()[i], news.get_links()[i]])

        self.result = result

    def get_headlines(self):
        return self.result

if __name__ == '__main__':
  x = NewsHeadlines(topic = "Bitcoin")
  for i in range(len(x.get_headlines())):
      print(x.get_headlines()[i][0])
      print(x.get_headlines()[i][1])
