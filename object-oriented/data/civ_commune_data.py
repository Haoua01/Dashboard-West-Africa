from financial_service import FinancialService
from shapefile import Shapefile


class CIVCommuneData(FinancialService):
    """Class to manage data specific to Côte d'Ivoire based on the type of financial service."""

    
    def __init__(self, service_type, shp):
        
        # Dictionary holding the geographical coordinates of cities in Côte d'Ivoire
        coordinates = shp.get_commune_coordinates()

        #department_mapping = {'Abidjan': 'Abidjan', 'San-Pédro': 'Bas-Sassandra', 'Tabou': 'Bas-Sassandra', 'Buyo': 'Bas-Sassandra', 'Guéyo': 'Bas-Sassandra', 'Méagui': 'Bas-Sassandra', 'Soubré': 'Bas-Sassandra', 'Fresco': 'Bas-Sassandra', 'Sassandra': 'Bas-Sassandra', 'Abengourou': 'Comoé', 'Agnibilékrou': 'Comoé', 'Bettié': 'Comoé', 'Aboisso': 'Comoé', 'Adiaké': 'Comoé', 'Grand-Bassam': 'Comoé', 'Tiapoum': 'Comoé', 'Gbéléban': 'District du Denguélé', 'Madinani': 'District du Denguélé', 'Odienné': 'District du Denguélé', 'Samatiguila': 'District du Denguélé', 'Séguélon': 'District du Denguélé', 'Kaniasso': 'District du Denguélé', 'Minignan': 'District du Denguélé', 'Gagnoa': 'Gôh-Djiboua', 'Oumé': 'Gôh-Djiboua', 'Divo': 'Gôh-Djiboua', 'Guitry': 'Gôh-Djiboua', 'Lakota': 'Gôh-Djiboua', 'Didiévi': 'Lacs', 'Djékanou': 'Lacs', 'Tiébissou': 'Lacs', 'Toumodi': 'Lacs', 'Daoukro': 'Lacs', 'M\'Bahiakro': 'Lacs', 'Ouellé': 'Lacs', 'Prikro': 'Lacs', 'Bocanda': 'Lacs', 'Dimbokro': 'Lacs', 'Kouassi-Kouassikro': 'Lacs', 'Arrah': 'Lacs', 'Bongouanou': 'Lacs', 'M\'Batto': 'Lacs', 'Grand-Lahou': 'Lagunes', 'Jacqueville': 'Lagunes', 'Agboville': 'Lagunes', 'Dabou': 'Lagunes', 'Sikensi': 'Lagunes', 'Taabo': 'Lagunes', 'Tiassalé': 'Lagunes', 'Adzopé': 'Lagunes', 'Akoupé': 'Lagunes', 'Alépé': 'Lagunes', 'Yakassé-Attobrou': 'Lagunes', 'Biankouma': 'Montagnes', 'Man': 'Montagnes', 'Danané': 'Montagnes', 'Bloléquin': 'Montagnes', 'Guiglo': 'Montagnes', 'Taï': 'Montagnes', 'Facobly': 'Montagnes', 'Sipilou': 'Montagnes', 'Toulépleu': 'Montagnes', 'Zouan-Hounien': 'Montagnes', 'Bangolo': 'Montagnes', 'Duékoué': 'Montagnes', 'Daloa': 'Sassandra-Marahoué', 'Issia': 'Sassandra-Marahoué', 'Vavoua': 'Sassandra-Marahoué', 'Zoukougbeu': 'Sassandra-Marahoué', 'Bonon': 'Sassandra-Marahoué', 'Bouaflé': 'Sassandra-Marahoué', 'Gohitafla': 'Sassandra-Marahoué', 'Sinfra': 'Sassandra-Marahoué', 'Zuénoula': 'Sassandra-Marahoué', 'Korhogo': 'Savanes_CIV', 'Ferkessédougou': 'Savanes_CIV', 'Sinématiali': 'Savanes_CIV', 'M\'Bengué': 'Savanes_CIV', 'Tengréla': 'Savanes_CIV', 'Boundiali': 'Savanes_CIV', 'Kouto': 'Savanes_CIV', 'Dikodougou': 'Savanes_CIV', 'Niakaramandougou': 'Savanes_CIV', 'Kong': 'Savanes_CIV', 'Ouangolodougou': 'Savanes_CIV', 'Béoumi': 'Vallée du Bandama', 'Botro': 'Vallée du Bandama', 'Bouaké': 'Vallée du Bandama', 'Katiola': 'Vallée du Bandama', 'Sakassou': 'Vallée du Bandama', 'Dabakala': 'Vallée du Bandama', 'Niakaramandougou': 'Vallée du Bandama', 'Kani': 'Woroba', 'Séguéla': 'Woroba', 'Dianra': 'Woroba', 'Mankono': 'Woroba', 'Koro': 'Woroba', 'Ouaninou': 'Woroba', 'Touba': 'Woroba', 'Yamoussoukro': 'Yamoussoukro', 'Attiégouakro': 'Yamoussoukro', 'Bondoukou': 'Zanzan', 'Koun-Fao': 'Zanzan', 'Sandégué': 'Zanzan', 'Tanda': 'Zanzan', 'Transua': 'Zanzan', 'Bouna': 'Zanzan', 'Doropo': 'Zanzan', 'Nassian': 'Zanzan', 'Téhini': 'Zanzan'}
        department_mapping = shp.get_department_mapping()

        # Total population of Côte d'Ivoire, 2021
        population = 29389150

        # Total area (in km²) of Côte d'Ivoire
        area = 322462

        super().__init__(department_mapping, coordinates, population, area)  # Initialize the parent class

        # Dictionary holding the number of agencies based on the service type
        if service_type.lower() == 'bank':
            self.agency_counts = shp.get_agency_counts_in_commune()
        elif service_type.lower() == 'atm':
            self.agency_counts = shp.get_agency_counts_in_commune()
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
        return 0.5647 * self.population   # 56.47% of the total population

    