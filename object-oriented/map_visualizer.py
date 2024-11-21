import folium
import plotly.express as px
from shapely.geometry import shape

class MapVisualizer:

    """
    Class for visualizing data on a map using Folium.

    Attributes:
        geo_data (GeoDataFrame): Geographic data used for visualization.

    Methods:
        create_choropleth(): Creates a choropleth map with the given values and title.
        create_leaflet(): Creates a cleaner map using Leaflet with Jawg Light basemap.
    """
    
    def __init__(self, geo_data, scores, label, type, lat, lon, zoom, country):
        self.geo_data = geo_data
        self.lat = lat
        self.lon = lon
        self.zoom = zoom
        self.scores = scores
        self.label = label
        self.type = type
        self.country = country



    def create_choropleth(self):

        # Add the scores to the GeoDataFrame

        self.geo_data[f'{self.label}'] = self.geo_data['admin1Name'].map(self.scores)

        self.geo_data['geometry'] = self.geo_data['geometry'].apply(lambda x: shape(x).simplify(0.01))

        self.geo_data = self.geo_data[['geometry', 'admin1Name', 'country', f'{self.label}']]

        # Convert to GeoJSON
        geojson_data = self.geo_data.__geo_interface__

        fig = px.choropleth_mapbox(
            self.geo_data,
            geojson=geojson_data,
            locations='admin1Name',  # Location column in your GeoDataFrame
            featureidkey='properties.admin1Name',  # This should match the GeoJSON structure
            color=f'{self.label}',  # Fill color with scores
            mapbox_style="carto-positron",
            zoom=self.zoom,
            center={"lat": self.lat, "lon": self.lon},
            #title=f"Score d'accès aux agences bancaires par {self.type}",
            hover_name="admin1Name",  # Region names
            hover_data={f'{self.label}': True, 'admin1Name': False},  # Show score but hide original name
            labels={'admin1Name': f'{self.type}', f'{self.label}': 'Score'},
            color_continuous_scale=px.colors.sequential.Blues,
            range_color=[0, 1]
        )
         

        # Save as HTML
        html_file_path = f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/{self.label}_{self.type}_{self.country}.html'

        # Save the map as HTML
        fig.write_html(html_file_path)

        print(f"Map generated and saved")

    def create_leaflet(self):
        """
        Create a map using Leaflet with basic interactive features.
        """
        # Add the scores to the GeoDataFrame
        self.geo_data[f'{self.label}'] = self.geo_data['admin1Name'].map(self.scores)

        self.geo_data['geometry'] = self.geo_data['geometry'].apply(lambda x: shape(x).simplify(0.01))

        self.geo_data = self.geo_data[['geometry', 'admin1Name', 'country', f'{self.label}']]

        # Initialize a Folium map
        my_map = folium.Map(location=[self.lat, self.lon], zoom_start=self.zoom)

        # Jawg access token (replace this with your own token)
        jawg_access_token = "dioMGYzKr2G5hw92MoTu8vvqmdOVm8zrb7lElgXzmBSo7pdqgvsTDCqV4UjS4hz2"

        # Add Jawg Light tiles with the access token
        folium.TileLayer(
            tiles="https://{s}.tile.jawg.io/jawg-light/{z}/{x}/{y}.png?access-token=" + jawg_access_token,
            attr="Map data &copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors, &copy; <a href='https://jawg.io/'>Jawg</a>",
            name="Jawg Light"
        ).add_to(my_map)

        # Plot the map with a choropleth layer
        folium.Choropleth(
            geo_data=self.geo_data.__geo_interface__,
            name='choropleth',
            data=self.geo_data,
            columns=['admin1Name', f'{self.label}'],
            key_on='feature.properties.admin1Name',
            fill_color='Blues',
            fill_opacity=1,
            line_opacity=0.2,
            line_weight=1,
            legend_name=f'{self.label}',
            highlight=True
        ).add_to(my_map)

        # Add a tooltip to display information
        folium.GeoJson(
            self.geo_data.__geo_interface__,
            style_function=lambda feature: {
                'fillColor': 'Blues' if feature['properties'][f'{self.label}'] is not None else 'gray',
                'color': 'black',
                'weight': 0.5,
                'fillOpacity': 0,
            },
            tooltip=folium.GeoJsonTooltip(
                fields=['admin1Name', f'{self.label}'],
                aliases=[f'{self.type}:', 'Score:'],
                localize=True,
            )
        ).add_to(my_map)

        # Save the map as an HTML file
        folium_map_path = f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/{self.label}_{self.type}_{self.country}_leaflet.html'
        my_map.save(folium_map_path)

        print(f"Leaflet map generated and saved at {folium_map_path}")

    def create_leaflet_combined(self):
        """
        Create a map using Leaflet with basic interactive features, Jawg Light tiles, and darker external borders.
        """
        # Add the scores to the GeoDataFrame
        self.geo_data[f'{self.label}'] = self.geo_data['admin1Name'].map(self.scores)
        print(self.geo_data.columns)
        print(self.geo_data['country'])

        # Jawg access token (replace this with your own token)
        jawg_access_token = "dioMGYzKr2G5hw92MoTu8vvqmdOVm8zrb7lElgXzmBSo7pdqgvsTDCqV4UjS4hz2"

        # Initialize a Folium map with Jawg Light tiles
        my_map = folium.Map(
            location=[self.lat, self.lon],
            zoom_start=self.zoom,
            control_scale=True
        )

        # Add Jawg Light tiles with the access token
        folium.TileLayer(
            tiles="https://{s}.tile.jawg.io/jawg-light/{z}/{x}/{y}.png?access-token=" + jawg_access_token,
            attr="Map data &copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors, &copy; <a href='https://jawg.io/'>Jawg</a>",
            name="Jawg Light"
        ).add_to(my_map)

        # Plot the map with a choropleth layer
        folium.Choropleth(
            geo_data=self.geo_data.__geo_interface__,
            name='choropleth',
            data=self.geo_data,
            columns=['admin1Name', f'{self.label}'],
            key_on='feature.properties.admin1Name',
            fill_color='Blues',  # Color scale for the choropleth
            fill_opacity=1,  # Set the opacity for internal borders
            line_opacity=0.4,  # Set the opacity for internal borders
            line_weight=1,  # Weight for internal borders
            legend_name=f'{self.label}',
            highlight=True  # Make highlighted regions stand out when hovered over
        ).add_to(my_map)

        # Iterate over each country and style external borders
        for country in self.geo_data['country'].unique():
            # Identify external borders (regions where the 'country' is different from the current country)
            external_borders = self.geo_data[self.geo_data['country'] != country]

            # Add custom styling for external borders (borders with other countries)
            folium.GeoJson(
                external_borders.__geo_interface__,
                style_function=lambda feature: {
                    'fillColor': 'none',  # No fill color for external borders
                    'color': 'black',  # Dark color for external borders
                    'weight': 2,  # Thicker line weight for external borders
                    'fillOpacity': 0.0  # Transparent fill
                }
            ).add_to(my_map)

            # Internal borders (within the same country) - not external borders
            internal_borders = self.geo_data[self.geo_data['country'] == country]

            # Add custom styling for internal borders (same country regions)
            folium.GeoJson(
                internal_borders.__geo_interface__,
                style_function=lambda feature: {
                    'fillColor': 'Blues' if feature['properties'][f'{self.label}'] is not None else 'gray',
                    'color': 'grey',
                    'weight': 0.5,
                    'fillOpacity': 0,
                },
                tooltip=folium.GeoJsonTooltip(
                    fields=['admin1Name', f'{self.label}'],
                    aliases=[f'{self.type}:', 'Score:'],
                    localize=True,
                    sticky=True  # Makes the tooltip sticky on hover
                )
            ).add_to(my_map)

        # Add a layer control if needed
        folium.LayerControl().add_to(my_map)

        # Save the map as an HTML file
        folium_map_path = f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/{self.label}_{self.type}_{self.country}_leaflet.html'
        my_map.save(folium_map_path)

        print(f"Leaflet map generated and saved at {folium_map_path}")