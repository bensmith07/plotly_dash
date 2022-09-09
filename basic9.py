import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Input(id='number_in',
              value=1,
              style={'fontSize':24}),
    html.Button(id='submit_button',
                n_clicks=0,
                children='Submit Here',
                style={'fontSize': 24}),
    html.H1(id='number_out')
])

@app.callback(Output(component_id='number_out',
                     component_property='children'),
              [Input(component_id='submit_button',
                     component_property='n_clicks')],
              [State(component_id='number_in', 
                     component_property='value')])
def output(n_clicks, number):
    return f'''Input Value: {number} Number of Button Clicks: {n_clicks}'''


if __name__ == '__main__':
    app.run_server()