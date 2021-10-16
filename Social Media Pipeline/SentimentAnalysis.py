import pypyodbc as odbc

class SentimentAnalysis(object):
    
    def __init__(self, tableNames):
        DRIVER = 'SQL Server'
        SERVER_NAME = ''
        DATABASE_NAME = 'Social Media Research' 

        select_query = """ SELECT * from {0}
                                """
        data = []
        try: 
            con = odbc.connect(driver = DRIVER, server = SERVER_NAME, database = DATABASE_NAME, trust_connection = 'yes')
        except Exception as e: 
            print(e)
            print("Connection Failed")
        else: 
            cursor = con.cursor()
            for name in tableNames:
                cursor.execute(select_query.format(name))
                data += [row for row in cursor.fetchall()]

            self.data = data
            cursor.close()
            con.close()

    #def Analysis(self):


if __name__ == '__main__':
    DRIVER = 'SQL Server'
    SERVER_NAME = ''
    DATABASE_NAME = 'Social Media Research' 

    table_query = """ SELECT top(4) name
                                FROM sys.Tables
                                order by create_date desc
                                """
    try: 
        con = odbc.Connection(driver = DRIVER, server = SERVER_NAME, database = DATABASE_NAME, trust_connection = 'yes')
    except Exception as e: 
        print(e)
        print("Error: Can't connect")
    else: 
        cursor = con.cursor()
        cursor.execute(table_query)
        table_names = [row[0] for row in cursor.fetchall()]

    x = SentimentAnalysis(['Tweets_95321','Tweets_21098'])
    print(len(x.data))

    


