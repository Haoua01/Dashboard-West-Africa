from financial_service import FinancialService

class TchadDepartmentData(FinancialService):
    """ Class to manage data specific to Togo based on the type of financial service. """
    
    def __init__(self, service_type):
        # Dictionary mapping regions to their respective departments
        department_mapping = {
            'Barh-El-Gazel': ['Barh-El-Gazel Sud', 'Barh-El-Gazel Ouest', 'Barh-El-Gazel Nord'], 
            'Batha': ['Batha Ouest', 'Batha Est', 'Fitri'], 
            'Borkou': ['Borkou', 'Borkou Yala'], 
            'Chari-Baguirmi': ['Baguirmi', 'Chari', 'Loug-Chari'], 
            'Ennedi Est': ['Am-Djarass', 'Wadi Hawar'], 
            'Ennedi Ouest': ['Fada', 'Mourtcha'], 
            'Guéra': ['Guéra', 'Abtouyour', 'Barh-Signaka', 'Mangalmé'], 
            'Hadjer-Lamis': ['Dagana', 'Dababa', 'Haraze-Al-Biar'], 
            'Kanem': ['Kanem', 'Nord Kanem', 'Wadi Bissam'], 
            'Lac': ['Mamdi', 'Wayi', 'Fouli', 'Kaya'], 
            'Logone Occidental': ['Lac Wey', 'Dodjé', 'Guéni', 'Ngourkosso'], 
            'Logone Oriental': ['La Pendé', 'Kouh Est', 'Kouh Ouest', 'La Nya', 'La Nya Pendé', 'Monts de Lam'], 
            'Mandoul': ['Mandoul Oriental', 'Barh-Sara', 'Mandoul Occidental'], 
            'Mayo-Kebbi Est': ['Mayo-Boneye', 'Kabbia', 'Mayo-Lemié', 'Mont Illi'], 
            'Mayo-Kebbi Ouest': ['Lac Léré', 'Mayo-Binder', 'Mayo-Dallah'], 
            'Moyen-Chari': ['Grande Sido', 'Lac Iro', 'Bahr-Köh'], 
            "N'Djamena": ["N'Djaména"], 
            'Ouaddaï': ['Ouara', 'Abdi', 'Assoungha'], 
            'Salamat': ['Bahr-Azoum', 'Aboudéia', 'Haraze-Mangueigne'], 
            'Sila': ['Kimiti', 'Djourf Al Ahmar'], 
            'Tandjilé': ['Tandjilé Est', 'Tandjile Ouest', 'Tandjilé Centre'], 
            'Tibesti': ['Tibesti Est', 'Tibesti Ouest'], 
            'Wadi Fira': ['Biltine', 'Dar-Tama', 'Kobé', 'Mégri']
        }
        
        # Dictionary holding the geographical coordinates of cities in Togo
        coordinates = {'Fitri': (12.77458195, 17.563197244643096), 'Borkou': (18.0, 19.0), 'Baguirmi': (10.5445, 16.8299), 'Chari': (11.0, 17.0), 'Am-Djarass': (16.0662879, 22.8350448), 'Fada': (17.1930577, 21.5813259), 'Guéra': (11.5, 18.5), 'Mangalmé': (12.365648, 19.615227), 'Dagana': (12.996486, 15.7349101), 'Kanem': (13.7106674, 15.8608182), 'Nord Kanem': (14.1227992, 15.3132737), 'Mamdi': (13.4846395, 14.6961484), 'Fouli': (13.841006, 14.5077844), 'Kaya': (13.5588115, 14.8399752), 'Guéni': (8.9984333, 15.9327833), 'La Pendé': (7.9261587, 16.6318788), 'La Nya': (7.9261587, 16.6318788), 'La Nya Pendé': (7.9261587, 16.6318788), 'Mandoul Oriental': (8.9052311, 17.5689986), 'Kabbia': (9.568095694911777, 15.529101769491337), 'Lac Léré': (9.657125, 14.288347982591059), 'Mayo-Binder': (9.632630664856284, 14.071896462905737), 'Grande Sido': (8.350634186332458, 18.871713258967212), 'Lac Iro': (10.10935935, 19.429807226255473), "N'Djaména": (12.1053232, 15.0468872), 'Ouara': (14.235364, 20.673905), 'Abdi': (12.8081572, 21.3044437), 'Bahr-Azoum': (10.9481, 20.2924), 'Aboudéia': (11.4506235, 19.2776144), 'Haraze-Mangueigne': (9.916667, 20.8), 'Tandjilé Est': (9.589357288895837, 15.876245137332967), 'Biltine': (14.525174, 20.928701), 'Kobé': (15.3168067, 22.1689525), "Barh-El-Gazel Sud": (14.8397, 17.2067), "Barh-El-Gazel Ouest": (13.6422, 16.4911)}

        # Total population of Togo, 2023
        population = 8095498

        # Total area (in km²) of Togo
        area = 56790

        super().__init__(department_mapping, coordinates, population, area)  # Initialize the parent class


        # Dictionary holding the number of agencies based on the service type
        if service_type.lower() == 'bank':
            self.agency_counts = {"N'Djaména": 42, 'Ouara': 6, 'Lac Wey': 6, 'Bahr-Köh': 3, 'Mayo-Dallah': 2, 'Guéra': 2, 'La Pendé': 2, 'Bahr-Azoum': 1, 'Mayo-Boneye': 1, 'Biltine': 1, 'Mamdi': 1, 'Kanem': 1}
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
        return 0.5718 * self.population  # 57.18% of the total population
