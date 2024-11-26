from financial_service import FinancialService

class MaliData(FinancialService):
    """Class to manage data specific to Côte d'Ivoire based on the type of financial service."""
    
    def __init__(self, service_type):
        
        department_mapping = {
            'Kayes': ['Bafoulabé', 'Diéma', 'Kayes', 'Kéniéba', 'Kita', 'Nioro', 'Yélimané'],
            'Koulikoro': ['Banamba', 'Dioila', 'Kangaba', 'Kati', 'Kolokani', 'Koulikoro', 'Nara'],
            'Sikasso': ['Bougouni', 'Kadiolo', 'Kolondieba', 'Koutiala', 'Sikasso', 'Yanfolila', 'Yorosso'],
            'Ségou': ['Baraouéli', 'Bla', 'Macina', 'Niono', 'San', 'Ségou', 'Tominian'],
            'Mopti': ['Bandiagara', 'Bankass', 'Djenné', 'Douentza', 'Koro', 'Mopti', 'Ténenkou', 'Youwarou'],
            'Tombouctou': ['Diré', 'Goundam', 'Gourma-Rharous', 'Niafunké', 'Tombouctou'],
            'Gao': ['Ansongo', 'Bourem', 'Gao'],
            'Kidal': ['Abeibara', 'Kidal', 'Tessalit', 'Tin-Essako'],
            'Bamako': ['Bamako'],
            'Menaka': ['Ménaka', 'Anderamboukane', 'Inekar', 'Tidermene']
        }

        # Dictionary holding the geographical coordinates of each city in Côte d'Ivoire
        #coordinates = GeographicData.get_department_coordinates(department_mapping, 'Mali')
        #print(coordinates)
        coordinates = {'Bafoulabé': (13.6785, -10.724738095238095), 'Diéma': (14.654499999999999, -9.256088755707761), 'Kayes': (14.443406, -11.437914), 'Kéniéba': (12.795450500000001, -11.044997099718604), 'Kita': (13.20698005, -9.388645713571428), 'Nioro': (15.2304528, -9.5899063), 'Yélimané': (15.033999999999999, -10.641903453136011), 'Banamba': (13.5485166, -7.446532), 'Dioila': (12.4863792, -6.7948799), 'Kangaba': (11.9415411, -8.4138589), 'Kati': (12.7389091, -8.0684052), 'Kolokani': (13.577326, -8.031273), 'Koulikoro': (12.8646318, -7.5561287), 'Nara': (15.1712509, -7.2888666), 'Bougouni': (11.4194313, -7.4833878), 'Kadiolo': (10.5540365, -5.7592858), 'Kolondieba': (11.0884592, -6.8930677), 'Koutiala': (12.3894818, -5.4639199), 'Sikasso': (11.3165531, -5.6777526), 'Yanfolila': (11.174901, -8.152292), 'Yorosso': (12.3524881, -4.7768451), 'Baraouéli': (13.039258400000001, -6.638869299766208), 'Bla': (12.949364, -5.7620576), 'Macina': (13.962189, -5.3594898), 'Niono': (14.2515119, -5.9783506), 'San': (13.3043073, -4.8957273), 'Ségou': (13.441518, -6.268147), 'Tominian': (13.2868042, -4.5902405), 'Bandiagara': (14.3505, -3.6112766), 'Bankass': (14.0786136, -3.5187494), 'Djenné': (13.9051631, -4.5548581), 'Douentza': (15.0068749, -2.9529649), 'Koro': (14.069845, -3.080698), 'Mopti': (14.4877275, -4.1892469), 'Ténenkou': (14.4547633, -4.9164995), 'Youwarou': (15.3706088, -4.2615466), 'Diré': (16.2678091, -3.3971368), 'Goundam': (16.4168533, -3.6636275), 'Gourma-Rharous': (16.8776652, -1.925352), 'Niafunké': (15.931, -3.99), 'Tombouctou': (16.7719091, -3.0087272), 'Ansongo': (15.6639257, 0.5067841), 'Bourem': (16.9575282, -0.3468008), 'Gao': (16.2788129, -0.0412392), 'Abeibara': (19.3494891, 1.8443903), 'Kidal': (18.4408358, 1.4075395), 'Tessalit': (20.2019542, 1.0124531), 'Tin-Essako': (18.4509602, 2.4897883), 'Bamako': (12.61326555, -7.984739136241295), 'Ménaka': (15.9167, 2.4), 'Anderamboukane': (15.4220566, 3.0224703), 'Inekar': (15.9486791, 3.1572826), 'Tidermene': (16.5923464, 2.415028)}

        # Total population of Mali, 2022
        population = 22395489

        # Total area (in km²) of Mali
        area = 1241238

        super().__init__(department_mapping, coordinates, population, area)  # Initialize the parent class

        # Dictionary holding the number of agencies based on the service type
        if service_type.lower() == 'bank':
            self.agency_counts = {'Bamako': 168, 'Sikasso': 18, 'Kayes': 18, 'Mopti': 17, 'Ségou': 15, 'Koutiala': 11, 'Koulikoro': 8, 'Gao': 5, 'Niono': 5, 'Bougouni': 4, 'Kéniéba': 4, 'Kati': 4, 'San': 4, 'Tombouctou': 3, 'Yanfolila': 3, 'Dioila': 3, 'Kadiolo': 3, 'Kita': 3, 'Douentza': 2, 'Bandiagara': 2, 'Nioro': 2, 'Bafoulabé': 2, 'Bla': 2, 'Sévaré': 1, 'Diéma': 1, 'Djenné': 1, 'Nara': 1, 'Bafoulabe': 1, 'Banamba': 1, 'Baraouéli': 1, 'Kolondieba': 1, 'Tabakoto': 1, 'Kidal': 1, 'Koro': 1, 'Bankass': 1, 'Tominian': 1, 'Yorosso': 1, 'Yélimané': 0, 'Kangaba': 0, 'Kolokani': 0, 'Macina': 0, 'Ténenkou': 0, 'Youwarou': 0, 'Diré': 0, 'Goundam': 0, 'Gourma-Rharous': 0, 'Niafunké': 0, 'Ansongo': 0, 'Bourem': 0, 'Abeibara': 0, 'Tessalit': 0, 'Tin-Essako': 0, 'Ménaka': 0, 'Anderamboukane': 0, 'Inekar': 0, 'Tidermene': 0}
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
    
    def get_coordinates(self):
        """Returns the geographical coordinates for cities in Benin."""
        return self.coordinates
    
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
        return 0.5069 * self.population  # 50.69% of the total population
    