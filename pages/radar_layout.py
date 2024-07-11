import sys

sys.path.append("..")

from dash import Dash, dcc, html, Input, Output, callback
from components.radar import radar_fig


def create_radar_layout():
    """
    Create a layout for the radar plot
    """
    return html.Div([
        html.Div([
            # multiselect dropdown
            dcc.Dropdown(
                ['Overall', 'Manhattan', 'Brooklyn', 'Queens', 'Staten Island', 'Bronx'],
                multi=True,
                id='radar-neighborhood-select',
                value=['Overall']
            ),
            # radiobutton
            dcc.RadioItems(
                ['Mean', 'Median'],
                'Median',
                id='radar-method',
                inline=True,
                className="radio",
            ),
        ]),
        # radar graph
        dcc.Graph(id='radar-plot', figure=radar_fig(neighbours=['Manhattan'])),
    ])


@callback(
    Output(component_id='radar-plot', component_property='figure'),
    Input(component_id='radar-neighborhood-select', component_property='value'),
    Input(component_id='radar-method', component_property='value')
)
def update_radar(neighborhood_select, method):
    if neighborhood_select:
        return radar_fig(neighbours=neighborhood_select, method=method)
    else:
        return radar_fig(neighbours=["Overall"], method=method)
