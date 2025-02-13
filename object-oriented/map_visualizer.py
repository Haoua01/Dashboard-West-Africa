import folium
import plotly.express as px
from shapely.geometry import shape
import os 
from dotenv import load_dotenv
load_dotenv()

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

        #save the geo_data as a shapefile
        self.geo_data.to_file(f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/Shapefiles/{self.label}_{self.type}_{self.country}.shp')

        # Initialize a Folium map
        my_map = folium.Map(location=[self.lat, self.lon], zoom_start=self.zoom, scrollWheelZoom=False)

        # Jawg access token (replace this with your own token)
        jawg_access_token = os.getenv("JAWG_ACCESS_TOKEN")

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
            line_weight=0.7,
            legend_name='Score d\'accès',
            highlight=True
        ).add_to(my_map)

        # Add a tooltip to display information
        folium.GeoJson(
            self.geo_data.__geo_interface__,
            style_function=lambda feature: {
                'fillColor': 'Blues' if feature['properties'][f'{self.label}'] is not None else 'gray',
                'color': 'grey',
                'weight': 0.3,
                'fillOpacity': 0,
            },
            tooltip=folium.GeoJsonTooltip(
                fields=['admin1Name', f'{self.label}'],
                aliases=[f'{self.type}:', 'score:'],
                localize=True,
            )
        ).add_to(my_map)



        # Save the map as an HTML file
        folium_map_path = f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/{self.label}_{self.type}_{self.country}_leaflet.html'
        my_map.save(folium_map_path)

        print(f"Leaflet map generated")

    def create_leaflet_combined(self, geo_borders):
        # Add the scores to the GeoDataFrame
        self.geo_data[f'{self.label}'] = self.geo_data['admin1Name'].map(self.scores)

        self.geo_data['geometry'] = self.geo_data['geometry'].apply(lambda x: shape(x).simplify(0.01))

        self.geo_data = self.geo_data[['geometry', 'admin1Name', 'country', f'{self.label}']]

        #save the geo_data as a shapefile
        self.geo_data.to_file(f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/Shapefiles/{self.label}_{self.type}_{self.country}.shp')

        # Initialize a Folium map
        my_map = folium.Map(location=[self.lat, self.lon], zoom_start=self.zoom, scrollWheelZoom=False)

        # Jawg access token (replace this with your own token)
        jawg_access_token = os.getenv("JAWG_ACCESS_TOKEN")

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
            line_weight=0.3,
            legend_name='Score d\'accès',
            highlight=True
        ).add_to(my_map)

        # Add a tooltip to display information
        folium.GeoJson(
            self.geo_data.__geo_interface__,
            style_function=lambda feature: {
                'fillColor': 'gray',  # Set a neutral color for non-hovered regions (you can change this)
                'color': 'transparent',  # Make the border invisible
                'weight': 0,  # No border around the region
                'fillOpacity': 0,  # Make the fill transparent
            },
            highlight_function=lambda feature: {
                'color': 'grey',  # Set the border color on hover (optional)
                'weight': 1,  # Thicker border on hover
                'fillOpacity': 0,  # Set opacity when hovered
            },
            tooltip=folium.GeoJsonTooltip(
                fields=['admin1Name', f'{self.label}'],
                aliases=[f'{self.type}:', 'score:'],
                localize=True,
            )
        ).add_to(my_map)

        # Plot the borders with a choropleth layer
        c=folium.Choropleth(
            geo_data=geo_borders.__geo_interface__,
            name='choropleth2',
            data=geo_borders,
            columns=['country', 'Shape_Leng'],
            key_on='feature.properties.country',
            fill_opacity=0.8,
            line_opacity=0.7,
            line_weight=0.8,
            legend=False,
        )
        
        #remove second legend
        for key in c._children:
            if key.startswith('color_map'):
                del(c._children[key])
        c.add_to(my_map)



        # Save the map as an HTML file
        folium_map_path = f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/{self.label}_{self.type}_{self.country}_with_borders_leaflet.html'
        my_map.save(folium_map_path)

        print(f"Leaflet map combined generated")

    def create_leaflet_combined_tchad(self, geo_tchad, geo_borders):
        # Add the scores to the GeoDataFrame
        self.geo_data[f'{self.label}'] = self.geo_data['admin1Name'].map(self.scores)

        self.geo_data['geometry'] = self.geo_data['geometry'].apply(lambda x: shape(x).simplify(0.01))

        self.geo_data = self.geo_data[['geometry', 'admin1Name', 'country', f'{self.label}']]

        #save the geo_data as a shapefile
        self.geo_data.to_file(f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/Shapefiles/{self.label}_{self.type}_{self.country}.shp')

        # Initialize a Folium map
        my_map = folium.Map(location=[self.lat, self.lon], zoom_start=self.zoom, scrollWheelZoom=False)

        # Jawg access token (replace this with your own token)
        jawg_access_token = os.getenv("JAWG_ACCESS_TOKEN")

        # Add Jawg Light tiles with the access token
        folium.TileLayer(
            tiles="https://{s}.tile.jawg.io/jawg-light/{z}/{x}/{y}.png?access-token=" + jawg_access_token,
            attr="Map data &copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors, &copy; <a href='https://jawg.io/'>Jawg</a>",
            name="Jawg Light"
        ).add_to(my_map)

        # Plot the map in self with a choropleth layer
        folium.Choropleth(
            geo_data=self.geo_data.__geo_interface__,
            name='choropleth',
            data=self.geo_data,
            columns=['admin1Name', f'{self.label}'],
            key_on='feature.properties.admin1Name',
            fill_color='Blues',
            fill_opacity=1,
            line_opacity=0.2,
            line_weight=0.3,
            legend_name='Score d\'accès en UEMOA',
            highlight=True
        ).add_to(my_map)

        # Add a tooltip to display information
        folium.GeoJson(
            self.geo_data.__geo_interface__,
            style_function=lambda feature: {
                'fillColor': 'gray',  # Set a neutral color for non-hovered regions (you can change this)
                'color': 'transparent',  # Make the border invisible
                'weight': 0,  # No border around the region
                'fillOpacity': 0,  # Make the fill transparent
            },
            highlight_function=lambda feature: {
                'color': 'grey',  # Set the border color on hover (optional)
                'weight': 1,  # Thicker border on hover
                'fillOpacity': 0,  # Set opacity when hovered
            },
            tooltip=folium.GeoJsonTooltip(
                fields=['admin1Name', f'{self.label}'],
                aliases=[f'{self.type}:', 'score:'],
                localize=True,
            )
        ).add_to(my_map)

        # Plot the map of Tchad with a choropleth layer
        folium.Choropleth(
            geo_data=geo_tchad.__geo_interface__,
            name='choropleth',
            data=geo_tchad,
            columns=['admin1Name', f'{self.label}'],
            key_on='feature.properties.admin1Name',
            fill_color='Reds',
            fill_opacity=1,
            line_opacity=0.2,
            line_weight=0.3,
            legend_name='Score d\'accès au Tchad',
            highlight=True
        ).add_to(my_map)

        # Add a tooltip to display information
        folium.GeoJson(
            geo_tchad.__geo_interface__,
            style_function=lambda feature: {
                'fillColor': 'gray',  # Set a neutral color for non-hovered regions (you can change this)
                'color': 'transparent',  # Make the border invisible
                'weight': 0,  # No border around the region
                'fillOpacity': 0,  # Make the fill transparent
            },
            highlight_function=lambda feature: {
                'color': 'grey',  # Set the border color on hover (optional)
                'weight': 1,  # Thicker border on hover
                'fillOpacity': 0,  # Set opacity when hovered
            },
            tooltip=folium.GeoJsonTooltip(
                fields=['admin1Name', f'{self.label}'],
                aliases=['province:', 'score:'],
                localize=True,
            )
        ).add_to(my_map)


        # Plot the borders with a choropleth layer
        c=folium.Choropleth(
            geo_data=geo_borders.__geo_interface__,
            name='choropleth2',
            data=geo_borders,
            columns=['country', 'Shape_Leng'],
            key_on='feature.properties.country',
            fill_opacity=0.8,
            line_opacity=0.7,
            line_weight=0.8,
            legend=False,
        )
        
        #remove second legend
        for key in c._children:
            if key.startswith('color_map'):
                del(c._children[key])
        c.add_to(my_map)



        # Save the map as an HTML file
        folium_map_path = f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/{self.label}_{self.type}_{self.country}_with_borders_leaflet.html'
        my_map.save(folium_map_path)

        print(f"Leaflet map combined with Tchad generated")


    def create_leaflet_commune(self):
        """
        Create a map using Leaflet with basic interactive features.
        """
        # Add the scores to the GeoDataFrame
        self.geo_data[f'{self.label}'] = self.geo_data['ADM3_FR'].map(self.scores)

        self.geo_data['geometry'] = self.geo_data['geometry'].apply(lambda x: shape(x).simplify(0.01))

        self.geo_data = self.geo_data[['geometry', 'ADM3_FR', 'country', f'{self.label}']]

        #save the geo_data as a shapefile
        self.geo_data.to_file(f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/Shapefiles/{self.label}_{self.type}_{self.country}.shp')

        # Initialize a Folium map
        my_map = folium.Map(location=[self.lat, self.lon], zoom_start=self.zoom, scrollWheelZoom=False)

        # Jawg access token (replace this with your own token)
        jawg_access_token = os.getenv("JAWG_ACCESS_TOKEN")

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
            columns=['ADM3_FR', f'{self.label}'],
            key_on='feature.properties.ADM3_FR',
            fill_color='Blues',
            fill_opacity=1,
            line_opacity=0.1,
            line_weight=0.1,
            legend_name='Score d\'accès',
            highlight=True
        ).add_to(my_map)

        # Add a tooltip to display information
        folium.GeoJson(
            self.geo_data.__geo_interface__,
            style_function=lambda feature: {
                'fillColor': 'Blues' if feature['properties'][f'{self.label}'] is not None else 'gray',
                'color': 'grey',
                'weight': 0.1,
                'fillOpacity': 0,
            },
            tooltip=folium.GeoJsonTooltip(
                fields=['ADM3_FR', f'{self.label}'],
                aliases=[f'{self.type}:', 'score:'],
                localize=True,
            )
        ).add_to(my_map)



        # Save the map as an HTML file
        folium_map_path = f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/{self.label}_{self.type}_{self.country}_leaflet.html'
        my_map.save(folium_map_path)

        print(f"Leaflet commune map generated")
