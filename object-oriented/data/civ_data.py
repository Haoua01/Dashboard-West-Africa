from financial_service import FinancialService

class CIVData(FinancialService):
    """Class to manage data specific to Côte d'Ivoire based on the type of financial service."""
    
    def __init__(self, service_type):

        # Dictionary mapping regions to their respective departments
        department_mapping = {
            'Abidjan': 'Abidjan',
            'San-Pédro': 'Bas-Sassandra',
            'Abengourou': 'Comoé',
            'Odienné': 'District du Denguélé',
            'Gagnoa': 'Gôh-Djiboua',
            'Dimbokro': 'Lacs',
            'Dabou': 'Lagunes',
            'Man': 'Montagnes',
            'Daloa': 'Sassandra-Marahoué',
            'Korhogo': 'Savanes_CIV',
            'Bouaké': 'Vallée du Bandama',
            'Séguéla': 'Woroba',
            'Yamoussoukro': 'Yamoussoukro',
            'Bondoukou': 'Zanzan'
        }
        
        # Dictionary holding the geographical coordinates of cities in Côte d'Ivoire
        coordinates = {
            'Abidjan': (5.32, -4.03),
            'San-Pédro': (4.95, -6.08),
            'Abengourou': (5.18, -3.28),
            'Odienné': (9.59, -7.54),
            'Gagnoa': (6.07, -5.94),
            'Dimbokro': (6.81, -5.18),
            'Dabou': (5.90, -3.93),
            'Man': (7.38, -7.56),
            'Daloa': (6.21, -5.90),
            'Korhogo': (9.41, -5.63),
            'Bouaké': (7.70, -5.03),
            'Séguéla': (8.22, -6.49),
            'Yamoussoukro': (6.82, -5.27),
            'Bondoukou': (8.06, -2.78)
        }

        # Dictionary holding the population of each region in Côte d'Ivoire, 2021
        regions_population = {
            'Abidjan': 6321017,
            'Bas-Sassandra': 2687176,
            'Comoé': 1501336,
            'District du Denguélé': 436015,
            'Gôh-Djiboua': 2088440,
            'Lacs': 1488531,
            'Lagunes': 2042623,
            'Montagnes': 3027023,
            'Sassandra-Marahoué': 2720876,
            'Savanes_CIV': 2159434,
            'Vallée du Bandama': 1964929,
            'Woroba': 1184813,
            'Yamoussoukro': 422072,
            'Zanzan': 1344865
        }

        # Dictionary holding the population of each cities in Côte d'Ivoire, 2021
        population = {
            'Abidjan': 5616633,
            'San-Pédro': 790242,
            'Abengourou': 430539,
            'Odienné': 156730,
            'Gagnoa': 724496,
            'Dimbokro': 102192,
            'Dabou': 213582,
            'Man': 461135,
            'Daloa': 705378,
            'Korhogo': 748393,
            'Bouaké': 931851,
            'Séguéla': 298384,
            'Yamoussoukro': 372559,
            'Bondoukou': 453841
        }
        
        # Dictionary holding the area (in km²) of each region in Côte d'Ivoire
        area = {
            'Abidjan': 2119,
            'Bas-Sassandra': 26680,
            'Comoé': 14200,
            'District du Denguélé': 20600,
            'Gôh-Djiboua': 21300,
            'Lacs': 12190,
            'Lagunes': 13323,
            'Montagnes': 16600,
            'Sassandra-Marahoué': 19840,
            'Savanes_CIV': 40210,
            'Vallée du Bandama': 28530,
            'Woroba': 31140,
            'Yamoussoukro': 3500,
            'Zanzan': 38000
        }

        super().__init__(department_mapping, coordinates, population, area)  # Initialize the parent class

        # Dictionary holding the number of agencies based on the service type
        if service_type.lower() == 'bank':
            self.agency_counts = {
                'Abidjan': 396,
                'San-Pédro': 40,
                'Abengourou': 27,
                'Odienné': 2,
                'Gagnoa': 20,
                'Dimbokro': 8,
                'Dabou': 15,
                'Man': 15,
                'Daloa': 23,
                'Korhogo': 24,
                'Bouaké': 20,
                'Séguéla': 4,
                'Yamoussoukro': 11,
                'Bondoukou': 1
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
