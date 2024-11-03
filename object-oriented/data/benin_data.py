from financial_service import FinancialService

class BeninData(FinancialService):
    """
    Class to manage data specific to Benin based on the type of financial service.

    Attributes:
        service_type (str): The type of financial service (e.g., 'bank', 'mobile_money', 'microfinance').
        agency_counts (dict): A dictionary containing the number of agencies per region based on the service type.
        department_mapping (dict): A dictionary mapping regions to their respective departments.
        coordinates (dict): A dictionary containing the geographical coordinates of cities in Benin.
        population (dict): A dictionary containing the population of each region.
        area (dict): A dictionary containing the area (in km²) of each region.
        
    Methods:
        get_agency_counts(): Returns the agency counts for the specified service type.
        get_department_mapping(): Returns the department mapping for regions in Benin.
        get_coordinates(): Returns the geographical coordinates for cities in Benin.
        get_total_agencies(): Returns the total number of agencies across all regions for the specified service type.
        get_adult_population(): Returns the population over 15 years old for the regions.
        get_area(): Returns the area data for the regions.
        display_info(): Prints out the agency counts, department mapping, and coordinates.
    """
    
    def __init__(self, service_type):
        # Dictionary mapping regions to their respective departments
        department_mapping = {
            'Kandi': 'Alibori',
            'Natitingou': 'Atakora',
            'Ouidah': 'Atlantique',
            'Parakou': 'Borgou',
            'Savalou': 'Collines',
            'Dogbo-Tota': 'Couffo',
            'Djougou': 'Donga',
            'Cotonou': 'Littoral',
            'Lokossa': 'Mono',
            'Porto-Novo': 'Ouémé',
            'Sakété': 'Plateau',
            'Abomey': 'Zou'
        }
        
        # Dictionary holding the geographical coordinates of cities in Benin
        coordinates = {
            'Kandi': (11.13, 2.94),
            'Natitingou': (10.32, 1.38),
            'Ouidah': (6.37, 2.08),
            'Parakou': (9.34, 2.63),
            'Savalou': (8.03, 1.97),
            'Dogbo-Tota': (6.73, 1.78),
            'Djougou': (9.69, 1.57),
            'Cotonou': (6.37, 2.43),
            'Lokossa': (6.64, 1.72),
            'Porto-Novo': (6.47, 2.61),
            'Sakété': (6.74, 2.67),
            'Abomey': (7.18, 2.05)
        }

        # Dictionary holding the population of regions in Benin, 2013
        regions_population = {
            'Alibori': 867463,
            'Atakora': 772262,
            'Atlantique': 1398229,
            'Borgou': 1212249,
            'Collines': 717477,
            'Couffo':745328,
            'Donga':543130,
            'Littoral': 679012,
            'Mono':497243,
            'Ouémé':1100404,
            'Plateau':622372,
            'Zou':851580
        }

        # Dictionary holding the population of cities in Benin, 2013
        population = {
            'Kandi': 179290,
            'Natitingou': 103843,
            'Ouidah': 162034,
            'Parakou': 255478,
            'Savalou': 144549,
            'Dogbo-Tota': 103057,
            'Djougou': 267812,
            'Cotonou': 679012,
            'Lokossa': 104961,
            'Porto-Novo': 264320,
            'Sakété': 114088,
            'Abomey': 92266
        }

        # Dictionary holding the area (in km²) of regions in Benin
        area = {
            'Alibori': 26242,
            'Atakora': 20499,
            'Atlantique': 3233,
            'Borgou': 25856,
            'Collines': 13931,
            'Couffo': 2404,
            'Donga': 11126,
            'Littoral': 79,
            'Mono': 1605,
            'Ouémé': 1281,
            'Plateau': 3264,
            'Zou': 5243
        }

        super().__init__(department_mapping, coordinates, population, area)  # Initialize the parent class

        # Dictionary holding the number of agencies based on the service type
        if service_type.lower() == 'bank':
            self.agency_counts = {
                'Kandi': 5,
                'Natitingou': 3,
                'Ouidah': 17,
                'Parakou': 13,
                'Savalou': 4,
                'Dogbo-Tota': 1,
                'Djougou': 1,
                'Cotonou': 121,
                'Lokossa': 7,
                'Porto-Novo': 19,
                'Sakété': 0,
                'Abomey': 11
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
