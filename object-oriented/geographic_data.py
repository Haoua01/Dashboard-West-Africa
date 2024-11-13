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

    @staticmethod
    def get_department_coordinates(department_mapping, country):
        """
        Retrieves the geographic coordinates of departments by geocoding.

        Args:
            department_mapping (dict): A dictionary mapping regions to their respective departments.
            country (str): The country name.

        Returns:
            dict: A dictionary where the key is the department name and the value is a tuple (latitude, longitude).
        """

        geolocator = Nominatim(user_agent="department_coordinates")
        department_coordinates = {}

        for region, departments in department_mapping.items():
            for department in departments:
                try:
                    location = geolocator.geocode(f'{department}, {region}, {country}')
                    if location:
                        department_coordinates[department] = (location.latitude, location.longitude)
                    else:
                        logging.warning(f"Warning: {department} not found in {region}, {country}.")
                except Exception as e:
                    logging.error(f"Error geocoding {department}: {e}")
                time.sleep(1)
        print("Coordinates successfully retrieved.")
        return department_coordinates

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
    

