import yfinance as yf
import plotly.graph_objs as go
import dash
from dash import dcc
from dash import html
import pypyodbc as odbc
 

class DashBoardUI():
    def __init__(self):
        self.app = dash.Dash(__name__)
        self.app.title = "Bitcoin Dashboard"
        self.app.layout = html.Div([html.H1(children = "Bitcoin Dash"),
            html.Div(dcc.Graph(id = 'stockChart', figure=self.candleStickFig())),
            html.Div(dcc.Graph(id = 'sentPieChart', figure=self.pieChartFig()))
            ])

        self.app.run_server(debug = True, use_reloader = False)

    def candleStickFig(self):
        data = yf.download(tickers='BTC-USD', period='5d', interval='30m')
        candleStickFig = go.Figure()
        candleStickFig.add_trace(go.Candlestick(x=data.index,
                                    open=data['Open'],
                                    high=data['High'],
                                    low=data['Low'],
                                    close=data['Close']))


        candleStickFig.update_layout(
            title='BTC-USD',
            yaxis_title='Coin Price (USD per coin)')

        return candleStickFig



    def pieChartFig(self):

        DRIVER = 'SQL Server'
        SERVER_NAME = ''
        DATABASE_NAME = 'Social Media Research' 


        table_query = """ SELECT top(1) name, create_date
                                FROM sys.Tables
                                order by create_date desc
                                """

        try: 
            con = odbc.connect(driver = DRIVER, server = SERVER_NAME, database = DATABASE_NAME, trust_connection = 'yes')
        except Exception as e: 
            print(e)
            print("Connection Failed")
        else: 
            cursor = con.cursor()
            cursor.execute(table_query)
            table_name = [row[0] for row in cursor.fetchall()]

        table_name = table_name[0]
        sentiment_percents_query = """
                                select Overall_Sent as Sentiment, count(*) * 100.0/ sum(count(*)) over () as sent_percentage
                                from {0}
                                group by Overall_Sent
                                """

        cursor.execute(sentiment_percents_query.format(table_name))
        sent_data = [row for row in cursor.fetchall()]
        
        cursor.close()
        con.close()

        labels  = [row[0] for row in sent_data]
        percents = [row[1] for row in sent_data]

        trace = go.Pie(labels = labels, values = percents)
        pieChartFig = go.Figure(data = [trace])
        pieChartFig.update_layout(title = "Bitcoin Public Sentiment")

        return pieChartFig



if __name__ == '__main__':
    DashBoardUI()
