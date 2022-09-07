import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import numpy as np

# creating data
np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

# define a scatter plot Graph object
plot_1 = dcc.Graph(
                   id='scatterplot', 
                   figure = {
                            'data':[
                                    go.Scatter(
                                               x=random_x,
                                               y=random_y,
                                               mode='markers',
                                               marker={
                                                       'size':12,
                                                       'color':'rgb(51,204,153)',
                                                       'symbol':'pentagon',
                                                       'line':{'width':2}
                                                      }
                                              )
                                    ],
                            'layout': go.Layout(
                                                title='Example Scatterplot',
                                                xaxis={'title':'The X-Axis'},
                                                yaxis={'title':'The Y-Axis'}
                                               )
                            }
                  )
# define a bar plot Graph object
plot_2 = dcc.Graph(
                   id='example',
                   figure={
                           'data':[
                                   {'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name':'SF'},
                                   {'x':[1,2,3], 'y':[2,4,5], 'type':'bar', 'name':'NYC'}
                                  ],
                           'layout':{
'title': 'Example Bar Plots'}
                          }
                  )

# creating app
app = dash.Dash()
# defining app layout
app.layout = html.Div([
                       plot_1,
                       plot_2
                      ]
)

if __name__ == '__main__':
        app.run_server()