import sys

sys.path.append('..')
from dash import html, dcc, callback, Output, Input

from components.histogram import create_histogram


def create_histogram_layout():
    return html.Div(
        id="app-container",
        children=[
            html.Div(id='dropdown',
                     children=[dcc.Dropdown(['Entire home', 'Private room', 'Shared room', 'Hotel room'],
                                            'Entire home',
                                            id='demo-dropdown'),
                               html.Div(id='dd-output-container')],
                     )
        ],
    )


@callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    histogram = create_histogram()
    return histogram.update(value)
