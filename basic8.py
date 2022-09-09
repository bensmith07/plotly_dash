import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd
import base64 #for working with images in python

df = pd.read_csv('course_resources/data/wheels.csv')

app = dash.Dash()

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return f'data:image/png;base64,{encoded.decode()}'

wheels_radio_options = [{'label': i, 'value': i} for i in df.wheels.unique()]
colors_radio_options = [{'label': i, 'value': i} for i in df.color.unique()]

app.layout = html.Div(
    children=[dcc.RadioItems(id='wheels_input',
                             options=wheels_radio_options,
                             value=1), #default option value
              html.Div(id='wheels_output'), # "children" argument to be updated by callback
              html.Hr(), # "horizontal rule" line separator
              dcc.RadioItems(id='colors_input',
                             options=colors_radio_options,
                             value='blue'), # default option value
              html.Div(id='colors_output'),
              html.Img(id='display_image', 
                       src='children',
                       height=300)], 
    style={'fontFamily': 'helvetica',
           'fontSize': 18} 
)

@app.callback(Output(component_id='wheels_output',
                     component_property='children'),
              [Input(component_id='wheels_input',
                     component_property='value')])
def callback_wheels(wheels_value):
    return f'you chose {wheels_value}'

@app.callback(Output(component_id='colors_output',
                     component_property='children'),
              [Input(component_id='colors_input',
                     component_property='value')])
def callback_colors(colors_value):
    return f'you chose {colors_value}'

@app.callback(Output(component_id='display_image',
                     component_property='src'),
              [Input(component_id='wheels_input',
                     component_property='value'),
               Input(component_id='colors_input',
                     component_property='value')])
def callback_image(wheels, color):
    path = 'course_resources/data/images/'
    return encode_image(path 
                        + df[(df.wheels == wheels) & (df.color == color)]
                            .image.values[0])

if __name__ == '__main__':
    app.run_server()

html.Img()