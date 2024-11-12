from financial_service import FinancialService

class CIVDepartmentData(FinancialService):
    """Class to manage data specific to Côte d'Ivoire based on the type of financial service."""
    
    def __init__(self, service_type):
        
        # Dictionary holding the geographical coordinates of cities in Côte d'Ivoire
        coordinates = {'Abidjan': (5.320357, -4.016107), 'Attiégouakro': (6.7760146, -5.1178031), 'Yamoussoukro': (6.8200066, -5.2776034), 'San-Pédro': (4.7589989, -6.6463922), 'Tabou': (4.4162799, -7.3559159), 'Buyo': (6.2507192, -7.0057256), 'Guéyo': (5.69117595, -6.139586651979171), 'Méagui': (5.4039253, -6.5551664), 'Soubré': (5.7850195, -6.5933223), 'Fresco': (5.14528285, -5.627871932754667), 'Sassandra': (4.9490007, -6.0921667), 'Abengourou': (6.7269042, -3.4968431), 'Agnibilékrou': (7.0648415, -3.3287147232087344), 'Bettié': (6.11447955, -3.3097383812321786), 'Aboisso': (5.712626, -3.2076104114485666), 'Adiaké': (5.231890249999999, -3.258247883103464), 'Grand-Bassam': (5.212884, -3.743226), 'Tiapoum': (5.257687000000001, -2.8536454090555075), 'Gbéléban': (9.583453, -8.1304389), 'Madinani': (9.6103848, -6.9430731), 'Odienné': (9.504431, -7.561942), 'Samatiguila': (9.818397, -7.561488), 'Séguélon': (9.3564345, -7.1196823), 'Kaniasso': (9.814673, -7.511101), 'Minignan': (9.9964793, -7.836692), 'Gagnoa': (6.1334787, -5.9510987), 'Oumé': (6.3823941, -5.4175714), 'Divo': (5.8405332, -5.3549049), 'Guitry': (5.50177835, -5.153368261942675), 'Lakota': (5.8511202, -5.6827839), 'Didiévi': (7.12866, -4.898041), 'Djékanou': (6.4695268, -5.1142493) , 'Tiébissou': (7.1580709, -5.2255722), 'Toumodi': (6.5602173, -5.0160877), 'Daoukro': (7.0579401, -3.9660686), 'M\'Bahiakro': (7.4572779, -4.341103947419997), 'Ouellé': (7.2964128, -4.0141563), 'Prikro': (7.6470835, -3.9973171), 'Bocanda': (7.063065, -4.4972477), 'Dimbokro': (6.6494254, -4.7040555), 'Kouassi-Kouassikro': (7.341414, -4.67709), 'Arrah': (6.6745413, -3.970127), 'Bongouanou': (6.6475288, -4.2046603), 'M\'Batto': (6.4695017, -4.3585668) , 'Dabou': (5.3239991, -4.3722982), 'Grand-Lahou': (5.2503434, -5.0024449), 'Jacqueville': (5.2076511, -4.4195117), 'Agboville': (5.9307328, -4.2131327), 'Sikensi': (5.64314725, -4.594765169351558), 'Taabo': (6.2668844, -5.0699787), 'Tiassalé': (5.8956463, -4.8250584), 'Adzopé': (6.1058336, -3.8640409), 'Akoupé': (6.3815237, -3.8859041), 'Alépé': (5.4966091, -3.6638901), 'Yakassé-Attobrou': (6.1824665, -3.6512284), 'Biankouma': (7.738348, -7.612799), 'Danané': (7.2631278, -8.1546282), 'Man': (7.4102584, -7.5503719), 'Sipilou': (7.8630249, -8.1033408), 'Zouan-Hounien': (6.9198246, -8.2089154), 'Bloléquin': (6.5705513, -8.003273), 'Guiglo': (6.43034025, -7.5909032112704775), 'Taï': (5.8756204, -7.4531292), 'Toulépleu': (6.580899, -8.4150175), 'Bangolo': (7.0119038, -7.4867606), 'Duékoué': (6.71397265, -7.425218155057541), 'Facobly': (7.3886375, -7.3761531), 'Kouibly': (7.256817, -7.235397), 'Daloa': (6.8869233, -6.4529859), 'Issia': (6.4877871, -6.5887859), 'Vavoua': (7.3793487, -6.4796624), 'Zoukougbeu': (6.762992, -6.864266), 'Bonon': (6.92692, -6.0442776), 'Bouaflé': (6.980181, -5.7458332), 'Gohitafla': (7.4905838, -5.8799547), 'Sinfra': (6.6167488, -5.9089494), 'Zuénoula': (7.4280208, -6.0500349), 'Dikodougou': (9.06757, -5.769772), 'Korhogo': (9.4580698, -5.6316293), "M\'Bengué": (10.0010816, -5.9007432), 'Sinématiali': (9.5840785, -5.3840301), 'Ferkessédougou': (9.5939778, -5.1975952), 'Kong': (9.148681, -4.610648), 'Ouangolodougou': (9.966279, -5.149917), 'Boundiali': (9.5232291, -6.4820197), 'Kouto': (9.8927311, -6.4127605), 'Tengréla': (10.4808337, -6.4084077), 'Béoumi': (7.6745381, -5.5827323), 'Botro': (7.8525444, -5.3103708), 'Bouaké': (7.6890212, -5.0283552), 'Sakassou': (7.4534806, -5.2923493), 'Dabakala': (8.363238, -4.428486), 'Katiola': (8.0912137, -5.150708249056292), 'Niakaramandougou': (8.6606903, -5.2894139), 'Kani': (8.4772526, -6.6032747), 'Séguéla': (7.9614107, -6.6702351), 'Dianra': (8.9525209, -6.2547072), 'Kounahiri': (7.7887394, -5.8352918), 'Mankono': (8.0448003, -6.074259236645267), 'Koro': (8.5536789, -7.4623837), 'Ouaninou': (8.23753, -7.867145), 'Touba': (8.2840981, -7.6818105), 'Bondoukou': (8.0397992, -2.7984258), 'Koun-Fao': (7.4879991, -3.2517544), 'Sandégué': (7.9555223, -3.5813579), 'Transua': (7.5495016, -3.0136612), 'Tanda': (7.803664, -3.1672478), 'Bouna': (9.2687219, -2.9989845), 'Doropo': (9.8095188, -3.3458764), 'Nassian': (8.4530536, -3.4707332), 'Téhini': (9.6067135, -3.6576767)}

        #department_mapping = {'Abidjan': 'Abidjan', 'San-Pédro': 'Bas-Sassandra', 'Tabou': 'Bas-Sassandra', 'Buyo': 'Bas-Sassandra', 'Guéyo': 'Bas-Sassandra', 'Méagui': 'Bas-Sassandra', 'Soubré': 'Bas-Sassandra', 'Fresco': 'Bas-Sassandra', 'Sassandra': 'Bas-Sassandra', 'Abengourou': 'Comoé', 'Agnibilékrou': 'Comoé', 'Bettié': 'Comoé', 'Aboisso': 'Comoé', 'Adiaké': 'Comoé', 'Grand-Bassam': 'Comoé', 'Tiapoum': 'Comoé', 'Gbéléban': 'District du Denguélé', 'Madinani': 'District du Denguélé', 'Odienné': 'District du Denguélé', 'Samatiguila': 'District du Denguélé', 'Séguélon': 'District du Denguélé', 'Kaniasso': 'District du Denguélé', 'Minignan': 'District du Denguélé', 'Gagnoa': 'Gôh-Djiboua', 'Oumé': 'Gôh-Djiboua', 'Divo': 'Gôh-Djiboua', 'Guitry': 'Gôh-Djiboua', 'Lakota': 'Gôh-Djiboua', 'Didiévi': 'Lacs', 'Djékanou': 'Lacs', 'Tiébissou': 'Lacs', 'Toumodi': 'Lacs', 'Daoukro': 'Lacs', 'M\'Bahiakro': 'Lacs', 'Ouellé': 'Lacs', 'Prikro': 'Lacs', 'Bocanda': 'Lacs', 'Dimbokro': 'Lacs', 'Kouassi-Kouassikro': 'Lacs', 'Arrah': 'Lacs', 'Bongouanou': 'Lacs', 'M\'Batto': 'Lacs', 'Grand-Lahou': 'Lagunes', 'Jacqueville': 'Lagunes', 'Agboville': 'Lagunes', 'Dabou': 'Lagunes', 'Sikensi': 'Lagunes', 'Taabo': 'Lagunes', 'Tiassalé': 'Lagunes', 'Adzopé': 'Lagunes', 'Akoupé': 'Lagunes', 'Alépé': 'Lagunes', 'Yakassé-Attobrou': 'Lagunes', 'Biankouma': 'Montagnes', 'Man': 'Montagnes', 'Danané': 'Montagnes', 'Bloléquin': 'Montagnes', 'Guiglo': 'Montagnes', 'Taï': 'Montagnes', 'Facobly': 'Montagnes', 'Sipilou': 'Montagnes', 'Toulépleu': 'Montagnes', 'Zouan-Hounien': 'Montagnes', 'Bangolo': 'Montagnes', 'Duékoué': 'Montagnes', 'Daloa': 'Sassandra-Marahoué', 'Issia': 'Sassandra-Marahoué', 'Vavoua': 'Sassandra-Marahoué', 'Zoukougbeu': 'Sassandra-Marahoué', 'Bonon': 'Sassandra-Marahoué', 'Bouaflé': 'Sassandra-Marahoué', 'Gohitafla': 'Sassandra-Marahoué', 'Sinfra': 'Sassandra-Marahoué', 'Zuénoula': 'Sassandra-Marahoué', 'Korhogo': 'Savanes_CIV', 'Ferkessédougou': 'Savanes_CIV', 'Sinématiali': 'Savanes_CIV', 'M\'Bengué': 'Savanes_CIV', 'Tengréla': 'Savanes_CIV', 'Boundiali': 'Savanes_CIV', 'Kouto': 'Savanes_CIV', 'Dikodougou': 'Savanes_CIV', 'Niakaramandougou': 'Savanes_CIV', 'Kong': 'Savanes_CIV', 'Ouangolodougou': 'Savanes_CIV', 'Béoumi': 'Vallée du Bandama', 'Botro': 'Vallée du Bandama', 'Bouaké': 'Vallée du Bandama', 'Katiola': 'Vallée du Bandama', 'Sakassou': 'Vallée du Bandama', 'Dabakala': 'Vallée du Bandama', 'Niakaramandougou': 'Vallée du Bandama', 'Kani': 'Woroba', 'Séguéla': 'Woroba', 'Dianra': 'Woroba', 'Mankono': 'Woroba', 'Koro': 'Woroba', 'Ouaninou': 'Woroba', 'Touba': 'Woroba', 'Yamoussoukro': 'Yamoussoukro', 'Attiégouakro': 'Yamoussoukro', 'Bondoukou': 'Zanzan', 'Koun-Fao': 'Zanzan', 'Sandégué': 'Zanzan', 'Tanda': 'Zanzan', 'Transua': 'Zanzan', 'Bouna': 'Zanzan', 'Doropo': 'Zanzan', 'Nassian': 'Zanzan', 'Téhini': 'Zanzan'}
        department_mapping = {
            'Abidjan': ['Abidjan'],
            'Bas-Sassandra': ['San-Pédro', 'Tabou', 'Buyo', 'Guéyo', 'Méagui', 'Soubré', 'Fresco', 'Sassandra'],
            'Comoé': ['Abengourou', 'Agnibilékrou', 'Bettié', 'Aboisso', 'Adiaké', 'Grand-Bassam', 'Tiapoum'],
            'District du Denguélé': ['Gbéléban', 'Madinani', 'Odienné', 'Samatiguila', 'Séguélon', 'Kaniasso', 'Minignan'],
            'Gôh-Djiboua': ['Gagnoa', 'Oumé', 'Divo', 'Guitry', 'Lakota'],
            'Lacs': ['Didiévi', 'Djékanou', 'Tiébissou', 'Toumodi', 'Daoukro', 'M\'Bahiakro', 'Ouellé', 'Prikro', 'Bocanda', 'Dimbokro', 'Kouassi-Kouassikro', 'Arrah', 'Bongouanou', 'M\'Batto'],
            'Lagunes': ['Grand-Lahou', 'Jacqueville', 'Agboville', 'Dabou', 'Sikensi', 'Taabo', 'Tiassalé', 'Adzopé', 'Akoupé', 'Alépé', 'Yakassé-Attobrou'],
            'Montagnes': ['Biankouma', 'Man', 'Danané', 'Bloléquin', 'Guiglo', 'Taï', 'Facobly', 'Sipilou', 'Toulépleu', 'Zouan-Hounien', 'Bangolo', 'Duékoué'],
            'Sassandra-Marahoué': ['Daloa', 'Issia', 'Vavoua', 'Zoukougbeu', 'Bonon', 'Bouaflé', 'Gohitafla', 'Sinfra', 'Zuénoula'],
            'Savanes_CIV': ['Korhogo', 'Ferkessédougou', 'Sinématiali', 'M\'Bengué', 'Tengréla', 'Boundiali', 'Kouto', 'Dikodougou', 'Niakaramandougou', 'Kong', 'Ouangolodougou'],
            'Vallée du Bandama': ['Béoumi', 'Botro', 'Bouaké', 'Katiola', 'Sakassou', 'Dabakala', 'Niakaramandougou'],
            'Woroba': ['Kani', 'Séguéla', 'Dianra', 'Kounahiri', 'Mankono', 'Koro', 'Ouaninou', 'Touba'],
            'Yamoussoukro': ['Yamoussoukro', 'Attiégouakro'],
            'Zanzan': ['Bondoukou', 'Koun-Fao', 'Sandégué', 'Tanda', 'Transua', 'Bouna', 'Doropo', 'Nassian', 'Téhini']
        }

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
            self.agency_counts = {'Abidjan': 390, 'San-Pédro': 19, 'Korhogo': 16, 'Bouaké': 15, 'Daloa': 13, 'Yamoussoukro': 10, 'Soubré': 9, 'Gagnoa': 8, 'Abengourou': 8, 'Grand-Bassam': 8, 'Divo': 6, 'Aboisso': 5, 'Man': 5, 'Duékoué': 5, 'Dabou': 3, 'Adzopé': 3, 'Ferkessédougou': 3, 'Boundiali': 3, 'Bondoukou': 3, 'Méagui': 2, 'Sassandra': 2, 'Agnibilékrou': 2, 'Odienné': 2, 'Oumé': 2, 'Daoukro': 2, 'Dimbokro': 2, 'Bongouanou': 2, 'Agboville': 2, 'Tiassalé': 2, 'Issia': 2, 'Bouaflé': 2, 'Katiola': 2, 'Séguéla': 2, 'Tiébissou': 1, 'Grand-Lahou': 1, 'Jacqueville': 1, 'Danané': 1, 'Bloléquin': 1, 'Guiglo': 1, 'Bonon': 1, 'Sinfra': 1, 'Ouangolodougou': 1, 'Touba': 1, 'Toumodi': 1, 'Adiaké': 1, 'Mankono': 1, 'Tabou': 1, 'Attiégouakro': 0, 'Buyo': 0, 'Guéyo': 0, 'Fresco': 0, 'Bettié': 0, 'Tiapoum': 0, 'Gbéléban': 0, 'Madinani': 0, 'Samatiguila': 0, 'Séguélon': 0, 'Kaniasso': 0, 'Minignan': 0, 'Guitry': 0, 'Lakota': 0, 'Didiévi': 0, 'Djékanou': 0, 'M\'Bahiakro': 0, 'Ouellé': 0, 'Prikro': 0, 'Bocanda': 0, 'Kouassi-Kouassikro': 0, 'Arrah': 0, "M\'Batto": 0, 'Sikensi': 0, 'Taabo': 0, 'Akoupé': 0, 'Alépé': 0, 'Yakassé-Attobrou': 0, 'Biankouma': 0, 'Sipilou': 0, 'Zouan-Hounien': 0, 'Taï': 0, 'Toulépleu': 0, 'Bangolo': 0, 'Facobly': 0, 'Kouibly': 0, 'Vavoua': 0, 'Zoukougbeu': 0, 'Gohitafla': 0, 'Zuénoula': 0, 'Dikodougou': 0, "M\'Bengué": 0, 'Sinématiali': 0, 'Kong': 0, 'Kouto': 0, 'Tengréla': 0, 'Béoumi': 0, 'Botro': 0, 'Sakassou': 0, 'Dabakala': 0, 'Niakaramandougou': 0, 'Kani': 0, 'Dianra': 0, 'Kounahiri': 0, 'Koro': 0, 'Ouaninou': 0, 'Koun-Fao': 0, 'Sandégué': 0, 'Transua': 0, 'Tanda': 0, 'Bouna': 0, 'Doropo': 0, 'Nassian': 0, 'Téhini': 0, 'M\'Bahiakro':0}
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
    
    def get_adult_population(self):
        """Calculates and returns the population over 15 years old for the regions."""
        return {region: 0.57 * pop for region, pop in self.population.items()}  # 57% of the total population

    