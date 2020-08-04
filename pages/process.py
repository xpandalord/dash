# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            The logistic regression model from the sklearn library, was trained on 64% of the following 
            [dataset](https://www.kaggle.com/bobbyscience/league-of-legends-diamond-ranked-games-10-min) 
            found on Kaggle.com. Then is was validated with the remaining 16% to make sure the accuracy score
            of the model was as high as possible. Between the Logistic Regression model and Random Forest Classifier,
            the Logistic Regression model proved to obtain a higher accuracy score. Thus the model was scored on
            the remaining 20% of the data to recieve the final test score. 
            
            After testing with permuation feature importance, I found out that the most prominent features that 
            affect the outcome of a League of Legends match was the gold difference and the total amount of gold
            for each team.
            
            Due to the League of Legends Championship Series Heads-Up Display, the picture on the right, having 
            the prominent stats displayed at the top, it would be easy for the user of this application to input 
            the number of towers destroyed by either team, the amount of gold each team has, and the amount of kills 
            each team has as well. Before having my model predict based off of the inputs, I generate the gold difference
            first and have that be another input for my model to predict, since the gold difference is the largest
            contributing factor to the success of a team.

            Since the model was trained by statistics of a game by the 10 minute mark, all inputs are revolved around
            reasonable values that are achievable by that time. After all of that is done, either a picture that has blue 
            in it or a picture that has red in it comes up to tell the user which team is likely to win the game. You
            can follow this [link](https://xpandalord.github.io/2020-07-27-league-of-legends/) to my blog post that goes
            into futher details about how I came to my conclusions along with other techniques and graphs used in the
            process.


            """
        )
    ],
)

column2 = dbc.Col(
    [
        html.Img(src="assets/lcs-hud.jpg", className="img-fluid"),
        dcc.Link(dbc.Button("Home", color="primary"), href="/"),
    ]
)

layout = dbc.Row([column1, column2])
