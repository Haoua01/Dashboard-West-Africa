from financial_service import FinancialService

class NigerData(FinancialService):
    """ Class to manage data specific to Togo based on the type of financial service. """
    
    def __init__(self, service_type):
        # Dictionary mapping regions to their respective departments
        department_mapping = {
            "Niamey": ["Niamey I", "Niamey II", "Niamey III", "Niamey IV"],
            "Agadez": ["Aderbissinat", "Arlit", "Bilma", "Iférouane", "Ingall", "Tchirozérine"],
            "Diffa": ["Bosso", "Diffa", "Goudoumaria", "Maïné-Soroa", "N'Gourti", "N'Guigmi"],
            "Dosso": ["Boboye", "Dioundiou", "Dogondoutchi", "Dosso", "Falmèy", "Gaya", "Loga", "Tibiri"],
            "Maradi": ["Aguié", "Bermo", "Dakoro", "Gazaoua", "Guidan-Roumdji", "Madarounfa", "Mayahi", "Tessaoua"],
            "Tahoua": ["Abalak", "Bagaroua", "Birni N'Konni", "Bouza", "Illéla", "Kéita", "Madaoua", "Malbaza", "Tahoua", "Tassara", "Tchintabaraden", "Tillia"],
            "Tillabéri": ["Abala", "Ayérou", "Balleyara", "Banibangou", "Bankilaré", "Filingué", "Gothèye", "Kollo", "Ouallam", "Say", "Téra", "Tillabéri", "Torodi"],
            "Zinder": ["Belbédji", "Damagaram Takaya", "Dungass", "Gouré", "Magaria", "Matamèye", "Mirriah", "Tanout", "Takeita", "Tesker"]
        }

        # Dictionary holding the geographical coordinates of cities in Togo
        coordinates = {'Agadez': (16.972556, 7.990739), 'Diffa': (13.3130749, 12.6136611), 'Dosso': (13.0496369, 3.1944647), 'Maradi': (13.501206, 7.102534), 'Tahoua': (14.889922, 5.262149), 'Tillabéri': (13.72510675, 1.6961455845759024), 'Zinder': (13.8063421, 8.9891659), 'Niamey': (13.534712800000001, 2.01268986831725)}
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
                'Niamey': 79,
                'Maradi': 16,
                'Tahoua': 14,
                'Agadez': 9,
                'Zinder': 10,
                'Dosso': 9,
                'Diffa': 3,
                'Tillabéri': 6
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
