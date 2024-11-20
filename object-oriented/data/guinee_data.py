from financial_service import FinancialService

class GuineeData(FinancialService):
    """ Class to manage data specific to Togo based on the type of financial service. """
    
    def __init__(self, service_type):
        # Dictionary mapping regions to their respective departments
        department_mapping = guinea_bissau_regions = {
            "Bafatá": "Bafatá",
            "Biombo": "Bissau",
            "Cacheu": "Cacheu",
            "Gabu": "Gabu",
            "Oio": "Safim",
            "Quinara": "Buba",
            "Tombali": "Canchungo",
            "Bissau": "Bissau",
            "Bolama": "Bolama"
        }


        # Dictionary holding the geographical coordinates of cities in Togo
        coordinates = {'Bafata': (12.1723403, -14.6555027), 'Biombo': (11.7343369, -15.9506571), 'Cacheu': (12.274246, -16.1648911), 'Gabu': (12.2819517, -14.2260818), 'Oio': (12.4823646, -15.2196439), 'Quinara': (11.591979, -14.994788), 'Tombali': (11.406411023846891, -15.284302802545074), 'Bissau': (11.861324, -15.583055), 'Bolama': (11.57763, -15.475261)}
        # Dictionary holding the population of cities in Togo
        population = {
            'Lomé': 2188376,
            'Kara': 158090,
            'Sokodé': 115442,
            'Atakpamé': 98193,
            'Dapaong': 117675
        }

        # Dictionary holding the area (in km²) of each region in Togo
        area = {
            'Maritime': 6100,
            'Plateaux': 16975,
            'Centrale': 13182,
            'Kara': 11738,
            'Savanes_Togo': 8602
        }


        super().__init__(department_mapping, coordinates, population, area)  # Initialize the parent class


        # Dictionary holding the number of agencies based on the service type
        if service_type.lower() == 'bank':
            self.agency_counts = {'Bissau': 24, 'Bafata': 5, 'Cacheu': 4, 'Gabu': 3, 'Quinara': 2, 'Biombo': 1, 'Oio': 0, 'Tombali': 0, 'Bolama': 0}
        elif service_type.lower() == 'mobile_money':
            self.agency_counts = {
            }
        elif service_type.lower() == 'microfinance':
            self.agency_counts = {
            }
        else:
            raise ValueError("Invalid service type. Choose from 'bank', 'mobile_money', or 'microfinance'.")
        

    def get_agency_counts(self):
        """Returns a dictionary containing the number of agencies per region."""
        return self.agency_counts

    def get_service_type(self):
        """Returns the type of financial service."""
        return self.service_type
    
    def get_department_mapping(self):
        return self.department_mapping
    
    def get_coordinates(self):
        """Returns the geographical coordinates for cities in Benin."""
        return self.coordinates
    
    def get_adult_population(self):
        """Calculates and returns the population over 15 years old for the regions."""
        return {region: 0.57 * pop for region, pop in self.population.items()}  # 57% of the total population
