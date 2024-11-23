from financial_service import FinancialService

class TogoDepartmentData(FinancialService):
    """ Class to manage data specific to Togo based on the type of financial service. """
    
    def __init__(self, service_type):
        # Dictionary mapping regions to their respective departments
        department_mapping = {
            "Maritime": ["Avé", "Golfe", "Lacs", "Vo", "Yoto", "Zio", "Bas-Mono", "Agoè-Nyivé"],
            "Plateaux": ["Agou", "Akébou", "Amou", "Anié", "Danyi", "Est-Mono", "Haho", "Kloto", "Moyen-Mono", "Ogou", "Wawa", "Kpélé"],
            "Centrale": ["Blitta", "Mô", "Sotouboua", "Tchamba", "Tchaoudjo"],
            "Kara": ["Kozah", "Assoli", "Bassar", "Binah", "Dankpen", "Doufelgou", "Kéran"],
            "Savanes_Togo": ["Cinkassé", "Kpendjal", "Kpendjal-Ouest", "Oti", "Oti-Sud", "Tandjouaré", "Tône"]
        }
        
        # Dictionary holding the geographical coordinates of cities in Togo
        coordinates = {'Golfe': (6.122616407297969, 1.2210703043977398), 'Lacs': (6.23906865, 1.6221267334297442), 'Vo': (6.402985, 1.525283), 'Yoto': (6.7354794, 1.3127133), 'Zio': (6.4815405, 1.0594082), 'Bas-Mono': (6.4583267, 1.7075987), 'Agoè-Nyivé': (6.224265, 1.2101671), 'Agou': (6.85462025, 0.7291426853431653), 'Akébou': (7.8009867, 0.6596978), 'Amou': (7.3431616, 1.1708104), 'Anié': (7.7594052, 1.1965329), 'Danyi': (7.1675142, 0.6308336), 'Est-Mono': (8.1098252, 1.3518737), 'Haho': (6.703928279530556, 1.2537056825753818), 'Kloto': (6.947935, 0.579546), 'Moyen-Mono': (7.0546875, 1.6124747), 'Ogou': (8.4792909, 1.5438297), 'Wawa': (7.686416400000001, 0.5888108233468348), 'Kpélé': (6.8596846, 1.1842139), 'Blitta': (8.35353095, 0.9963413304880842), 'Sotouboua': (8.484799500000001, 0.9471545424212758), 'Tchamba': (8.8294049, 1.473464180690247), 'Tchaoudjo': (8.9826228, 1.133915145313403), 'Kozah': (9.5899785, 1.1534875974893626), 'Assoli': (9.3358244, 1.1872873897992815), 'Bassar': (9.2501955, 0.7718031022037812), 'Binah': (9.7427315, 1.324484), 'Dankpen': (9.7195902, 0.6041652403511807), 'Doufelgou': (9.87120045, 1.1762304268401662), 'Kéran': (10.0256015, 0.9281346202815028), 'Cinkassé': (11.10107, 0.0157272), 'Kpendjal': (10.8550907, 0.22980296783364068), 'Kpendjal-Ouest': (10.7283174, 0.3827182), 'Oti': (10.30576285978697, 0.46979020983094305), 'Tandjouaré': (10.6690145, 0.1960154), 'Tône': (10.80609085, 0.6849561357118255), 'Avé': (6.430292, 0.930962), 'Mô': (8.7824759, 0.5647293), 'Oti-Sud': (10.3315816, 0.7472741)}

        # Dictionary holding the population of each region in Togo
        regions_population = {
            'Kara': 985512,
            'Centrale': 795529,
            'Maritime': 1346615+2188376,
            'Plateaux': 1635946,
            'Savanes_Togo': 1143520
        }

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
            self.agency_counts = {'Golfe': 112, 'Kozah': 9, 'Ogou': 8, 'Cinkassé': 8, 'Tchaoudjo': 7, 'Lacs': 4, 'Oti': 4, 'Tône': 4, 'Kloto': 4, 'Bassar': 3, 'Vo': 3, 'Haho': 2, 'Yoto': 2, 'Sotouboua': 2, 'Kéran': 2, 'Doufelgou': 2, 'Assoli': 2, 'Anié': 2, 'Zio': 2, 'Binah': 1, 'Dankpen': 1, 'Wawa': 1, 'Avé': 0, 'Bas-Mono': 0, 'Agoè-Nyivé': 0, 'Agou': 0, 'Akébou': 0, 'Amou': 0, 'Danyi': 0, 'Est-Mono': 0, 'Moyen-Mono': 0, 'Kpélé': 0, 'Blitta': 0, 'Mô': 0, 'Tchamba': 0, 'Kpendjal': 0, 'Kpendjal-Ouest': 0, 'Oti-Sud': 0, 'Tandjouaré': 0}
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
