'''
Tia Campagna
DS2500
Spring 2021
Visualizations Using Dash
'''

'''
Goal: Make a scatter plot that has drop downs that allow you to select the average audio feature to view over the 
course of the pandemic
Inspired by: https://www.youtube.com/watch?v=Kr94sFOWUMg&t=531s
Sourced by: https://dash.plotly.com/dash-core-components/dropdown
'''

import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from gatherToptrackInfo import *


app = dash.Dash(__name__)
df = find_monthly_averages()

app.layout = html.Div([

    html.Div([
        dcc.Graph(id='my_graph')]),

    html.Div([

        html.Br(),
        html.Label(['Choose an Audio Feature'], style={'font-weight': 'bold', "text-align": "center"}),
        dcc.Dropdown(id='audio_feature',
                     options=[
                         {'label': 'Acousticness', 'value': 'Acousticness'},
                         {'label': 'Danceability', 'value': 'Danceability'},
                         {'label': 'Duration Ms', 'value': 'Duration Ms'},
                         {'label': 'Energy', 'value': 'Energy'},
                         {'label': 'Instrumentalness', 'value': 'Instrumentalness'},
                         {'label': 'Liveness', 'value': 'Liveness'},
                         {'label': 'Loudness', 'value': 'Loudness'},
                         {'label': 'Mode', 'value': 'Mode'},
                         {'label': 'Speechiness', 'value': 'Speechiness'},
                         {'label': 'Tempo', 'value': 'Tempo'},
                         {'label': 'Valence', 'value': 'Valence'}],
                     value='Acousticness',
                     clearable=True,
                     multi=False,
                     placeholder='Choose Feature...'),
])])

@app.callback(
        Output('my_graph', 'figure'),
        [Input('audio_feature', 'value')],
    )

def render_graph(audio_feature):

    # create a df containing only the selected average audio feature
    option_df = df[audio_feature]

    fig = px.line(option_df)
    fig.update_layout(yaxis={'title': 'Monthly Average of {} Audio Feature'.format(audio_feature)},
                      xaxis={'title': 'Month of the Pandemic'},
                      title={'text': 'Monthly Audio Feature Average of Top Spotify Tracks Over Pandemic',
                             'font': {'size': 20}},
                      font = dict(color = 'green'),
                      legend= ({'title': 'Audio Feature'}))

    return fig

if __name__ == '__main__':
    app.run_server(debug=False)