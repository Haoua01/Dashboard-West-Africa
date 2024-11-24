from financial_service import FinancialService

class GuineeDepartmentData(FinancialService):
    """ Class to manage data specific to Togo based on the type of financial service. """
    
    def __init__(self, service_type):
        # Dictionary mapping regions to their respective departments
        department_mapping = {
            'Bafata': ['Bafata', 'Bambadinca', 'Contuboel', 'Galomaro', 'Gamamundo', 'Xitole'],
            'Bolama': ['Bolama', 'Bubaque', 'Caravela', 'Uno'],
            'Cacheu': ['Bigene', 'Bula', 'Cacheu', 'Caió', 'Canchungo', 'Sao Domingos'],
            'Oio': ['Bissorã', 'Farim', 'Mansaba', 'Mansôa', 'Nhacra'],
            'Quinara': ['Buba', 'Empada', 'Fulacunda', 'Tite'],
            'Tombali': ['Bedanda', 'Cacine', 'Catió', 'Komo', 'Quebo'],
            'Bissau': ['Bissau'],
            'Gabu': ['Boé', 'Gabú', 'Pitche', 'Pirada', 'Sonaco'],
            'Biombo': ['Prábis', 'Quinhámel', 'Safim']
        }


        # Dictionary holding the geographical coordinates of cities in Togo
        coordinates = {'Bafata': (12.1723403, -14.6555027), 'Bambadinca': (12.023539, -14.860555), 'Contuboel': (12.3755089, -14.5603502), 'Galomaro': (11.9529086, -14.6371254), 'Gamamundo':(12.27132, -14.72651), 'Xitole': (11.7349442, -14.8144697), 'Bolama': (11.57763, -15.475261), 'Bubaque': (11.3000802, -15.8312425), 'Caravela': (11.53941045, -16.329990159596093), 'Uno': (11.2459664, -16.16341), 'Bigene': (12.439277, -15.535395), 'Bula': (12.108565, -15.711007), 'Cacheu': (12.274246, -16.1648911), 'Caió': (11.930685, -16.20014), 'Canchungo': (12.066422, -16.031912), 'Sao Domingos': (12.402654, -16.196593), 'Bissorã': (12.2235221, -15.4507416), 'Farim': (12.4823646, -15.2196439), 'Mansaba': (12.293782, -15.171311), 'Mansôa': (12.06661, -15.316344), 'Nhacra': (11.9589273, -15.5378614), 'Buba': (11.591979, -14.994788), 'Empada': (11.541162, -15.227461), 'Fulacunda': (11.774895, -15.1720999), 'Tite': (11.780287, -15.399514), 'Bedanda': (11.348427, -15.112394), 'Cacine': (11.12915, -15.02007), 'Catió': (11.2835568, -15.2547152), 'Komo': (11.1964101, -15.3335452), 'Quebo': (11.5388759, -14.7678444), 'Bissau': (11.861324, -15.583055), 'Boé': (11.747412, -14.210941), 'Gabú': (12.2819517, -14.2260818), 'Pitche': (12.326137, -13.954994), 'Pirada': (12.663468, -14.15473), 'Sonaco': (12.3951689, -14.4838361), 'Prábis': (11.8005341, -15.7401575), 'Quinhámel': (11.894183, -15.851309), 'Safim': (11.931923, -15.615397)}
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
            self.agency_counts = {'Bissau': 21, 'Bafata': 4, 'Gabú': 4, 'Buba': 2, 'Canchungo': 2, 'Bandim': 2, 'Bantandjam': 1, 'Sao Domingos ': 1, 'Safim': 1, 'Cacheu': 1, 'Bambadinca': 0, 'Contuboel': 0, 'Galomaro': 0, 'Gamamundo': 0, 'Xitole': 0, 'Bolama': 0, 'Bubaque': 0, 'Caravela': 0, 'Uno': 0, 'Bigene': 0, 'Bula': 0, 'Caió': 0, 'Sao Domingos': 0, 'Boé': 0, 'Pitche': 0, 'Pirada': 0, 'Sonaco': 0, 'Bissorã': 0, 'Farim': 0, 'Mansaba': 0, 'Mansôa': 0, 'Nhacra': 0, 'Empada': 0, 'Fulacunda': 0, 'Tite': 0, 'Bedanda': 0, 'Cacine': 0, 'Catió': 0, 'Komo': 0, 'Quebo': 0, 'Prábis': 0, 'Quinhámel': 0}
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
