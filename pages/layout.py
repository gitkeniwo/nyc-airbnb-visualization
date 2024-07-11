from dash import Dash, Input, Output, html

import sys

sys.path.append('..')

from components.map import create_map_layout
from components.violin import create_violin_layout
from components.matrix import create_matrix_fig
from .radar_layout import create_radar_layout
from .textual_analysis_layout import create_freq_layout
from .histogram_layout import create_histogram_layout


def div_plot(title: str, description: str, fig) -> html.Div:
    return html.Div([

        html.Div([
            html.H1(className="title", children=title),
            html.P(className="description", children=description)
        ], className="title-container"),

        html.Div([fig], className="plot")

    ], className="child")


def div_row(*args) -> html.Div:
    return html.Div([*args], className="row")


def navbar():
    return html.Div(
        [html.Div(
            [html.Div(
                [html.Img(className="logo", src="https://tailwindui.com/img/logos/workflow-mark-indigo-500.svg"),
                 html.Div(["New York Airbnb Open Data Dashboard"], className="navbar-title")],
                className="navbar-container")],
            className="navbar-flex")],
        className="navbar")


def create_app_layout():
    return html.Div([
        navbar(),
        div_row(
            div_plot(
                "Geographic Analysis",
                "Geographic distribution of property attributes in NYC",
                create_map_layout()
            )
        ),
        div_row(
            div_plot(
                "Property Quantity Analysis",
                "Comparison of the number of listed properties over the different neighborhoods with respect "
                "to the different room type",
                create_histogram_layout(),
            ),
            div_plot(
                "Regional Price Distribution",
                "The distribution of property price with respect to properties age and neighbourhoods in New York "
                "City",
                create_violin_layout(),
            ),
            div_plot(
                "Regional Attribute Summary",
                "Means and medians attributes of Properties with the respect to the New York City Boroughs",
                create_radar_layout(),
            )
        ),
        div_row(
            div_plot(
                "Findings on Textual Data",
                "Word Frequency of housing rules and cancellation policy.",
                create_freq_layout(),
            ),
            div_plot(
                "Correlation Heatmap",
                "Correlation coefficient between the numeric features.",
                create_matrix_fig(),
            ),
        )
    ])
