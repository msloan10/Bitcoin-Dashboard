from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np
import nltk
import string
import re


class SentimentAnalysis_MFI():
    
    def __init__(self, text):
        self.text = text
        self.processed = self.pre_process(self.text)

    def pre_process(self, text) -> list():
        sen_tok = []

        #tokenize by sentence
        for i in range(len(text)):
            sen_tok.append(sent_tokenize(text[i][0]))

        word_tok = []
        sen_words = []

        #tokenize by word in sentence
        for i in range(len(sen_tok)):
            sen_words = []
            for j in range(len(sen_tok[i])):
                sen_words.append(word_tokenize(sen_tok[i][j]))
            word_tok.append(sen_words)
        
        # remove punctuation
        def remove_punc(word_tok) -> list():
            tweets = []
            sen = []
            translator = str.maketrans('', '', string.punctuation)
            for tweet in word_tok:
                sen = []
                for sentence in tweet:
                    no_punc = ' '.join(sentence).translate(translator)
                    no_punc = no_punc.split(' ')
                    for word in no_punc:
                        if ('' in no_punc):
                            no_punc.remove('')
                    if (no_punc == []):
                        continue
                    else:
                        sen.append(no_punc)
 
                tweets.append(sen)
                
            return tweets
                    

        no_punc = remove_punc(word_tok)

        #remove stop words/ POS tagging
        def pos_tag_no_stop_words(tweets) -> list():

            def get_wordnet_pos(tag):
                if tag.startswith('J'):
                    return wordnet.ADJ
                elif tag.startswith('V'):
                    return wordnet.VERB
                elif tag.startswith('N'):
                    return wordnet.NOUN
                elif tag.startswith('R'):
                    return wordnet.ADV
                else:
                    return wordnet.NOUN

            tagged = []
            
            for tweet in tweets:
                record = []
                for sentence in tweet:
                    tw = []
                    sen = nltk.pos_tag(sentence)
                    for word in sen:
                        if (word[0] in stopwords.words('english')):
                            continue
                        else:
                            tw.append((word[0], get_wordnet_pos(word[1])))
                    record.append(tw)

                tagged.append(record)
            return tagged

        pre_lemma = pos_tag_no_stop_words(no_punc)

        #lemma
        def lemmatize(data) -> list():
            wnl = WordNetLemmatizer()
            lemmatized = []
            for tweet in data:
                tw = []
                for sentence in tweet:
                    sen = []
                    for word in sentence:
                        sen.append(wnl.lemmatize(word[0], word[1]))
                    tw.append(sen)
                lemmatized.append(tw)
            return lemmatized
        return lemmatize(pre_lemma)


    def Market_Forecast_Indicator(self) -> list():
        scores = []
        bear_words = ["sell", "selling", "low", "drop", "dump", "dumping", "dropping", "bear", "bearish",
                      "dip", "dipping", "decrease", "decreasing", "red", "loss", "down", "downside"]

        bull_words = ["buy", "buying", "bull", "bullish", "high", "ath", "moon",
                      "hold", "green", "pump", "pumping", "increase", "increasing", "burning","burn","gain", "up", "upside"]

       
        bear_count = 0
        bull_count = 0
        
        for tweet in self.processed:
            tweet_score = 0
            bull_count = 0
            bear_count = 0
            for sentence in tweet:
                for word in sentence:
                    if (word in bear_words):
                        bear_count += 1
                    elif (word in bull_words):
                        bull_count += 1
                    else:
                        continue
            
            tweet_score = bull_count - bear_count
            if(tweet_score < 0):
                scores.append(['Bearish', tweet_score])
            elif(tweet_score > 0):
                scores.append(['Bullish', tweet_score])
            else:
                scores.append(['Stable', tweet_score])

        return scores


    def analyze(self) -> list():
        analysis = []
        for tweet in self.processed:
            sent = []
            for sentence in tweet:
                polarity= SentimentIntensityAnalyzer().polarity_scores(" ".join(sentence))
                sent.append(np.array([polarity['neg'], polarity['neu'], polarity['pos']]))
            sent = np.sum(sent, axis=0)/len(tweet)
            max_value= max(sent)
            sent = sent.tolist()
            if (sent.index(max_value) == 0):
                sent.append('negative')
            elif(sent.index(max_value) == 1):
                sent.append('neutral')
            else:
                sent.append('positive')

            analysis.append(sent)

        return analysis

if __name__ == "__main__":
    data = [['bitcoin is bearish. after the ath, the burn '], ['bitcoin is in a bear market']]

    x = SentimentAnalysis(data)
    #print(x.analyze())

    print(SentimentAnalysis(data).Market_Forecast_Indicator())

