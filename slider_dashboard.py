import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash()

app.layout = html.Div(
    children=[html.Div(children=dcc.RangeSlider(id='slider1', 
                                                min=-10, max=10, step=1,
                                                value=[-5, 5]),
                       style={'width':'50%'}),
              html.Div(id='number_output',
                       children=None,
                       style={'fontSize':24})]
)


@app.callback(Output(component_id='number_output',
                     component_property='children'),
              [Input(component_id='slider1',
                     component_property='value')])
def update_output(value_list):
    return (f'''{value_list[0]} x {value_list[1]} = 
                {value_list[0] * value_list[1]}''')


if __name__ == '__main__':
    app.run_server()