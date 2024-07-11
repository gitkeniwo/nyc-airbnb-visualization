import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, callback

df_violin = pd.read_csv('./data/preprocessed.csv', low_memory=False)  # load preprocessed data
violin = df_violin[df_violin.availability_365 < 1000]  # remove outlier

construct_year_list = violin[violin['age'].notna()]['age'].sort_values().unique()  # Sort age and make a list, drop na


def create_violin_layout():
    """
    Create a layout for the violin plot
    """
    layout = html.Div([
        html.P("Age of properties"),  # slider
        dcc.Slider(
            id='year-slider',
            min=violin['age'].min(),
            max=violin['age'].max(),
            value=violin.age.min(),
            marks={str(year): str(year) for year in construct_year_list.astype(int)},
            step=1.0
        ),
        dcc.RadioItems(
            id='yaxis-type',
            options=[{'label': i, 'value': j} for i, j in zip(
                ['Price', 'Availability in a Year', 'Service Fee'],
                ['price', 'availability_365', 'service_fee'])
                     ],
            value='price',
            labelStyle={'display': 'inline-block'},
            className="radio",
        ),
        dcc.Graph(id='graph-with-slider'),
    ])
    return layout


@callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'),
    Input('yaxis-type', 'value')
)
def update_figure(selected_year, yaxis_type):
    """
    # Violin plot for the chart
    # Input
    Value_YearSlider: str -> float
    Value_Yaxis: str (options)
    """

    fig = go.Figure()
    filtered_df = violin[violin.age == float(selected_year)]

    # x - building age
    borough_all = violin[violin['neighbourhood_group'].notna()]['neighbourhood_group'].unique().tolist()
    # y - could be price, popularity, service fee
    selected_type = yaxis_type

    for place in borough_all:

        # inconsistency naming
        if place == 'brookln':
            pass
        elif place == 'manhatan':
            pass
        else:
            # plot violin
            fig.add_trace(go.Violin(
                x=filtered_df['neighbourhood_group'][filtered_df["neighbourhood_group"] == place],
                y=filtered_df[selected_type][filtered_df["neighbourhood_group"] == place],
                name=place,
                box_visible=True,
                meanline_visible=True

            ))

    fig.update_layout(
        xaxis_title_text='NYC Boroughs',  # xaxis label
        yaxis_title_text="Property Price",  # yaxis label
        bargap=0.2,  # gap between bars of adjacent location coordinates
        bargroupgap=0.1,  # gap between bars of the same location coordinates
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title={
            'text': "Price Distribution in NYC Boroughs",
            'xanchor': 'center',
            'x': 0.5,
        },
    )

    return fig
