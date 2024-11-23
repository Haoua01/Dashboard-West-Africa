from financial_service import FinancialService

class BeninDepartmentData(FinancialService):
    """
    Class to manage data specific to Benin based on the type of financial service.

    Attributes:
        service_type (str): The type of financial service (e.g., 'bank', 'mobile_money', 'microfinance').
        agency_counts (dict): A dictionary containing the number of agencies per territory based on the service type.
        department_mapping (dict): A dictionary mapping regions to their respective departments.
        coordinates (dict): A dictionary containing the geographical coordinates of territories in Benin.
        
    Methods:
        get_agency_counts(): Returns the agency counts for the specified service type.
        get_department_mapping(): Returns the department mapping for regions in Benin.
        get_coordinates(): Returns the geographical coordinates for cities in Benin.
    """
    
    def __init__(self, service_type):
        # Dictionary mapping regions to their respective departments
        department_mapping = {
            "Alibori": ["Banikoara", "Gogounou", "Kandi", "Karimama", "Malanville", "Segbana"],
            "Atakora": ["Boukoumbé", "Cobly", "Kérou", "Kouandé", "Matéri", "Natitingou", "Péhunco", "Tanguiéta", "Toucountouna"],
            "Atlantique": ["Abomey-Calavi", "Allada", "Kpomassè", "Ouidah", "Sô-Ava", "Toffo", "Tori-Bossito", "Zè"],
            "Borgou": ["Bembéréké", "Kalalé", "N'Dali", "Nikki", "Parakou", "Pèrèrè", "Sinendé", "Tchaourou"],
            "Collines": ["Bantè", "Dassa-Zoumé", "Glazoué", "Ouèssè", "Savalou", "Savè"],
            "Donga": ["Bassila", "Copargo", "Djougou", "Ouaké"],
            "Couffo": ["Aplahoué", "Djakotomey", "Dogbo-Tota", "Klouékanmè", "Lalo", "Toviklin"],
            "Littoral": ["Cotonou"],
            "Mono": ["Athiémé", "Bopa", "Comè", "Grand-Popo", "Houéyogbé", "Lokossa"],
            "Ouémé": ["Adjarra", "Adjohoun", "Aguégués", "Akpro-Missérété", "Avrankou", "Bonou", "Dangbo", "Porto-Novo", "Sèmè-Kpodji"],
            "Plateau": ["Adja-Ouèrè", "Ifangni", "Kétou", "Pobè", "Sakété"],
            "Zou": ["Abomey", "Agbangnizoun", "Bohicon", "Covè", "Djidja", "Ouinhi", "Za-Kpota", "Zagnanado", "Zogbodomey"]
        }
        
        # Dictionary holding the geographical coordinates of cities in Benin
        coordinates = {'Banikoara': (11.32625415, 2.473040680223342), 'Gogounou': (10.8522725, 2.7290948000000004), 'Kandi': (11.1311029, 2.9322321), 'Karimama': (11.91622705, 2.7121422370930746), 'Malanville': (11.8618128, 3.3862982), 'Segbana': (10.9762375, 3.5053446821212226), 'Boukoumbé': (10.1832167, 1.1000529), 'Cobly': (10.479186200000001, 0.936429736261758), 'Kérou': (10.8263035, 2.1128252), 'Kouandé': (10.3321794, 1.6919847), 'Matéri': (10.8214675, 1.070225078666595), 'Natitingou': (10.3051511, 1.3808554), 'Péhunco': (10.2308948, 2.0004282), 'Tanguiéta': (10.965512, 1.420338250811944), 'Toucountouna': (10.56790835, 1.4922519231480926), 'Abomey-Calavi': (6.4538637, 2.354245), 'Allada': (6.6658411, 2.1511876), 'Kpomassè': (6.479239, 2.0343745060035476), 'Ouidah': (6.3666147, 2.0853599), 'Sô-Ava': (6.5126364, 2.4436602381870856), 'Toffo': (6.8248853, 2.1865379514733916), 'Tori-Bossito': (6.502478, 2.1441704), 'Zè': (6.73078365, 2.3329072503448813), 'Bembéréké': (10.25395885, 2.750742720088743), 'Kalalé': (10.2880733, 3.3792735), "N'Dali": (9.8623108, 2.719146), 'Nikki': (9.9363383, 3.2085658), 'Parakou': (9.3400159, 2.6278258), 'Pèrèrè': (9.605063000000001, 3.0295235323064453), 'Sinendé': (10.260695, 2.367979301912146), 'Tchaourou': (8.8881676, 2.596108), 'Bantè': (8.33007795, 1.8696095473096985), 'Dassa-Zoumé': (7.7815402, 2.183606), 'Glazoué': (8.16811735, 2.2291357527306785), 'Ouèssè': (8.4919261, 2.4258417), 'Savalou': (7.9297324, 1.9780951), 'Savè': (7.9852170000000005, 2.5417577150572566), 'Bassila': (8.96666435, 1.8218396684307867), 'Copargo': (9.8817865, 1.5446319011603729), 'Djougou': (9.7106683, 1.6651614), 'Ouaké': (9.6642475, 1.3859323), 'Aplahoué': (6.9396098, 1.6751946), 'Djakotomey': (6.850139, 1.6955773826214111), 'Dogbo-Tota': (6.801846, 1.7815205), 'Klouékanmè': (7.07500005, 1.8244247611931035), 'Lalo': (6.8744445, 1.9729216960175053), 'Toviklin': (6.891787949999999, 1.8209605779941023), 'Cotonou': (6.3676953, 2.4252507), 'Athiémé': (6.53229705, 1.7414348816705576), 'Bopa': (6.5893347, 1.9668937), 'Comè': (6.4041973, 1.8840863), 'Grand-Popo': (6.2763745, 1.8067199), 'Houéyogbé': (6.5661833, 1.8547538), 'Lokossa': (6.6458524, 1.7171404), 'Adjarra': (6.493028000000001, 2.6933383052933184), 'Adjohoun': (6.6981376, 2.516410998155393), 'Aguégués': (6.4848719500000005, 2.5395829827801037), 'Akpro-Missérété': (6.5750718, 2.6099368012167643), 'Avrankou': (6.5564209, 2.6550687), 'Bonou': (6.89096245, 2.4667140256399183), 'Dangbo': (6.5662073, 2.51544769354959), 'Porto-Novo': (6.4990718, 2.6253361), 'Sèmè-Kpodji': (6.3814684, 2.6044573), 'Adja-Ouèrè': (7.01182455, 2.5983039082882566), 'Ifangni': (6.6805991, 2.718289), 'Kétou': (7.3604193, 2.6024222), 'Pobè': (6.9820238, 2.666791), 'Sakété': (6.7377567, 2.6551566), 'Abomey': (7.1820012, 1.993632), 'Agbangnizoun': (7.075825, 1.9705679), 'Bohicon': (7.1816331, 2.0695683), 'Covè': (7.2999575, 2.298927334403489), 'Djidja': (7.39911905, 1.9769064644898355), 'Ouinhi': (7.08236145, 2.4835912066427603), 'Za-Kpota': (7.22026665, 2.1908969406542544), 'Zagnanado': (7.21660735, 2.3904810986467764), 'Zogbodomey': (7.01729035, 2.20306582428993)}

        # Dictionary holding the population of cities in Benin, 2013
        population = {
            'Kandi': 179290,
            'Natitingou': 103843,
            'Ouidah': 162034,
            'Parakou': 255478,
            'Savalou': 144549,
            'Dogbo-Tota': 103057,
            'Djougou': 267812,
            'Cotonou': 679012,
            'Lokossa': 104961,
            'Porto-Novo': 264320,
            'Sakété': 114088,
            'Abomey': 92266
        }

        # Dictionary holding the area (in km²) of regions in Benin
        area = {
            'Alibori': 26242,
            'Atakora': 20499,
            'Atlantique': 3233,
            'Borgou': 25856,
            'Collines': 13931,
            'Couffo': 2404,
            'Donga': 11126,
            'Littoral': 79,
            'Mono': 1605,
            'Ouémé': 1281,
            'Plateau': 3264,
            'Zou': 5243
        }

        super().__init__(department_mapping, coordinates, population, area)  # Initialize the parent class

        # Dictionary holding the number of agencies based on the service type
        if service_type.lower() == 'bank':
            self.agency_counts = {'Cotonou': 139, 'Porto-Novo': 14, 'Abomey-Calavi': 13, 'Parakou': 10, 'Bohicon': 7, 'Sèmè-Podji': 3, 'Lokossa': 3, 'Grand-Popo': 3, 'Malanville': 2, 'Comè': 2, 'Natitingou': 2, 'Savalou': 1, 'Djougou': 1, 'Abomey': 1, 'Aplahoué': 1, 'Covè': 1, 'Allada': 1, 'Pobè': 1, 'Tanguiéta': 1, 'Banikoara': 0, 'Gogounou': 0, 'Kandi': 0, 'Karimama': 0, 'Segbana': 0, 'Boukoumbé': 0, 'Cobly': 0, 'Kérou': 0, 'Kouandé': 0, 'Matéri': 0, 'Péhunco': 0, 'Toucountouna': 0, 'Kpomassè': 0, 'Ouidah': 0, 'Sô-Ava': 0, 'Toffo': 0, 'Tori-Bossito': 0, 'Zè': 0, 'Bembéréké': 0, 'Kalalé': 0, "N'Dali": 0, 'Nikki': 0, 'Pèrèrè': 0, 'Sinendé': 0, 'Tchaourou': 0, 'Bantè': 0, 'Dassa-Zoumé': 0, 'Glazoué': 0, 'Ouèssè': 0, 'Savè': 0, 'Bassila': 0, 'Copargo': 0, 'Ouaké': 0, 'Djakotomey': 0, 'Dogbo-Tota': 0, 'Klouékanmè': 0, 'Lalo': 0, 'Toviklin': 0, 'Athiémé': 0, 'Bopa': 0, 'Houéyogbé': 0, 'Adjarra': 0, 'Adjohoun': 0, 'Aguégués': 0, 'Akpro-Missérété': 0, 'Avrankou': 0, 'Bonou': 0, 'Dangbo': 0, 'Sèmè-Kpodji': 0, 'Adja-Ouèrè': 0, 'Ifangni': 0, 'Kétou': 0, 'Sakété': 0, 'Agbangnizoun': 0, 'Djidja': 0, 'Ouinhi': 0, 'Za-Kpota': 0, 'Zagnanado': 0, 'Zogbodomey': 0}
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
