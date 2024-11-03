from financial_service import FinancialService

class TogoData(FinancialService):
    """ Class to manage data specific to Togo based on the type of financial service. """
    
    def __init__(self, service_type):
        # Dictionary mapping regions to their respective departments
        department_mapping = {
            'Lomé': 'Maritime',
            'Kara': 'Kara',
            'Sokodé': 'Centrale',
            'Atakpamé': 'Plateaux',
            'Dapaong': 'Savanes_Togo'
        }
        
        # Dictionary holding the geographical coordinates of cities in Togo
        coordinates = {
            'Lomé': (6.13, 1.22),
            'Kara': (9.55, 1.19),
            'Sokodé': (8.99, 1.13),
            'Atakpamé': (7.53, 1.13),
            'Dapaong': (10.86, 0.20),
        }

        # Dictionary holding the population of each region in Togo
        regions_population = {
            'Kara': 985512,
            'Centrale': 795529,
            'Maritime': 1346615+2188376,
            'Plateaux': 1635946,
            'Savanes_Togo': 1143520
        }

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
            self.agency_counts = {
                'Kara': 19,
                'Sokodé': 10,
                'Atakpamé': 16,
                'Lomé': 112,
                'Dapaong': 19
            }
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
