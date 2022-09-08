import dash
from dash import html

app = dash.Dash()

app.layout = html.Div(children=['This is the outermost Div',
                                html.Div(children=['This is an inner Div'],
                                         style={'color':'red',
                                                'border':'3px red solid'}),
                                html.Div(children=['Another inner Div'],
                                         style={'color':'blue',
                                                'border': '3px blue solid'})],
                      style={'color':'green',
                             'border':'4px green solid'})

if __name__ == '__main__':
    app.run_server()