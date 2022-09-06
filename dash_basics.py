import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div(children=[html.H1('Hello Dash'),
                                html.Div('Dash: Web Dashboards with Python'),
                                dcc.Graph(id='example',
                                          figure={'data':[{'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name':'SF'},
                                                          {'x':[1,2,3], 'y':[2,4,5], 'type':'bar', 'name':'NYC'}
                                                         ],
                                                  'layout':{'title': 'BAR PLOTS'}
                                                 }
                                         )
                               ]
                     )

if __name__ == '__main__':
    app.run_server()