import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import numpy as np
import pandas as pd

app = dash.Dash()

# CREATE DATA
np.random.seed(10)

x1 = np.linspace(0.1, 5, 50)
x2 = np.linspace(5.1, 10, 50)
y = np.random.randint(0, 50, 50)

df1 = pd.DataFrame({'x': x1, 'y': y})
df2 = pd.DataFrame({'x': x1, 'y': y})
df3 = pd.DataFrame({'x': x2, 'y': y})
df = pd.concat([df1, df2, df3])

# # CREATE scatterplot_1
# data_1 = [go.Scatter(x=df.x,
#                    y=df.y,
#                    mode='markers')]
# layout_1 = go.Layout(title='Scatterplot #1', 
#                    hovermode='closest')
# scatterplot_1 = dcc.Graph(id='scatterplot_1',
#                           figure={'data': data_1,
#                                   'layout': layout_1})

# DEFINE APP LAYOUT
app.layout = html.Div(
    children=[html.Div(dcc.Graph(id='scatterplot_1',
                                 figure={'data': [go.Scatter(x=df.x,
                                                             y=df.y,
                                                             mode='markers')],
                                         'layout': go.Layout(title='Scatterplot #1',
                                                             hovermode='closest')}),
                       style={'width':'30%',
                              'display':'inline-block'}),
              html.Div([html.H1(id='density_output',
                                children='[density_output]',
                                style={'paddingTop':25})],
                       style={'width': '30%',
                              'display': 'inline-block',
                              'verticalAlign': 'top'})])

@app.callback(Output(component_id='density_output',
                     component_property='children'),
              [Input(component_id='scatterplot_1',
                     component_property='selectedData')])
def find_density(selectedData):
    # calculate density
    pts = len(selectedData['points'])
    rng_or_lp = list(selectedData.keys())
    rng_or_lp.remove('points')
    max_x = max(selectedData[rng_or_lp[0]]['x'])
    min_x = min(selectedData[rng_or_lp[0]]['x'])
    max_y = max(selectedData[rng_or_lp[0]]['y'])
    min_y = min(selectedData[rng_or_lp[0]]['y'])
    area = (max_x - min_x) * (max_y - min_y)
    d = pts / area
    return f'Density = {d:.2f}'


if __name__ == '__main__':
    app.run_server()