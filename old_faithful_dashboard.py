import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objects as go

# acquire and prep data
df = pd.read_csv('course_resources/data/old_faithful.csv')
df = df.rename(columns={'D':'date',
                        'Y':'interval',
                        'X':'duration'})
df = df[['date', 'duration', 'interval']]

# define the scatter plot graph object
data_1 = go.Scatter(x=df.duration,
                    y=df.interval,
                    mode='markers')

layout_1 = go.Layout(title='Old Faithful Eruptions\nIntervals vs. Durations',
                     xaxis={'title': 'Duration of Eruption (minutes)'},
                     yaxis={'title': 'Interval to next eruption (minutes)'})

plot_1 = dcc.Graph(id='old_faithful_scatter',
                   figure={'data': [data_1],
                           'layout': layout_1})

# plot_1 = dcc.Graph(
#                    id='scatterplot', 
#                    figure = {
#                             'data':[
#                                     go.Scatter(
#                                                x=df.duration,
#                                                y=df.interval,
#                                                mode='markers',
#                                                marker={
#                                                        'size':12,
#                                                        'color':'rgb(51,204,153)',
#                                                        'symbol':'pentagon',
#                                                        'line':{'width':2}
#                                                       }
#                                               )
#                                     ],
#                             'layout': go.Layout(
#                                                 title='Example Scatterplot',
#                                                 xaxis={'title':'The X-Axis'},
#                                                 yaxis={'title':'The Y-Axis'}
#                                                )
#                             }
#                   )

# create the app and define the layout
app = dash.Dash()
app.layout = html.Div([plot_1])

# run server
if __name__ == '__main__':
    app.run_server()