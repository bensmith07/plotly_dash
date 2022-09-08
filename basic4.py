import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go

app = dash.Dash()

app.layout = html.Div([
                        html.Label('Dropdown'),
                        dcc.Dropdown(options=[{'label':'New York City',
                                               'value':'NYC'},
                                              {'label':'San Francisco',
                                               'value':'SF'}],
                                     value='SF'), # default value
                        html.Label('Slider'),
                        dcc.Slider(min=-10, max=10, step=.5, value=0, 
                                   marks={i: i for i in range(-10, 11)}),
                        html.Label('Radio Items'),
                        dcc.RadioItems(options=[{'label':'New York City',
                                                 'value':'NYC'},
                                                {'label':'San Francisco',
                                                 'value':'SF'}],
                                       value='SF') # default value
                      ])



if __name__ == '__main__':
    app.run_server()