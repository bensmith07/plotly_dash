import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('course_resources/data/mpg.csv')
features = df.columns

app = dash.Dash()

app.layout = html.Div(
    children=[html.Div(children=[dcc.Dropdown(id='x_axis_dropdown',
                                              options=[{'label':feat, 'value':feat} 
                                                            for feat in features
                                                      ],
                                              value='displacement')],
                       style={'width':'48%', 'display':'inline-block'}),
              html.Div(children=[dcc.Dropdown(id='y_axis_dropdown',
                                              options=[{'label':feat, 'value':feat} 
                                                            for feat in features
                                                      ],
                                              value='mpg')],
                       style={'width':'48%', 'display':'inline-block'}),
              dcc.Graph(id='feature_graphic',
                        figure=None)],
    style={'padding':10}
)

@app.callback(Output(component_id='feature_graphic',
                     component_property='figure'),
              [Input(component_id='x_axis_dropdown',
                     component_property='value'),
               Input(component_id='y_axis_dropdown',
                     component_property='value')])
def update_figure(x_axis_name, y_axis_name):
    data = [go.Scatter(x=df[x_axis_name],
                         y=df[y_axis_name],
                         text=df.name,
                         mode='markers',
                         marker={'size':15,
                                 'opacity':.5,
                                 'line': {'width':.5, 'color':'white'}})]
    layout_1 = go.Layout(title='MPG Dashboard',
                         xaxis={'title':x_axis_name},
                         yaxis={'title':y_axis_name})
    return {'data':data, 'layout':layout_1}

if __name__ == '__main__':
    app.run_server()

