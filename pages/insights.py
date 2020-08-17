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
        
            ## Insights

            As the amount of towers destroyed and kills eventually translate into team gold accumulation,
            we can just focus on the amount of gold each team has. The amount of gold can determine whether the team 
            has the economy to buy items that will influece the outcome of the game. Furthermore, there are so many 
            insights we can gather from the factors that lead to a gold advantage. 

            Having a gold lead can come from having destroyed more towers, killed more enemies, destroyed more wards,
            taken more dragons, heralds, and elite monsters, and many other factors. However, the most prominant factors
            are towers destroyed and kills obtained. This is due to the vision of the map each tower grants along with it's
            protection.

            Kills will also set the enemy team back since while they are dead, your own team can continue to accumulate resources.
            Thus, all of these factors lead to the final conclusion that a League of Legends match is determined by which team can
            create the largest gold lead. One way of doing that would be to accumulate as much gold as possible. However, if
            the opposing team is giving equal oppotunities to accumluate resources and build their economy as well, then your team
            will not be creating a gold lead.

            The answer is to look for ways to deny resources. Ways in which your team benefits while the enemy team is either set backed,
            or at most is stagnant. Taking away their towers, vision of the arena, time on the battlefield by killing them, jungle monsters,
            and every other resource is the key to victory. The following graph shows that the gold difference has a greater affect
            on the outcome of a match than the total amount of gold a team has. Each number in the cells shows us the outcome given each input
            of either variable, and the number represents how likely the blue team will win.


            """
        ),
    ],
)

column2 = dbc.Col(
    [
        html.Img(
            src="assets/pdp-blue-totalGold-goldDiff.png", className="img-fluid"
        ),
        dcc.Link(dbc.Button("Process", color="primary"), href="/process"),
    ]
)


layout = dbc.Row([column1, column2])
