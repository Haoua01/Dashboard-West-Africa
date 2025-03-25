from geopy.distance import great_circle
from shapefile import Shapefile
from geopy.geocoders import Nominatim
import time
import requests
import json

class GeographicData:
    """
    Class for managing geographic data and computing neighbors based on distances.

    Attributes:
        coordinates (dict): A dictionary where keys are city names and values are their (latitude, longitude) tuples.

    Methods:
        compute_neighbors(distance_threshold): Computes a dictionary of neighboring regions based on a distance threshold.
    """
    
    def __init__(self, coordinates):
        self.coordinates = coordinates  # Expecting a dictionary of coordinates

    def compute_neighbors_new(self, distance_threshold, api_key):
        neighbors = {}
        for city1, coords1 in self.coordinates.items():
            neighbors[city1] = {}
            for city2, coords2 in self.coordinates.items():
                if city1 != city2:
                    distance = great_circle(coords1, coords2).kilometers
                    if distance <= distance_threshold:
                        origins = f"{coords1[0]},{coords1[1]}"
                        destinations = f"{coords2[0]},{coords2[1]}"
                        url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={destinations}&key={api_key}'
                        try:
                            response = requests.get(url)
                            data = response.json()
                            if response.status_code != 200 or 'rows' not in data or not data['rows']:
                                print(f"No valid distance matrix data for {city1} to {city2}")
                                continue
                            for i, element in enumerate(data['rows'][0]['elements']):
                                if element['status'] == 'OK':
                                    duration = element['duration']['value'] // 60
                                    neighbors[city1][city2] = duration
                                    break
                        except requests.exceptions.RequestException as e:
                            print(f"Request error for {city1} to {city2}: {e}")
                            continue
        #save as json
        with open('neighbors.json', 'w') as f:
            json.dump(neighbors, f)


    def compute_neighbors2(self, distance_threshold, countries):
        neighbors = {}
        # Loop over countries
        for country in countries:
            neighbors[country] = {}  # Initialize country key
            
            # Loop over each city in the country
            for city1, coords1 in self.coordinates[country].items():
                neighbors[country][city1] = {}  # Initialize city1 key within the country
                
                # Loop over each city again for comparison (to check neighbors)
                for city2, coords2 in self.coordinates[country].items():
                    if city1 != city2:  # Skip if it's the same city
                        # Calculate the distance between the two cities
                        distance = great_circle(coords1, coords2).kilometers
                        
                        # If the distance is within the threshold, consider it a neighbor
                        if distance <= distance_threshold:
                            neighbors[country][city1][city2] = distance  # Add city2 as a neighbor of city1
        
        with open('neighbors_great_circle4.json', 'w') as f:
            json.dump(neighbors, f)

    def compute_neighbors(self, distance_threshold, countries):
        neighbors = {}
        for city1, coords1 in self.coordinates.items():
            neighbors[city1] = {}
            for city2, coords2 in self.coordinates.items():
                if city1 != city2:
                    distance = great_circle(coords1, coords2).kilometers
                    if distance <= distance_threshold:
                            neighbors[city1][city2] = distance    
        #print("Neighbor's distances successfully computed.")
        return neighbors
    
    @staticmethod
    def get_coordinates(department_mapping, country):
        # Initialize geolocator
        geolocator = Nominatim(user_agent="department_coordinates")

        # Dictionary to store the coordinates
        department_coordinates = {}

        # Loop through the departments in the mapping
        for region, departments in department_mapping.items():
            for department in departments:
                try:
                    # Get the coordinates of the department
                    location = geolocator.geocode(f'{department}, {region}, {country}')
                    if location:
                        department_coordinates[department] = (location.latitude, location.longitude)
                    else:
                        print(f"Warning: {department} not found.")
                except Exception as e:
                    print(f"Error geocoding {department}: {e}")
                # Pause for a few seconds to avoid overloading the server
                time.sleep(1)

        return department_coordinates
    

    



