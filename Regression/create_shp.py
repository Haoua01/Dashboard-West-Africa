import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry import Point
import os

with open('results7/output_corrected.csv', 'r') as f:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(f)

# discard rows with GPS coordinate set to -999999999 
df = df[(df['GPS__Latitude'] != -999999999) & (df['GPS__Longitude'] != -999999999)]
# Ensure Latitude and Longitude are valid and not empty

# Create a GeoDataFrame from the DataFrame
df['GPS__Latitude'] = pd.to_numeric(df['GPS__Latitude'], errors='coerce')  # Convert to numbers, replace errors with NaN
df['GPS__Longitude'] = pd.to_numeric(df['GPS__Longitude'], errors='coerce')  # Same for Longitude


# Create a GeoDataFrame with geometry
geometry = [Point(xy) for xy in zip(df["GPS__Longitude"], df["GPS__Latitude"])]
gdf = GeoDataFrame(df, geometry=geometry)
gdf.to_file("results7/survey.shp")