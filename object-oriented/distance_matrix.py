import requests
import urllib.parse
from geopy.distance import great_circle
import time
from geographic_data import GeographicData
from geopy.geocoders import Nominatim

class DistanceMatrix():
    """
    Class for managing geographic data and computing the distance matrix based on time travel
    using Google Maps API after computing the neighbors using the compute_neighbors method.
    """

    def __init__(self, communes, country, api_key):
        self.api_key = api_key
        self.communes = communes
        self.country = country

    @staticmethod
    def get_commune_coordinates(list_communes, country):
        # Initialize geolocator
        geolocator = Nominatim(user_agent="commune_coordinates")

        # Dictionary to store the coordinates
        commune_coordinates = {}

        # Loop through the communes
        for commune in list_communes:
            try:
                # Get the coordinates of the commune
                location = geolocator.geocode(f'{commune}, {country}')
                if location:
                    commune_coordinates[commune] = (location.latitude, location.longitude)
                else:
                    print(f"Warning: {commune} not found.")
            except Exception as e:
                print(f"Error geocoding {commune}: {e}")
            # Pause for a few seconds to avoid overloading the server
            time.sleep(1)

        return commune_coordinates

    def get_distance_matrix(self):
        """
        Computes the travel time between each pair of communes only after neighbors have been computed.
        
        :param communes: List of communes to compute distances between.
        :return: A dictionary containing the travel time for each pair of communes.
        """
        # create an instance of the GeographicData class
        geo_data = GeographicData(self.get_commune_coordinates(self.communes, self.country))
        neighbors = geo_data.compute_neighbors(50)  
        
        distance_matrix = {}
        max_time_in_seconds = 2 * 60 * 60  # 2 hours in seconds

        for i, city in enumerate(self.communes):
            distance_matrix[city] = {}
            for j, city2 in enumerate(self.communes):
                if i < j and city in neighbors and city2 in neighbors[city]:  # Check if they are neighbors
                    # Encode cities for URL
                    origin_encoded = urllib.parse.quote(city)
                    destination_encoded = urllib.parse.quote(city2)
                    
                    print(f"Calculating travel time between {city} and {city2}")
                    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin_encoded}&destinations={destination_encoded}&key={self.api_key}"

                    try:
                        response = requests.get(url)
                        data = response.json()

                        if data['status'] == 'OK':
                            duration_in_seconds = data['rows'][0]['elements'][0]['duration']['value']
                            if duration_in_seconds <= max_time_in_seconds:
                                distance_matrix[city][city2] = duration_in_seconds
                                distance_matrix[city2] = distance_matrix.get(city2, {})
                                distance_matrix[city2][city] = duration_in_seconds
                        else:
                            print(f"Error retrieving travel time between {city} and {city2}: {data['status']}")
                    except Exception as e:
                        print(f"API request error for {city} and {city2}: {e}")
                    
                    # Pause to avoid hitting the API rate limit
                    time.sleep(0.1)

        return distance_matrix
