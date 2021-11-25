import string
import re

class WordCount():
    def __init__(self, tweets):
        for i in range(len(tweets)):
            tweets[i][0] = tweets[i][0].lower()
            tweets[i][0] = tweets[i][0].encode('ascii', 'ignore').decode('ascii')
            tweets[i][0] = re.sub('[^A-Za-z0-9]+', ' ', tweets[i][0])
    
        self.tweets = tweets
        

    def crypto_count(self)-> list():
        
        coins = [['ethereum', 'eth'],
            ['solana', 'sol'],
            ['binance', 'bnb'],
            ['cardano', 'ada'],
            ['avalanche', 'avax'],
            ['doge', 'dogecoin']]


        all_count = []

        for i in range(len(self.tweets)):
            eth_count = 0
            sol_count = 0
            bnb_count = 0
            ada_count = 0
            avax_count = 0
            doge_count = 0
            str = self.tweets[i][0].split()
            for j in range(len(str)):
                for k in range(len(coins)):
                    if (str[j] in coins[k]):
                        if(k == 0):
                            eth_count += 1
                        if(k == 1):
                            sol_count += 1
                        if(k == 2):
                            bnb_count += 1
                        if(k== 3):
                            ada_count += 1
                        if(k == 4):
                            avax_count += 1
                        if(k == 5):
                            doge_count += 1

            all_count.append([eth_count, sol_count, bnb_count, ada_count, avax_count, doge_count])
        return all_count


        





