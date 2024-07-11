import pandas as pd

feature_names_long = ['Neighbourhood Price', 'Age', 'Availability in 365 days', 'Latitude', 'Longitude']

df = pd.read_csv('data/preprocessed.csv', low_memory=False)


def get_data(features: list) -> pd.DataFrame:
    return df[features].copy()
