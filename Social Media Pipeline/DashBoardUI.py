import yfinance as yf
import plotly.graph_objs as go
import dash
from dash import dcc
from dash import html
import pypyodbc as odbc

class DashBoardUI():
    def __init__(self):

        self.app = dash.Dash(__name__)
        self.app.title = "Bitcoin Social Dashboard"
        self.app.layout = html.Div([html.H1(children = "Bitcoin Dashboard"),
            html.Div(dcc.Graph(id = 'stockChart', figure=self.candleStickFig())),
            html.Div(dcc.Graph(id = 'sentTimeSeries', figure=self.sentTimeSeries()))
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



    def sentTimeSeries(self):


if __name__ == '__main__':
    DashBoardUI()
