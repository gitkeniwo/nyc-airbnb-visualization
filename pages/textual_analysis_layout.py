import sys

sys.path.append("..")

from dash import dcc, html
from components.textual_analysis_plot import get_word_freq, get_cancellation_policy

'''
LAYOUT for the word frequency component
'''


def create_freq_layout():
    """
    Create a layout for the word frequency plot
    """
    return html.Div([
        # Tab view
        dcc.Tabs([
            dcc.Tab(label='House Rules', children=[get_word_freq(top_n=15)]),
            dcc.Tab(label='Cancellation Policy', children=[get_cancellation_policy()]),
        ], className="tabs")
    ])
