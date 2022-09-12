import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

# which api for pandas datareader to use to grap stock ticker information 
api_code = 'yahoo'

# define stock ticker dropdown options
nsdq_df = pd.read_csv('course_resources/data/NASDAQcompanylist.csv')
dropdown_options = [{'label': row['Symbol'] + ' ' + row['Name'],
                     'value': row['Symbol']}
                     for idx, row in nsdq_df.iterrows()]

# create the app
app = dash.Dash()
app.layout = html.Div([
    
    # dashboard title
    html.Div([html.H1(['Stock Ticker Dashboard'])]),
    
    # stock ticker dropdown
    html.Div(children=['Select stock symbols:',
                      dcc.Dropdown(id='ticker_dropdown',
                                   options=dropdown_options,
                                   multi=True)],
             style={'width': '40%',
                    'display': 'inline-block',
                    'verticalAlign': 'top'}),

    # date picker
    html.Div(children=['Select start and end dates:',
                       dcc.DatePickerRange(id='date_picker',
                                        #    start_date='2017-01-01',
                                        #    end_date='2017-12-31'
                                        )],
            style={'width': '25%',
                    'display': 'inline-block'}),

    # submit button
    html.Button(['Submit'],
                id='submit_button'),

    # chart
    dcc.Graph(id='stock_price_chart',
              figure={'data': [go.Scatter()],
                      'layout': go.Layout()})

])

# update chart
@app.callback(Output('stock_price_chart', 'figure'),
              [State('ticker_dropdown', 'value'),
               State('date_picker', 'start_date'),
               State('date_picker', 'end_date')],
              [Input('submit_button', 'n_clicks')])
def update_chart(dropdown_selections, start_date, end_date, n_clicks):

    traces = []
    for symbol in dropdown_selections:
        df = web.DataReader(symbol, api_code, start_date, end_date)
        traces.append({'x': df.index,
                       'y': df.Close,
                       'name': symbol})

    figure = {'data': traces,
              'layout': go.Layout(title=f'{dropdown_selections} Closing Price')}
    return figure

if __name__ == '__main__':
    app.run_server()