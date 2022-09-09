import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd
import base64 #for working with images in python
import json

app = dash.Dash()

df = pd.read_csv('course_resources/data/wheels.csv')

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return f'data:image/png;base64,{encoded.decode()}'

# create the graph object
wheels_plot_data = go.Scatter(x=df.color,
                            y=df.wheels,
                            dy=1, # creates grid-like structure
                            mode='markers',
                            marker={'size':15})
wheels_plot_layout = go.Layout(title='Test',
                               hovermode='closest')
wheels_plot = dcc.Graph(id='wheels_plot',
                        figure={'data': [wheels_plot_data],
                                'layout': wheels_plot_layout})

# create the app layout
app.layout = html.Div(
    children=[html.Div(children=wheels_plot,
                       style={'width':'30%',
                              'float':'left'}),
              html.Div(children=html.Pre(id='selection'),
                       style={'padding':35})]
)


@app.callback(Output(component_id='selection',
                     component_property='children'),
              [Input(component_id='wheels_plot',
                     component_property='selectedData')])
def callback_image(selectedData):
    return json.dumps(selectedData, indent=2)


if __name__ == '__main__':
    app.run_server()