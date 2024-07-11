from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd


token = 'pk.eyJ1IjoiZ29sZGVkaXRpb24yMTIiLCJhIjoiY2tld3dvMGxmMGJsbjM1bXV5cXNjam84cSJ9.32Xt4hp12-2Fa3Rk2XFLgQ'
airbnb = pd.read_csv('./data/preprocessed.csv', low_memory=False)

# Feature selection and data normalization
features = ["nei_price", "age", "availability_365", 'lat', 'long']
map_data = airbnb[features].copy()

rename = {'nei_price': 'Price', 'age': 'Age', 'availability_365': 'Availability in 365 days'}
map_data.rename(columns=rename, inplace=True)

feats = ["Price", "Age", "Availability in 365 days"]
options = ["Price Distribution", "Property Age Distribution", "Availability Distribution"]
option_feats = {opt: feat for opt, feat in zip(options, feats)}


# map layout
def create_map_layout():
    map_layout = html.Div([
        dcc.RadioItems(
            id='candidate',
            options=options,
            value="Price Distribution",
            inline=True,
            className="radio",
        ),
        dcc.Graph(id="map"),
    ])
    return map_layout


# Map Callbacks
@callback(
    Output("map", "figure"),
    Input("candidate", "value")
)
def display_choropleth(candidate):
    df = map_data
    fig = px.scatter_mapbox(df, lat='lat', lon='long', color=option_feats[candidate],
                            range_color=[df[option_feats[candidate]].min(), df[option_feats[candidate]].max()],
                            color_continuous_scale=px.colors.cyclical.IceFire
                            )
    fig.update_layout(mapbox_style="carto-positron")
    fig.update_layout(margin=dict(b=0, t=0, l=0, r=0))

    return fig
