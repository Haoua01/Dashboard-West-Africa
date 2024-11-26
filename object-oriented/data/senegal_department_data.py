from financial_service import FinancialService

class SenegalDepartmentData(FinancialService):
    """ Class to manage data specific to Togo based on the type of financial service. """
    
    def __init__(self, service_type):
        # Dictionary mapping regions to their respective departments
        department_mapping =  {
            "Dakar": ["Dakar", "Pikine", "Rufisque", "Guédiawaye", "Keur Massar"],
            "Ziguinchor": ["Bignona", "Oussouye", "Ziguinchor"],
            "Diourbel": ["Bambey", "Diourbel", "Mbacké"],
            "Saint Louis": ["Dagana", "Podor", "Saint Louis"],
            "Tambacounda": ["Bakel", "Tambacounda", "Goudiry", "Koumpentoum"],
            "Kaolack": ["Kaolack", "Nioro du Rip", "Guinguinéo"],
            "Thiès": ["Mbour", "Thiès", "Tivaouane"],
            "Louga": ["Kébémer", "Linguère", "Louga"],
            "Fatick": ["Fatick", "Foundiougne", "Gossas"],
            "Kolda": ["Kolda", "Vélingara", "Médina-Yorofoula"],
            "Matam": ["Kanel", "Matam", "Ranérou"],
            "Kaffrine": ["Kaffrine", "Birkelane", "Koungheul", "Malem-Hodar"],
            "Kédougou": ["Kédougou", "Salémata", "Saraya"],
            "Sédhiou": ["Sédhiou", "Bounkiling", "Goudomp"]
        }

        
        # Dictionary holding the geographical coordinates of cities in Togo
        coordinates = {'Dakar': (14.693425, -17.447938), 'Pikine': (14.751544, -17.396413), 'Rufisque': (14.716417, -17.273844), 'Guédiawaye': (14.7771207, -17.390071), 'Keur Massar': (14.7822567, -17.311199), 'Bignona': (12.801133, -16.22897), 'Oussouye': (12.4889623, -16.5432771), 'Ziguinchor': (12.5634929, -16.2724609), 'Bambey': (14.69548, -16.449262), 'Diourbel': (14.654562, -16.227822), 'Mbacké': (14.7971224, -15.9066608), 'Dagana': (16.516508, -15.50684), 'Podor': (16.652705, -14.958669), 'Saint Louis': (16.0280445, -16.5048686), 'Bakel': (14.9049666, -12.4568066), 'Tambacounda': (13.7692585, -13.6682901), 'Goudiry': (14.1814908, -12.7151588), 'Koumpentoum': (13.980418, -14.561125), 'Kaolack': (14.138815, -16.076391), 'Nioro du Rip': (13.745571, -15.774751), 'Guinguinéo': (14.272179, -15.945573), "Mbour": (14.411794, -16.9657124), 'Thiès': (14.791461, -16.925605), 'Tivaouane': (14.951507, -16.812868), 'Kébémer': (15.374006, -16.4497224), 'Linguère': (15.3954248, -15.1153121), 'Louga': (15.776878199999999, -16.061562227328675), 'Fatick': (14.333965, -16.404219), 'Foundiougne': (14.1263545, -16.4674807), 'Gossas': (14.491243, -16.064164), 'Kolda': (12.8921154, -14.9400971), 'Vélingara': (13.147235, -14.107583), 'Médina-Yorofoula': (13.2928356, -14.7146536), 'Kanel': (15.491026, -13.1756847), 'Matam': (15.656563, -13.255916), 'Ranérou': (15.2980838, -13.9623923), 'Kaffrine': (14.10197, -15.548433), 'Birkelane': (14.1282088, -15.7469433), 'Koungheul': (13.979578, -14.803538), 'Malem-Hodar': (14.0877914, -15.291912), 'Kédougou': (12.5570752, -12.1855655), 'Salémata': (12.6321326, -12.8178662), 'Saraya': (12.834249, -11.7549969), 'Sédhiou': (12.7099045, -15.557338), 'Bounkiling': (13.0408601, -15.6960536), 'Goudomp': (12.5729357, -15.8763382)}

        # Dictionary holding the population of each region in Togo
        regions_population = {
            'Kara': 985512,
            'Centrale': 795529,
            'Maritime': 1346615+2188376,
            'Plateaux': 1635946,
            'Savanes_Togo': 1143520
        }

        # Total population of Senegal
        population = 17738795

        # Total area (in km²) of Senegal
        area = 196722


        super().__init__(department_mapping, coordinates, population, area)  # Initialize the parent class


        # Dictionary holding the number of agencies based on the service type
        if service_type.lower() == 'bank':
            self.agency_counts = {'Dakar': 262, 'Mbacké': 23, 'Mbour': 23, 'Goudomp':0, 'Thiès': 20, 'Kaolack': 18, 'Saint Louis': 17, 'Ziguinchor': 14, 'Pikine': 12, 'Louga': 9, 'Kolda': 8, 'Tambacounda': 8, 'Rufisque': 9, 'Matam': 8, 'Dagana': 7, 'Bakel': 6, 'Fatick': 5, 'Diourbel': 6, 'Kédougou': 4, 'Thiaroye': 4, 'Tivaouane': 5, 'Kaffrine': 3, 'Bignona': 3, 'Kébémer': 2, 'Podor': 3, 'Sédhiou': 2, 'Guinguinéo': 1, 'Linguère': 2, 'Vélingara': 1, 'Guédiawaye': 0, 'Keur Massar': 0, 'Oussouye': 0, 'Bambey': 0, 'Goudiry': 0, 'Koumpentoum': 0, 'Nioro du Rip': 0, 'Foundiougne': 0, 'Gossas': 0, 'Médina-Yorofoula': 0, 'Kanel': 0, 'Ranérou': 0, 'Birkelane': 0, 'Koungheul': 0, 'Malem-Hodar': 0, 'Salémata': 0, 'Saraya': 0, 'Bounkiling': 0}
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
        return 0.558 * self.population   # 57% of the total population
