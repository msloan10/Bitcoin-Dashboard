from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import pypyodbc as odbc
import pandas as pd
import nltk
import string
import re


class SentimentAnalysis():
    
    def __init__(self, From, Till):

        self.From = re.sub(r'[^\w\s]','',From)
        self.Till = re.sub(r'[^\w\s]','',Till)

        DRIVER = 'SQL Server'
        SERVER_NAME = ''
        DATABASE_NAME = 'Social Media Research' 

        table_names_query = """SELECT name
                            FROM sys.tables
                            WHERE create_date >= '{0}' AND create_date < '{1}' """


        select_query  = """ Select *
                            from {0}"""


        try: 
            con = odbc.connect(driver = DRIVER, server = SERVER_NAME, database = DATABASE_NAME, trust_connection = 'yes')
        except Exception as e: 
            print(e)
            print("Connection Failed")
        else:
            cursor = con.cursor()
            cursor.execute(table_names_query.format(self.From, self.Till))
            tableNames = [row for row in cursor.fetchall()]


            if (len(tableNames) == 0): 
                print("ERROR: No tables are avaliable for this interval")
                return
            else:
                data = pd.DataFrame()
                for table in tableNames:
                    df = pd.DataFrame(pd.read_sql_query(select_query.format(table[0]),con))
                    data = data.append(df)

                cursor.close()
                con.close()

                data = self.pre_process(data)
                #data = self.analyze(data)
                self.data = data



    def pre_process(self, data):

        def remove_punc(data):
            new_data  = data 
            for sentence in new_data: 
                for word in sentence: 
                    if (word in string.punctuation):
                        sentence.remove(word)
            return new_data

        def pos_tag_no_stopwords(data):
            new_data = []
            for sentence in data:
                sen = nltk.pos_tag(sentence)
                for word in sen:
                    if (word[0] in stopwords.words('english')):
                        sen.remove(word)
                new_data.append(sen)
            return new_data

        def word_net_tags(data):

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

            new_data = []
            for sentence in data: 
                sen = []
                for word in sentence:
                    sen.append((word[0], get_wordnet_pos(word[1])))
                new_data.append(sen)
            return new_data

        def get_Lemma(data):
            wnl = WordNetLemmatizer()
            new_data = []
            for sentence in data: 
                sen = []
                for word in sentence: 
                    sen.append(wnl.lemmatize(word[0], word[1]))
                new_data.append(sen)
            return new_data



        data = data.astype({'tweetid': 'int64'})
        data = data.astype({'userid': 'int64'})
        data = data.drop_duplicates(subset = 'tweetid', keep='last')

        data['token_sent'] = data['twtext'].apply(sent_tokenize)
        data['tokenized_sent_by_word'] = data['token_sent'].apply(lambda x: [word_tokenize(word) for word in x])
        data['no_punc'] = data['tokenized_sent_by_word'].apply(remove_punc)
        data['pos_tags_no_stopwords'] = data['no_punc'].apply(pos_tag_no_stopwords)
        data['wordnet_pos'] = data['pos_tags_no_stopwords'].apply(word_net_tags)
        data['lemmatized'] = data['wordnet_pos'].apply(get_Lemma)

        return data


    def analysis(self):

        return
    def get_table(self, filename):
        return self.data.to_csv(file_name, encoding='utf-8', index=False)


if __name__ == '__main__':
    x = SentimentAnalysis(From = '2021-10-18', Till = '2021-10-20')
    x.analysis()
    #x.get_table(filename = "TESTTING")
