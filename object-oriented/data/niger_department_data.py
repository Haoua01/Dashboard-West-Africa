from financial_service import FinancialService

class NigerDepartmentData(FinancialService):
    """ Class to manage data specific to Togo based on the type of financial service. """
    
    def __init__(self, service_type):
        # Dictionary mapping regions to their respective departments
        department_mapping = {
            "Niamey": ["Niamey"],
            "Agadez": ["Aderbissinat", "Arlit", "Bilma", "Iférouane", "Ingall", "Tchirozérine"],
            "Diffa": ["Bosso", "Diffa", "Goudoumaria", "Maïné-Soroa", "N\'Gourti", "N\'Guigmi"],
            "Dosso": ["Boboye", "Dioundiou", "Dogondoutchi", "Dosso", "Falmèy", "Gaya", "Loga", "Tibiri"],
            "Maradi": ["Aguié", "Bermo", "Dakoro", "Gazaoua", "Guidan-Roumdji", "Madarounfa", "Mayahi", "Tessaoua", "Maradi"],
            "Tahoua": ["Abalak", "Bagaroua", "Birni N\'Konni", "Bouza", "Illéla", "Kéita", "Madaoua", "Malbaza", "Tahoua", "Tassara", "Tchintabaraden", "Tillia"],
            "Tillabéri": ["Abala", "Ayérou", "Balleyara", "Banibangou", "Bankilaré", "Filingué", "Gothèye", "Kollo", "Ouallam", "Say", "Téra", "Tillabéri", "Torodi"],
            "Zinder": ["Belbédji", "Damagaram Takaya", "Dungass", "Gouré", "Magaria", "Matamèye", "Mirriah", "Tanout", "Takeita", "Tesker", "Zinder", 'Kantché']
        }

        # Dictionary holding the geographical coordinates of cities in Togo
        coordinates = {'Niamey': (13.534712800000001, 2.01268986831725), 'Aderbissinat': (15.6182482, 7.8956817), 'Arlit': (18.739079, 7.393331), 'Bilma': (18.69293, 12.91872), 'Iférouane': (19.0678966, 8.4202829), 'Ingall': (16.7861094, 6.9321705), 'Tchirozérine': (17.266115, 7.832831), 'Bosso': (13.700055, 13.3112436), 'Diffa': (13.3130749, 12.6136611), 'Kantché': (13.539498, 8.462786), 'Goudoumaria': (13.7106995, 11.1885339), 'Maïné-Soroa': (13.2151567, 12.0280819), "N'Gourti": (15.3264167, 13.19605), "N'Guigmi": (14.253302, 13.113545), 'Boboye': (12.94531, 2.845741315640881), 'Dioundiou': (12.619361, 3.544343), 'Dogondoutchi': (13.6411218, 4.0293627), 'Dosso': (13.0496369, 3.1944647), 'Falmèy': (12.594472, 2.852715), 'Gaya': (11.884754, 3.459885), 'Loga': (13.6150486, 3.231257), 'Tibiri': (13.1112228, 4.0001684), 'Aguié': (13.5009617, 7.7759347), 'Bermo': (14.99132125, 6.972607043623567), 'Dakoro': (14.509465, 6.7644526), 'Gazaoua': (13.5271777, 7.9125927), 'Guidan-Roumdji': (13.66107, 6.696541), 'Madarounfa': (13.3031734, 7.1616587), 'Mayahi': (13.953305, 7.672419), 'Tessaoua': (13.755513, 7.990456), 'Maradi': (13.501206, 7.102534), 'Abalak': (15.463729, 6.281312), 'Bagaroua': (14.6395512, 4.3475296), "Birni N'Konni": (13.791612, 5.24779), 'Bouza': (14.423489, 6.043656), 'Illéla': (14.34675, 5.039007519168555), 'Kéita': (14.801449999999999, 6.059116216053109), 'Madaoua': (14.0708, 5.9553), 'Malbaza': (13.9602829, 5.5071021), 'Tahoua': (14.889922, 5.262149), 'Tassara': (16.8089516, 5.6481871), 'Tchintabaraden': (15.8982622, 5.8036112), 'Tillia': (16.137927, 4.792211), 'Abala': (14.9320767, 3.4298122), 'Ayérou': (14.822403600000001, 0.8622459013637926), 'Balleyara': (13.7841021, 2.9515071), 'Banibangou': (15.0393641, 2.7016766), 'Bankilaré': (14.5828541, 0.725173), 'Filingué': (14.351996, 3.324134), 'Gothèye': (13.8571396, 1.5665107), 'Kollo': (13.72510675, 1.6961455845759024), 'Ouallam': (14.315757, 2.084779), 'Say': (13.1024623, 2.3626379), 'Téra': (13.72510675, 1.6961455845759024), 'Tillabéri': (13.72510675, 1.6961455845759024), 'Torodi': (13.114744550000001, 1.4660878125590242), 'Belbédji': (14.9860422, 7.8136469840236735), 'Damagaram Takaya': (14.1383821, 9.482686), 'Dungass': (13.0634643, 9.3405575), 'Gouré': (13.9861879, 10.2642868), 'Magaria': (13.000948, 8.9086775), 'Matamèye': (13.422144, 8.47855), 'Mirriah': (13.7145507, 9.1585561), 'Tanout': (14.97119, 8.878363), 'Takeita': (13.93883875, 8.867422127727208), 'Tesker': (15.1159083, 10.6956447), 'Zinder': (13.8063421, 8.9891659)}
        
        # Total population of Niger, Africapolis
        population = 24206636 

        # Total area (in km²) of Niger
        area = 1267000

        super().__init__(department_mapping, coordinates, population, area)  # Initialize the parent class


        # Dictionary holding the number of agencies based on the service type
        if service_type.lower() == 'bank':
            self.agency_counts = {'Niamey': 79, 'Maradi': 13, 'Tahoua': 8, 'Zinder': 8, 'Tchirozérine': 7, 'Arlit': 2, 'Birni N\'Konni': 5, 'Dosso': 4, 'Gaya': 4, 'Tillabéri': 4, 'Diffa': 3, 'Tessaoua': 2, 'Madaoua': 1, 'Torodi': 1, 'Magaria': 1, 'Dakoro': 1, 'Téra': 1, 'Aderbissinat': 0, 'Bilma': 0, 'Iférouane': 0, 'Ingall': 0, 'Tchirozérine': 0, 'Bosso': 0, 'Goudoumaria': 0, 'Maïné-Soroa': 0, "N'Gourti": 0, "Kantché": 0, "N'Guigmi": 0, 'Boboye': 0, 'Dioundiou': 0, 'Dogondoutchi': 1, 'Falmèy': 0, 'Loga': 0, 'Tibiri': 0, 'Aguié': 0, 'Bermo': 0, 'Gazaoua': 0, 'Guidan-Roumdji': 0, 'Madarounfa': 0, 'Mayahi': 0, 'Abalak': 0, 'Bagaroua': 0, "Birni N'Konni": 0, 'Bouza': 0, 'Illéla': 0, 'Kéita': 0, 'Malbaza': 0, 'Tassara': 0, 'Tchintabaraden': 0, 'Tillia': 0, 'Abala': 0, 'Ayérou': 0, 'Balleyara': 0, 'Banibangou': 0, 'Bankilaré': 0, 'Filingué': 0, 'Gothèye': 0, 'Kollo': 0, 'Ouallam': 0, 'Say': 0, 'Torodi': 0, 'Belbédji': 0, 'Damagaram Takaya': 0, 'Dungass': 0, 'Gouré': 0, 'Matamèye': 1, 'Mirriah': 0, 'Tanout': 0, 'Takeita': 0, 'Tesker': 0}
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
    
    def get_area(self):
        """Returns the area of regions in Benin."""
        return self.area
    
    def get_adult_population(self):
        """Calculates and returns the population over 15 years old for the regions."""
        return 0.4884 * self.population  # 48.84% of the total population
