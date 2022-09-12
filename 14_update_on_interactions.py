import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd
import numpy as np

df = pd.read_csv('course_resources/data/mpg.csv')

app = dash.Dash()

app.layout = html.Div([
    # scatter plot
    html.Div(
        [dcc.Graph(id='mpg_scatter',
                   figure={'data': [go.Scatter(x=df.model_year + 1900,
                                               y=df.mpg,
                                               text=df.name,
                                               hoverinfo='text + x + y',
                                               mode='markers')],
                           'layout': go.Layout(title='MPG Data',
                                               xaxis={'title': 'Model Year'},
                                               yaxis={'title': 'MPG'},
                                               hovermode='closest')})],
         style={'width': '50%',
                'display': 'inline-block'}
),
    # line plot
    html.Div(
        [dcc.Graph(id='mpg_line',
                   figure={'data': [go.Scatter(x=[0,1],
                                               y=[0,1],
                                               mode='lines')],
                           'layout': go.Layout(title='Acceleration',
                                               margin={'l': 0})})],
        style={'width': '20%',
               'height': '50%',
               'display': 'inline-block'}
),
    # markdown
    html.Div(
        [dcc.Markdown(id='mpg_stats')],
        style={'width': '20%',
               'height': '50%',
               'display': 'inline-block'})
    ])



@app.callback(Output('mpg_line','figure'),
              [Input('mpg_scatter','hoverData')])
def callback_graph(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    figure = {'data': [go.Scatter(x=[0, 1],
                                  y=[0, 60 / df.iloc[v_index].acceleration],
                                  mode='lines',
                                  line={'width': 4 * df.iloc[v_index].cylinders})],
              'layout': go.Layout(title=df.iloc[v_index]['name'],
                                  margin={'l':0},
                                  height=300,
                                  xaxis={'visible': False},
                                  yaxis={'visible': False,
                                         'range': [0, 60 / df.acceleration.min()]})}
    return figure

@app.callback(Output('mpg_stats', 'children'),
              [Input('mpg_scatter', 'hoverData')])
def callback_stats(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = f'''
             {df.iloc[v_index].cylinders} cylinders\n
             {df.iloc[v_index].displacement} cc displacement\n
             0 to 60mph in {df.iloc[v_index].acceleration} seconds\n
             '''
    return stats




if __name__ == '__main__':
    app.run_server()

