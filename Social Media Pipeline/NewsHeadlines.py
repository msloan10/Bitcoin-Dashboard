from GoogleNews import GoogleNews
import datetime

class NewsHeadlines():
    def __init__(self, topic):
        self.topic = topic

    def get_headlines(self):
        return self.result
    def analyze(self): 


if __name__ == '__main__':
  x = NewsHeadlines(topic = "Bitcoin")
  for i in range(len(x.get_headlines())):
      print(x.get_headlines()[i][0])
      print(x.get_headlines()[i][1])
