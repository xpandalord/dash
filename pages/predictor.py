# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
pipeline = load('assets/pipeline.joblib')

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Inputs', className='mb-5'), 
        dcc.Markdown('#### \# of Towers the Blue Team Destroyed'), 
        dcc.Slider(
            id='blueTowersDestroyed', 
            min=0, 
            max=4, 
            step=1, 
            value=0, 
            marks={n: str(n) for n in range(0,5,1)}, 
            className='mb-5',
        ), 
        dcc.Markdown('#### Blue Team\'s Total Gold'), 
        dcc.Slider(
            id='blueTotalGold', 
            min=0, 
            max=25000, 
            step=1000, 
            value=0, 
            marks={n: str(n) for n in range(0,25001,5000)},
            className='mb-5',
        ), 
        dcc.Markdown('#### Blue Team\'s Total Kills'), 
        dcc.Slider(
            id='blueKills', 
            min=0, 
            max=25, 
            step=1, 
            value=0, 
            marks={n: str(n) for n in range(0,26,5)}, 
            className='mb-5',
        ),
        dcc.Markdown('#### Red Team\'s Total Kills'), 
        dcc.Slider(
            id='redKills', 
            min=0, 
            max=25, 
            step=1, 
            value=0, 
            marks={n: str(n) for n in range(0,26,5)}, 
            className='mb-5',
        ),
        dcc.Markdown('#### Red Team\'s Total Gold'), 
        dcc.Slider(
            id='redTotalGold', 
            min=0, 
            max=25000, 
            step=1000, 
            value=0, 
            marks={n: str(n) for n in range(0,25001,5000)}, 
            className='mb-5',
        ),
        dcc.Markdown('#### \# of Towers the Red Team Destroyed'), 
        dcc.Slider(
            id='redTowersDestroyed', 
            min=0, 
            max=4, 
            step=1, 
            value=0, 
            marks={n: str(n) for n in range(0,5,1)}, 
            className='mb-5',
        )
        
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Outcome', className='mb-5'), 
        html.Div(id='prediction-content', className='lead'),
        dcc.Link(dbc.Button('Insights', color='primary'), href='/insights')
    ]
)

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('blueTowersDestroyed', 'value'), Input('blueTotalGold', 'value'), Input('blueKills', 'value'), 
     Input('redKills', 'value'), Input('redTotalGold', 'value'), Input('redTowersDestroyed', 'value')],
)
def predict(blueTowersDestroyed, blueTotalGold, blueKills, redKills, redTotalGold, redTowersDestroyed):
    blueGoldDiff = blueTotalGold - redTotalGold
    df = pd.DataFrame(
        columns=['blueTowersDestroyed', 'blueTotalGold', 'blueKills',
                'redKills', 'redTotalGold', 'redTowersDestroyed', 'blueGoldDiff'], 
        data=[[blueTowersDestroyed, blueTotalGold, blueKills,
                redKills, redTotalGold, redTowersDestroyed, blueGoldDiff]]
    )
    y_pred = pipeline.predict(df)[0]
    if y_pred == 1:
        return html.Img(src='assets/blue-victory.jpg', className='img-fluid')
    else:
        return html.Img(src='assets/red-team-win.jpg', className='img-fluid')

layout = dbc.Row([column1, column2])