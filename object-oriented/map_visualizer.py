import folium
import plotly.express as px

class MapVisualizer:

    """
    Class for visualizing data on a map using Folium.

    Attributes:
        geo_data (GeoDataFrame): Geographic data used for visualization.

    Methods:
        create_choropleth(values, title): Creates a choropleth map with the given values and title.
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

        """
        my_map = folium.Map(location=[self.lat, self.lon], zoom_start=5)

        # Plot the map
        folium.Choropleth(
            geo_data=self.geo_data,
            name='choropleth',
            data=self.geo_data,
            columns=['admin1Name', f'{self.label}'],
            key_on='feature.properties.admin1Name',
            fill_color='YlGn',
            fill_opacity=0.9,
            line_opacity=0.2,
            line_weight=2,
            legend_name=f'{self.label}'
        ).add_to(my_map)

        # Add a tooltip to display information
        folium.GeoJson(
            self.geo_data.__geo_interface__,
            style_function=lambda feature: {
                'fillColor': 'YlGn' if feature['properties'][f'{self.label}'] is not None else 'gray',
                'color': 'grey',
                'weight': 0.5,
                'fillOpacity': 0.2,
            },
            tooltip=folium.GeoJsonTooltip(
                fields=['admin1Name', f'{self.label}'],
                aliases=[f'{self.type}:', 'Score:'],
                localize=True,
            )
        ).add_to(my_map)
        """

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