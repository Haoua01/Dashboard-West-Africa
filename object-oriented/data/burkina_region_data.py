from financial_service import FinancialService
from geographic_data import GeographicData

class BurkinaBisData(FinancialService):
    """Class to manage data specific to Côte d'Ivoire based on the type of financial service."""
    
    def __init__(self, service_type):
        
        # Dictionary holding the geographical coordinates of cities in Côte d'Ivoire

        department_mapping = {
            "Boucle du Mouhoun": ["Balé", "Banwa", "Kossi", "Mouhoun", "Nayala", "Sourou"],
            "Cascades": ["Comoé", "Léraba"],
            "Centre": ["Kadiogo"],
            "Centre-Est": ["Boulgou", "Koulpélogo", "Kouritenga"],
            "Centre-Nord": ["Bam", "Namentenga", "Sanmatenga"],
            "Centre-Ouest": ["Boulkiemdé", "Sanguié", "Sissili", "Ziro"],
            "Centre-Sud": ["Bazèga", "Nahouri", "Zoundwéogo"],
            "Est": ["Gnagna", "Gourma", "Komondjari", "Kompienga", "Tapoa"],
            "Hauts-Bassins": ["Houet", "Kénédougou", "Tuy"],
            "Nord": ["Loroum", "Passoré", "Yatenga", "Zondoma"],
            "Plateau-Central": ["Ganzourgou", "Kourwéogo", "Oubritenga"],
            "Sahel": ["Oudalan", "Séno", "Soum", "Yagha"],
            "Sud-Ouest": ["Bougouriba", "Ioba", "Noumbiel", "Poni"]
        }

        coordinates = GeographicData.get_coordinates(department_mapping, 'Burkina Faso')

        # Dictionary holding the population of each cities in Côte d'Ivoire, 2021
        population = {'Abidjan': 6321017, 'San-Pédro': 790242, 'Korhogo': 748393, 'Bouaké': 931851, 'Daloa': 705378, 'Yamoussoukro': 372559, 'Soubré': 587441, 'Gagnoa': 724496, 'Abengourou': 430539, 'Grand-Bassam': 267103, 'Divo': 571688, 'Aboisso': 361842, 'Man': 461135, 'Duékoué': 420911, 'Dabou': 213582, 'Adzopé': 283727, 'Ferkessédougou': 190141, 'Boundiali': 198541, 'Bondoukou': 453841, 'Méagui': 299251, 'Sassandra': 353228, 'Agnibilékrou': 216264, 'Odienné': 156730, 'Oumé': 260786, 'Daoukro': 148095, 'Dimbokro': 102192, 'Bongouanou': 193158, 'Agboville': 384340, 'Tiassalé': 278954, 'Issia': 410628, 'Bouaflé': 300305, 'Katiola': 162472, 'Séguéla': 298384, 'Tiébissou': 116321, 'Grand-Lahou': 155832, 'Jacqueville': 80593, 'Danané': 364012, 'Bloléquin': 237944, 'Guiglo': 259381, 'Bonon': 167397, 'Sinfra': 245226, 'Ouangolodougou': 294639, 'Touba': 120524, 'Toumodi': 168363, 'Adiaké': 88006, 'Mankono': 271894, 'Tabou': 270482, 'Attiégouakro': 49513, 'Buyo': 176568, 'Guéyo': 102213, 'Fresco': 107752, 'Bettié': 69640, 'Tiapoum': 67941, 'Gbéléban': 29532, 'Madinani': 50248, 'Samatiguila': 19710, 'Séguélon': 33585, 'Kaniasso': 84572, 'Minignan': 61637, 'Guitry': 197236, 'Lakota': 334235, 'Didiévi': 93629, 'Djékanou': 37281, 'M\'Bahiakro': 78369, 'Ouellé': 56501, 'Prikro': 95595, 'Bocanda': 121469, 'Kouassi-Kouassikro': 30962, 'Arrah': 103846, "M\'Batto": 142750, 'Sikensi': 125897, 'Taabo': 76761, 'Akoupé': 156698, 'Alépé': 180253, 'Yakassé-Attobrou': 105986, 'Biankouma': 238714, 'Sipilou': 73109, 'Zouan-Hounien': 250938, 'Taï': 117387, 'Toulépleu': 93529, 'Bangolo': 270629, 'Facobly': 94610, 'Kouibly': 144723, 'Vavoua': 477154, 'Zoukougbeu': 146537, 'Gohitafla': 83370, 'Zuénoula': 184882, 'Dikodougou': 102115, "M\'Bengué": 114971, 'Sinématiali': 74981, 'Kong': 118304, 'Kouto': 175587, 'Tengréla': 141761, 'Béoumi': 195015, 'Botro': 117924, 'Sakassou': 108110, 'Dabakala': 254430, 'Niakaramandougou': 195127, 'Kani': 131428, 'Dianra': 119146, 'Kounahiri': 101111, 'Koro': 76345, 'Ouaninou': 65981, 'Koun-Fao': 167881, 'Sandégué': 69742, 'Transua': 112842, 'Tanda': 113523, 'Bouna': 178081, 'Doropo': 93386, 'Nassian': 71724, 'Téhini': 83846}
        

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
            self.agency_counts ={
                'Boucle du Mouhoun': 44,
                'Cascades': 12,
                'Centre': 139,
                'Centre-Est': 33,
                'Centre-Nord': 25,
                'Centre-Ouest': 15,
                'Centre-Sud': 9,
                'Est': 5,
                'Hauts-Bassins': 33,
                'Nord': 12,
                'Plateau-Central': 3,
                'Sahel': 4,
                'Sud-Ouest': 7
            }
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
    
    def get_adult_population(self):
        """Calculates and returns the population over 15 years old for the regions."""
        return {region: 0.57 * pop for region, pop in self.population.items()}  # 57% of the total population

    