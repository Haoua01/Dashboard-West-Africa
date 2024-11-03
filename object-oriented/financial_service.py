from abc import ABC, abstractmethod

class FinancialService(ABC):

    """
    Abstract base class representing a generic financial service.

    Attributes:
        agency_counts (dict): A dictionary containing the number of agencies per region.
        department_mapping (dict): A dictionary mapping agencies to their respective departments.
        coordinates (dict): A dictionary containing the geographical coordinates of cities.

    Methods:
        get_service_type(): Abstract method to return the type of financial service.
        get_agency_data(): Returns agency data, including counts, departments, and coordinates.
    """

    def __init__(self, department_mapping, coordinates, population, area):
        self.department_mapping = department_mapping  
        self.coordinates = coordinates
        self.population = population
        self.area = area

        
    @abstractmethod
    def get_service_type(self):
        pass

    @abstractmethod
    def get_agency_counts(self):
        pass

    def get_agency_data(self):
        return {
            'counts': self.get_agency_counts(),
            'departments': self.department_mapping,
            'coordinates': self.coordinates,
            'population': self.population,
            'area': self.area
        }
