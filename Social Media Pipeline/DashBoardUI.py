#build UI 
import yfinance as yf
import plotly.graph_objs as go
import dash
#import dash shit 
 
class UI():
    def __init__(self):
        x = self.stockChart()
        x.show()
    def stockChart(self): 
        data = yf.download(tickers='BTC-USD', period='5d', interval='30m')

        #declare figure
        fig = go.Figure()

        #Candlestick
        fig.add_trace(go.Candlestick(x=data.index,
                                    open=data['Open'],
                                    high=data['High'],
                                    low=data['Low'],
                                    close=data['Close']))

        # Add titles
        fig.update_layout(
        title='BTC-USD ',
        yaxis_title='Stock Price (USD per coin)')
  
        #Add line to candlestick graph 
        app = dash.Dash(__name__)

        app.layout = html.Div([
            dcc.Checklist(
                id='toggle-rangeslider',
                options=[{'label': 'Include Rangeslider', 
                          'value': 'slider'}],
                value=['slider']
            ),
            dcc.Graph(id="graph"),
        ])


        app.run_server(debug=True)


        return fig

    #def pieChart():
if __name__ == '__main__':
    UI()
