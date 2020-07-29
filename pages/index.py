# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predicting the Outcome of a League of Legends Match

            LOL Match Predictor is an application that predicts the outcome of a League of Legends match.

            Given certain inputs based off the current statistics of the match, the predictor will return whether the blue team will lose or win.

            Since it is difficult to predict the outcome of the game from the beginning, it is worth noting that the models used were trained
            using data by the 10 minute mark.
            
            Thus, to have an accurate prediction, it is recommended to wait at least 10 minutes into the game before inputing the values.

            """
        ),
        dcc.Link(dbc.Button('Your Call To Action', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])