from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

class Sentiment(object):
    #connect to Azure 
    def __init__(self, key, endpoint):
        self.key = key 
        self.endpoint = endpoint

        def authenticate_client():
            ta_credential = AzureKeyCredential(self.key)
            text_analytics_client = TextAnalyticsClient(
            endpoint=self.endpoint, 
            credential=ta_credential)

            return text_analytics_client

        self.client = authenticate_client()
    
    #get sentiment 
    def sentiment(text):




if  __name__ == '__main__':
    sent = Sentiment(key =)
    text = "i love hotdogs. I hate giraffes. lions are ok."
    sent.sentiment(text)