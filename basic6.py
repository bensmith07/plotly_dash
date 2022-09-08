import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('course_resources/data/gapminderDataFiveYear.csv')

app = dash.Dash()

year_options = [{'label':str(year), 'value':year} for year in df.year.unique()]
app.layout = html.Div([dcc.Graph(id='graph',
                                 figure=None), #figure will be updated by update_figure() & callback
                       dcc.Dropdown(id='year_picker',
                                    options=year_options,
                                    value=df.year.min())])

@app.callback(Output(component_id='graph',
                     component_property='figure'),
              [Input(component_id='year_picker',
                    component_property='value')])
def update_figure(selected_year):

    # data only for selected year fro dropdown
    filtered_df = df[df.year == selected_year]

    # create a scatter plot for each continent and append to data list
    traces = []
    for continent_name in filtered_df.continent.unique():
            df_by_continent = filtered_df[filtered_df.continent == continent_name]
            traces.append(go.Scatter(x=df_by_continent.gdpPercap,
                                     y=df_by_continent.lifeExp,
                                     mode='markers',
                                     opacity=.7,
                                     marker={'size':15},
                                     name=continent_name))
    # define the graph layout
    layout = go.Layout(title='Life Expectancy vs. GDP',
                       xaxis={'title':'GDP Per Capita', 'type':'log'},
                       yaxis={'title':'Life Expectancy'})

    return {'data':traces, 'layout':layout}

if __name__ == '__main__':
    app.run_server()