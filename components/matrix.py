from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

matrix = pd.read_csv('./data/preprocessed.csv', low_memory=False)
attribute = ['neighbourhood_group', 'room_type', 'age', 'nei_price', 'service_fee', 'minimum_nights',
             'availability_365']
filtered_data = matrix[attribute].copy().dropna()

feature_corr = ['age', 'nei_price', 'service_fee', 'minimum_nights', 'availability_365']


def heatmap():
    # corr = filtered_data.corr(method='kendall') * 10
    corr = filtered_data[feature_corr].corr(method='kendall') * 10

    mask = np.triu(np.ones_like(corr, dtype=bool))
    corr_tri = corr.mask(mask).to_numpy().round(2)
    fig = px.imshow(corr_tri,
                    labels=dict(color="Correlation"),
                    x=list(corr.index.values),
                    y=list(corr.columns.values),
                    color_continuous_scale='purples',
                    zmin=-0.5, zmax=0.5,
                    )
    fig.update_traces(text=corr_tri, texttemplate="%{text}")
    fig.update_layout(
        margin=dict(
            # l=10,
            # r=10,
            # b=100,
            # t=100,
            pad=4
        ),
        xaxis_showgrid=False,
        xaxis={'side': 'bottom'},
        yaxis_showgrid=False,
        yaxis_autorange='reversed',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    return fig


def create_matrix_fig():
    layout = html.Div([
        dcc.Graph(id='graph', figure=heatmap())
    ])
    return layout
