from geopy.distance import great_circle

from geopy.geocoders import Nominatim
import time
import logging

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

    def compute_neighbors(self, distance_threshold):
        neighbors = {}
        for city1, coords1 in self.coordinates.items():
            neighbors[city1] = {}
            for city2, coords2 in self.coordinates.items():
                if city1 != city2:
                    distance = great_circle(coords1, coords2).kilometers
                    if distance <= distance_threshold:
                        neighbors[city1][city2] = distance
        print("Neighbor's distances successfully computed.")
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


