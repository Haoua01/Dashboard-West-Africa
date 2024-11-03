from geopy.distance import great_circle

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
        return neighbors
