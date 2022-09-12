import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

app = dash.Dash()



app.layout = html.Div([
    html.H1(id='live-update-text'),
    dcc.Interval(id='interval_component',
                 interval=2000,
                 n_intervals=0)
])

@app.callback(Output('live-update-text', 'children'),
              [Input('interval_component', 'n_intervals')])
def update_layout(n_intervals):
    return f'This page has updated {n_intervals} times.'




if __name__ == '__main__':
    app.run_server()