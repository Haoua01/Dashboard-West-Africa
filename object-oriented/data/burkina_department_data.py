from financial_service import FinancialService

class BurkinaDepartmentData(FinancialService):
    """Class to manage data specific to Côte d'Ivoire based on the type of financial service."""
    
    def __init__(self, service_type):
        
        # Dictionary holding the geographical coordinates of cities in Côte d'Ivoire
        coordinates = {'Balé': (11.658145000000001, -3.05410222166222), 'Banwa': (12.226556800000001, -4.191334410143565), 'Kossi': (12.959334649999999, -3.843679672896223), 'Mouhoun': (12.2367475, -3.3387562016398076), 'Nayala': (12.66018665, -2.989115317195795), 'Sourou': (13.2311675, -2.9621810439189185), 'Comoé': (10.24198965, -4.426887475215517), 'Léraba': (10.6520035, -5.2116858317609225), 'Kadiogo': (12.36732, -1.5430869129979032), 'Boulgou': (11.464625, -0.40891006975087923), 'Koulpélogo': (11.41531375, 0.1498990471870048), 'Kouritenga': (12.185035, -0.24484796351824084), 'Bam': (13.468115000000001, -1.5986636780329766), 'Namentenga': (13.23672, -0.48193425057372896), 'Sanmatenga': (13.24054485, -0.974702257138456), 'Boulkiemdé': (12.293712, -2.1041311868586234), 'Sanguié': (12.21015615, -2.642105900767874), 'Sissili': (11.4484064, -2.3912085167809947), 'Ziro': (11.675305, -1.9146625981460854), 'Bazèga': (11.8922276, -1.4593761927943558), 'Nahouri': (11.254511350000001, -1.2699820798913044), 'Zoundwéogo': (11.5525895, -1.0308937968749998), 'Gnagna': (12.91545745, -0.06595616042218595), 'Gourma': (12.22782665, 0.5472077927384438), 'Komondjari': (12.726911300000001, 0.7047082708628676), 'Kompienga': (11.44875915, 0.9770378186762776), 'Tapoa': (12.1450627, 1.7603025216478507), 'Houet': (11.3851056, -4.327364252199034), 'Kénédougou': (11.403998, -4.985102779774959), 'Tuy': (11.44956045, -3.378765326190213), 'Loroum': (13.9463767, -2.105539991379096), 'Passoré': (12.8777, -2.2944905358462657), 'Yatenga': (13.59429385, -2.524951256180203), 'Zondoma': (13.19753955, -2.30852755103427), 'Ganzourgou': (12.289915449999999, -0.8083428734589146), 'Kourwéogo': (12.6004222, -1.7598560868204798), 'Oubritenga': (12.597010000000001, -1.252231049186129), 'Oudalan': (14.6253063, -0.33334713188739373), 'Séno': (13.99508, -0.09920758226217463), 'Soum': (14.2861443, -1.345232631664196), 'Yagha': (13.426944500000001, 0.6161497146962224), 'Bougouriba': (10.882093300000001, -3.4306630906241278), 'Ioba': (11.0343187, -2.9627761001630786), 'Noumbiel': (9.796745300000001, -2.9265543286252163), 'Poni': (10.3085943, -3.3016811191930113)}        #department_mapping = {'Abidjan': 'Abidjan', 'San-Pédro': 'Bas-Sassandra', 'Tabou': 'Bas-Sassandra', 'Buyo': 'Bas-Sassandra', 'Guéyo': 'Bas-Sassandra', 'Méagui': 'Bas-Sassandra', 'Soubré': 'Bas-Sassandra', 'Fresco': 'Bas-Sassandra', 'Sassandra': 'Bas-Sassandra', 'Abengourou': 'Comoé', 'Agnibilékrou': 'Comoé', 'Bettié': 'Comoé', 'Aboisso': 'Comoé', 'Adiaké': 'Comoé', 'Grand-Bassam': 'Comoé', 'Tiapoum': 'Comoé', 'Gbéléban': 'District du Denguélé', 'Madinani': 'District du Denguélé', 'Odienné': 'District du Denguélé', 'Samatiguila': 'District du Denguélé', 'Séguélon': 'District du Denguélé', 'Kaniasso': 'District du Denguélé', 'Minignan': 'District du Denguélé', 'Gagnoa': 'Gôh-Djiboua', 'Oumé': 'Gôh-Djiboua', 'Divo': 'Gôh-Djiboua', 'Guitry': 'Gôh-Djiboua', 'Lakota': 'Gôh-Djiboua', 'Didiévi': 'Lacs', 'Djékanou': 'Lacs', 'Tiébissou': 'Lacs', 'Toumodi': 'Lacs', 'Daoukro': 'Lacs', 'M\'Bahiakro': 'Lacs', 'Ouellé': 'Lacs', 'Prikro': 'Lacs', 'Bocanda': 'Lacs', 'Dimbokro': 'Lacs', 'Kouassi-Kouassikro': 'Lacs', 'Arrah': 'Lacs', 'Bongouanou': 'Lacs', 'M\'Batto': 'Lacs', 'Grand-Lahou': 'Lagunes', 'Jacqueville': 'Lagunes', 'Agboville': 'Lagunes', 'Dabou': 'Lagunes', 'Sikensi': 'Lagunes', 'Taabo': 'Lagunes', 'Tiassalé': 'Lagunes', 'Adzopé': 'Lagunes', 'Akoupé': 'Lagunes', 'Alépé': 'Lagunes', 'Yakassé-Attobrou': 'Lagunes', 'Biankouma': 'Montagnes', 'Man': 'Montagnes', 'Danané': 'Montagnes', 'Bloléquin': 'Montagnes', 'Guiglo': 'Montagnes', 'Taï': 'Montagnes', 'Facobly': 'Montagnes', 'Sipilou': 'Montagnes', 'Toulépleu': 'Montagnes', 'Zouan-Hounien': 'Montagnes', 'Bangolo': 'Montagnes', 'Duékoué': 'Montagnes', 'Daloa': 'Sassandra-Marahoué', 'Issia': 'Sassandra-Marahoué', 'Vavoua': 'Sassandra-Marahoué', 'Zoukougbeu': 'Sassandra-Marahoué', 'Bonon': 'Sassandra-Marahoué', 'Bouaflé': 'Sassandra-Marahoué', 'Gohitafla': 'Sassandra-Marahoué', 'Sinfra': 'Sassandra-Marahoué', 'Zuénoula': 'Sassandra-Marahoué', 'Korhogo': 'Savanes_CIV', 'Ferkessédougou': 'Savanes_CIV', 'Sinématiali': 'Savanes_CIV', 'M\'Bengué': 'Savanes_CIV', 'Tengréla': 'Savanes_CIV', 'Boundiali': 'Savanes_CIV', 'Kouto': 'Savanes_CIV', 'Dikodougou': 'Savanes_CIV', 'Niakaramandougou': 'Savanes_CIV', 'Kong': 'Savanes_CIV', 'Ouangolodougou': 'Savanes_CIV', 'Béoumi': 'Vallée du Bandama', 'Botro': 'Vallée du Bandama', 'Bouaké': 'Vallée du Bandama', 'Katiola': 'Vallée du Bandama', 'Sakassou': 'Vallée du Bandama', 'Dabakala': 'Vallée du Bandama', 'Niakaramandougou': 'Vallée du Bandama', 'Kani': 'Woroba', 'Séguéla': 'Woroba', 'Dianra': 'Woroba', 'Mankono': 'Woroba', 'Koro': 'Woroba', 'Ouaninou': 'Woroba', 'Touba': 'Woroba', 'Yamoussoukro': 'Yamoussoukro', 'Attiégouakro': 'Yamoussoukro', 'Bondoukou': 'Zanzan', 'Koun-Fao': 'Zanzan', 'Sandégué': 'Zanzan', 'Tanda': 'Zanzan', 'Transua': 'Zanzan', 'Bouna': 'Zanzan', 'Doropo': 'Zanzan', 'Nassian': 'Zanzan', 'Téhini': 'Zanzan'}
        
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


        # Total population, 2021
        population = 21509443 

        # Total area (in km²) of Burkina Faso
        area = 274222

        super().__init__(department_mapping, coordinates, population, area)  # Initialize the parent class

        # Dictionary holding the number of agencies based on the service type
        if service_type.lower() == 'bank':
            self.agency_counts = {'Kadiogo': 139, 'Houet': 25, 'Boulgou': 16, 'Boulkiembé': 9, 'Yatenga': 9, 'Mouhoun': 8, 'Sanmatenga': 8, 'Kouritenga': 8, 'Comoé': 7, 'Boulkiemdé': 5, 'Tuy': 4, 'Séno': 4, 'Gourma': 3, 'Bougouriba': 3, 'Kénédougou': 3, 'Poni': 3, 'Zoudwéogo': 3, 'Balé': 3, 'Nahouri': 3, 'Passoré': 2, 'Sourou': 2, 'Ganzourgou': 2, 'Koulpélogo': 1, 'Sanguié': 1, 'Zoundwéogo': 1, 'Oubritenga': 1, 'Tapoa': 1, 'Gnagna': 1, 'Sissili': 1, 'Banwa': 1, 'Kossi': 1, 'Nayala': 0, 'Léraba': 0, 'Bam': 0, 'Namentenga': 0, 'Ziro': 0, 'Bazèga': 0, 'Komondjari': 0, 'Kompienga': 0, 'Loroum': 0, 'Zondoma': 0, 'Kourwéogo': 0, 'Oudalan': 0, 'Soum': 0, 'Yagha': 0, 'Ioba': 0, 'Noumbiel': 0}
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
        return 0.5414 * self.population # 54.14% of the total population
    