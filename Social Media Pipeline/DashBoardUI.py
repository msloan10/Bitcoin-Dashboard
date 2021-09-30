#build UI 
import yfinance as yf
import plotly.graph_objs as go
import dash
from dash import dcc
from dash import html
 
app = dash.Dash(__name__)

app.layout = html.Div(children = [html.H1(children = "Bitcoin Dash")])


if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = False)
