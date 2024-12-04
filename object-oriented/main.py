from bank_agencies import BankAgencies
from geographic_data import GeographicData
from indicator_calculator import IndicatorCalculator
from data.benin_data import BeninData
from data.togo_data import TogoData
#from data.civ_data import CIVData
from map_visualizer import MapVisualizer
from chart_visualizer import ChartVisualizer
from utils import normalize_scores, format_scores, round_scores, mean_scores, mean, alpha_values
from data.civ_department_data import CIVDepartmentData
from data.mali_data import MaliData
from data.burkina_department_data import BurkinaDepartmentData
from data.niger_data import NigerData
from data.guinee_data import GuineeData
from data.benin_department_data import BeninDepartmentData
from data.togo_department_data import TogoDepartmentData
from data.guinee_department_data import GuineeDepartmentData
from data.niger_department_data import NigerDepartmentData
from data.senegal_department_data import SenegalDepartmentData

# Import necessary Python libraries
import geopandas as gpd
import pandas as pd
import numpy as np

# Constants
THRESHOLD = 100  # Distance threshold for neighbors
REF_INHABITANTS = 100000  # Reference number of inhabitants for demographic indicator

# scores for access to infrastructures https://www.integrate-africa.org/fr/classements/dimensions/integration-des-infrastructures/
access_to_infrastructures = {
    'Benin': 0.174,
    'Togo': 0.150,
    'Côte d\'Ivoire': 0.292,
    'Mali': 0.154,
    'Burkina Faso': 0.147,
    'Niger': 0.069,
    'Guinée Bissau': 0.081,
    'Sénégal': 0.241
}

alpha_countries = alpha_values(access_to_infrastructures, 1.01, 1.04)


#define the alpha value for each country as constants
ALPHA_BENIN = alpha_countries['Benin']
ALPHA_TOGO = alpha_countries['Togo']
ALPHA_CIV = alpha_countries['Côte d\'Ivoire']
ALPHA_MALI = alpha_countries['Mali']
ALPHA_BURKINA = alpha_countries['Burkina Faso']
ALPHA_NIGER =  alpha_countries['Niger']
ALPHA_GUINEE = alpha_countries['Guinée Bissau']
ALPHA_SENEGAL = alpha_countries['Sénégal']


print('Access to infrastructures:', alpha_countries)

def load_country_shapefiles():
    benin = gpd.read_file('/Users/haouabenaliabbo/Downloads/ben_adm_1m_salb_2019_shapes/ben_admbnda_adm0_1m_salb_20190816.shp')
    togo = gpd.read_file('/Users/haouabenaliabbo/Downloads/Shapefiles_togo/tgo_admbnda_adm0_inseed_itos_20210107.shp')
    civ = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/civ_admbnda_adm0_cntig_20180706/civ_admbnda_adm0_cntig_20180706.shp')
    mali = gpd.read_file('/Users/haouabenaliabbo/Downloads/mali_adm_ab_shp/mli_admbnda_adm0_1m_gov_20211220.shp')
    burkina = gpd.read_file('/Users/haouabenaliabbo/Downloads/geoBoundaries-BFA-ADM0-all/geoBoundaries-BFA-ADM0_simplified.shp')
    niger = gpd.read_file('/Users/haouabenaliabbo/Downloads/ner_adm_ignn_20230720_ab_shp/NER_admbnda_adm0_IGNN_20230720.shp')
    guinee = gpd.read_file('/Users/haouabenaliabbo/Downloads/gnb_admbnda_1m_salb_20210609_shp/gnb_admbnda_adm0_1m_salb_20210609.shp')
    senegal = gpd.read_file('/Users/haouabenaliabbo/Downloads/sen_admbnd_anat_20240520_ab_shp/sen_admbnda_adm0_anat_20240520.shp')

    benin['admin1Name']='Bénin'
    togo['admin1Name']='Togo'
    civ['admin1Name']='Côte d\'Ivoire'
    mali['admin1Name']='Mali'
    burkina['admin1Name']='Burkina Faso'
    niger['admin1Name']='Niger'
    guinee['admin1Name']='Guinée Bissau'
    senegal['admin1Name']='Sénégal'

    togo['country'] = 'Togo'
    civ['country'] = "Côte d'Ivoire"
    mali['country'] = "Mali"
    burkina['country'] = "Burkina Faso"
    benin['country'] = 'Bénin'
    niger['country'] = 'Niger'
    guinee['country'] = 'Guinée Bissau'
    senegal['country'] = 'Sénégal'



    combined = pd.concat([benin, togo, civ, mali, burkina, niger, guinee, senegal], ignore_index=True)

    #combined.to_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/uemoa_countries.shp')

    return combined

def load_shapefiles():
    benin = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/ben_adm_1m_salb_2019_shapes') #change path once folder updated on GitHub
    togo = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/Shapefiles_togo') #change path once folder updated on GitHub
    civ = gpd.read_file("/Users/haouabenaliabbo/Downloads/202303_OSM2IGEO_COTE_D_IVOIRE_SHP_WGS84_4326/H_OSM_ADMINISTRATIF/DISTRICT.shp") #change path once folder updated on GitHub
    mali = gpd.read_file('/Users/haouabenaliabbo/Downloads/mali_adm_ab_shp/mli_admbnda_adm1_1m_gov_20211220.shp')
    burkina = gpd.read_file('/Users/haouabenaliabbo/Downloads/geoBoundaries-BFA-ADM1-all/geoBoundaries-BFA-ADM1_simplified.shp')
    niger = gpd.read_file('/Users/haouabenaliabbo/Downloads/ner_adm_ignn_20230720_ab_shp/NER_admbnda_adm1_IGNN_20230720.shp')
    guinee = gpd.read_file('/Users/haouabenaliabbo/Downloads/gnb_admbnda_1m_salb_20210609_shp/gnb_admbnda_adm1_1m_salb_20210609.shp')
    senegal = gpd.read_file('/Users/haouabenaliabbo/Downloads/sen_admbnd_anat_20240520_ab_shp/sen_admbnda_adm1_anat_20240520.shp')

    # Add columns for country names
    togo['country'] = 'Togo'
    civ['country'] = "Côte d'Ivoire"
    mali['country'] = "Mali"
    burkina['country'] = "Burkina Faso"
    benin['country'] = 'Bénin'
    niger['country'] = 'Niger'
    guinee['country'] = 'Guinée Bissau'
    senegal['country'] = 'Sénégal'

    # Rename columns for consistency
    benin = benin.rename(columns={'adm1_name': 'admin1Name'})
    #benin = benin.rename(columns={'adm0_name': 'country'})
    togo = togo.rename(columns={'ADM1_FR': 'admin1Name'})
    #togo = togo.rename(columns={'ADM1_REF': 'country'})
    civ = civ.rename(columns={'NOM': 'admin1Name'})
    mali = mali.rename(columns={'ADM1_FR': 'admin1Name'})
    burkina = burkina.rename(columns={'shapeName': 'admin1Name'})
    niger = niger.rename(columns={'ADM1_FR': 'admin1Name'})
    guinee = guinee.rename(columns={'ADM1_EN': 'admin1Name'})
    senegal = senegal.rename(columns={'ADM1_FR': 'admin1Name'})

    # Rename regions with common names to avoid conflicts
    benin['admin1Name'] = benin['admin1Name'].replace('Oueme', 'Ouémé')
    togo['admin1Name'] = togo['admin1Name'].replace('Savanes', 'Savanes_Togo')
    civ['admin1Name'] = civ['admin1Name'].replace('Savanes', 'Savanes_CIV')
    guinee['admin1Name'] = guinee['admin1Name'].replace('Bolama/Bijagos', 'Bolama')
    burkina['admin1Name'] = burkina['admin1Name'].replace('Plateau Central', 'Plateau-Central')
    senegal['admin1Name'] = senegal['admin1Name'].replace('Saint-Louis', 'Saint Louis')

    # Fusion shapefiles for combined maps
    combined = pd.concat([benin, togo, civ, mali, burkina, niger, guinee, senegal], ignore_index=True)
    #combined.to_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/uemoa_regions.shp')
    #print(combined[['admin1Name', 'country']])


    return benin, togo, civ, mali, burkina, niger, guinee, senegal, combined

def load_department_shapefiles():
    civ= gpd.read_file('/Users/haouabenaliabbo/Downloads/civ_admbnda_adm2_cntig_ocha_itos_20180706 (2)/civ_admbnda_adm2_cntig_ocha_itos_20180706.shp')
    civ = civ.rename(columns={'ADM2_FR': 'admin1Name'})
    civ['admin1Name'] = civ['admin1Name'].replace('Béttié', 'Bettié')
    civ['admin1Name'] = civ['admin1Name'].replace('Djekanou', 'Djékanou')
    civ['admin1Name'] = civ['admin1Name'].replace('Didievi', 'Didiévi')
    civ['admin1Name'] = civ['admin1Name'].replace('San Pédro', 'San-Pédro')
    civ['admin1Name'] = civ['admin1Name'].replace('Odienne', 'Odienné')
    civ['admin1Name'] = civ['admin1Name'].replace('Gbeleban', 'Gbéléban')
    civ['admin1Name'] = civ['admin1Name'].replace('Tengrela', 'Tengréla')
    civ['admin1Name'] = civ['admin1Name'].replace('Toulepleu', 'Toulépleu')
    civ['admin1Name'] = civ['admin1Name'].replace('Sandegue', 'Sandégué')
    civ['admin1Name'] = civ['admin1Name'].replace('Koun Fao', 'Koun-Fao')

    mali= gpd.read_file('/Users/haouabenaliabbo/Downloads/mali_adm_ab_shp/mli_admbnda_adm2_1m_gov_20211220.shp')
    mali= mali.rename(columns={'ADM2_FR': 'admin1Name'})
    mali['admin1Name'] = mali['admin1Name'].replace('Bafoulabe', 'Bafoulabé')

    burkina=gpd.read_file('/Users/haouabenaliabbo/Downloads/geoBoundaries-BFA-ADM2-all/geoBoundaries-BFA-ADM2_simplified.shp')
    burkina = burkina.rename(columns={'shapeName': 'admin1Name'})
    burkina['admin1Name']=burkina['admin1Name'].replace('Komonjdjari', 'Komondjari')
    #burkina['admin1Name']=burkina['admin1Name'].replace('Kourittenga', 'Kouritenga')
    province_replacements = {
        'Kourweogo': 'Kourwéogo',
        'Boulkiembe': 'Boulkiembé',
        'Comoe': 'Comoé',
        'Boulkiemde': 'Boulkiemdé',
        'Seno': 'Séno',
        'Kenedougou': 'Kénédougou',
        'Zoudweogo': 'Zoudwéogo',
        'Bale': 'Balé',
        'Passore': 'Passoré',
        'Koulpelogo': 'Koulpélogo',
        'Sanguie': 'Sanguié',
        'Zoundweogo': 'Zoundwéogo',
        'Leraba': 'Léraba',
        'Bazega': 'Bazèga',
    }

    # Replace names in 'admin1Name' column based on the above mappings
    for old_name, new_name in province_replacements.items():
        burkina['admin1Name'] = burkina['admin1Name'].replace(old_name, new_name)
    
    civ['country'] = "Côte d'Ivoire"
    mali['country'] = "Mali"
    burkina['country'] = "Burkina Faso"

    benin = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/ben_adm_1m_salb_2019_shapes/ben_admbnda_adm2_1m_salb_20190816.shp')
    benin = benin.rename(columns={'adm2_name': 'admin1Name'})
    benin['country'] = 'Bénin'
    commune_replacements_benin = {'Djakotome': 'Djakotomey', 'Dogbo-tota': 'Dogbo-Tota', 'Kopargo': 'Copargo', 'Banikoara': 'Banikoara', 'Gogounou': 'Gogounou', 'Kandi': 'Kandi', 'Karimama': 'Karimama', 'Malanville': 'Malanville', 'Segbana': 'Segbana', 'Kerou': 'Kérou', 'Kobli': 'Cobly', 'Kouande': 'Kouandé', 'Materi': 'Matéri', 'Natitingou': 'Natitingou', 'Pehunco': 'Péhunco', 'Tanguieta': 'Tanguiéta', 'Allada': 'Allada', 'Kpomasse': 'Kpomassè', 'Ouidah': 'Ouidah', 'Toffo': 'Toffo', 'Ze': 'Zè', 'Bembereke': 'Bembéréké', 'Kalale': 'Kalalé', 'Nikki': 'Nikki', 'Parakou': 'Parakou', 'Perere': 'Pèrèrè', 'Sinende': 'Sinendé', 'Tchaourou': 'Tchaourou', 'Bante': 'Bantè', 'Glazoue': 'Glazoué', 'Ouesse': 'Ouèssè', 'Savalou': 'Savalou', 'Save': 'Savè', 'Aplahoue': 'Aplahoué', 'Klouekanme': 'Klouékanmè', 'Lalo': 'Lalo', 'Toviklin': 'Toviklin', 'Bassila': 'Bassila', 'Djougou': 'Djougou', 'Ouake': 'Ouaké', 'Cotonou': 'Cotonou', 'Athieme': 'Athiémé', 'Bopa': 'Bopa', 'Come': 'Comè', 'Houeyogbe': 'Houéyogbé', 'Lokossa': 'Lokossa', 'Adjohoun': 'Adjohoun', 'Avrankou': 'Avrankou', 'Bonou': 'Bonou', 'Dangbo': 'Dangbo', 'Ifangni': 'Ifangni', 'Ketou': 'Kétou', 'Pobe': 'Pobè', 'Sakete': 'Sakété', 'Abomey': 'Abomey', 'Agbangnizoun': 'Agbangnizoun', 'Bohicon': 'Bohicon', 'Cove': 'Covè', 'Djidja': 'Djidja', 'Ouinhi': 'Ouinhi', 'Zogbodomey': 'Zogbodomey', 'Aguegues': 'Aguégués', 'Boukoumbe': 'Boukoumbé', 'Toukountouna': 'Toucountouna', 'Abomey-calavi': 'Abomey-Calavi', 'So-ava': 'Sô-Ava', 'Tori-bossito': 'Tori-Bossito', 'Ndali': 'N\'Dali', 'Dassa': 'Dassa-Zoumé', 'Grand-popo': 'Grand-Popo', 'Adjara': 'Adjarra', 'Akpro-misserete': 'Akpro-Missérété', 'Porto-novo': 'Porto-Novo', 'Seme-kpodji': 'Sèmè-Kpodji', 'Adja-ouere': 'Adja-Ouèrè', 'Za-kpota': 'Za-Kpota', 'Zangnanado': 'Zagnanado'}


    # Replace names in 'admin1Name' column based on the above mappings
    for old_name, new_name in commune_replacements_benin.items():
        benin['admin1Name'] = benin['admin1Name'].replace(old_name, new_name)

    togo = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/Shapefiles_togo/tgo_admbnda_adm2_inseed_itos_20210107.shp')
    togo = togo.rename(columns={'ADM2_FR': 'admin1Name'})
    togo['country'] = 'Togo'

    togo_names_dict = {
        'Agoe-Nyive': 'Agoè-Nyivé',
        'Akebou': 'Akébou',
        'Anie': 'Anié',
        'Ave': 'Avé',
        'Cinkasse': 'Cinkassé',
        'Keran': 'Kéran',
        'Kpele': 'Kpélé',
        'Lome Commune': 'Golfe',
        'Plaine du Mo': 'Mô',
        'Tandjoare': 'Tandjouaré',
        'Tone': 'Tône',
        'Naki-Ouest': 'Tône'
    }

    # Replace names in 'admin1Name' column based on the above mappings
    for old_name, new_name in togo_names_dict.items():
        togo['admin1Name'] = togo['admin1Name'].replace(old_name, new_name)

    guinee = gpd.read_file('/Users/haouabenaliabbo/Downloads/gnb_admbnda_1m_salb_20210609_shp/gnb_admbnda_adm2_1m_salb_20210609.shp')
    guinee = guinee.rename(columns={'ADM2_EN': 'admin1Name'})
    guinee['country'] = 'Guinée Bissau'
    secteurs_mapping = {'Gabu': 'Gabú', 'Gamamudo/Ganadu': 'Gamamundo', 'Cacheu/Calequisse': 'Cacheu', 'Caio': 'Caió', 'Boe': 'Boé', 'Gabu': 'Gabú', 'Bissora': 'Bissorã', 'Mansoa': 'Mansôa', 'Catio': 'Catió', 'Sector Autonomo de Bissau': 'Bissau', 'Prabis': 'Prábis', 'Quinhamel': 'Quinhámel', 'Galomaro/Cosse':'Galomaro'}
    for old_name, new_name in secteurs_mapping.items():
        guinee['admin1Name'] = guinee['admin1Name'].replace(old_name, new_name)

    niger=gpd.read_file('/Users/haouabenaliabbo/Downloads/ner_adm_ignn_20230720_ab_shp/NER_admbnda_adm2_IGNN_20230720.shp')
    niger.rename(columns={'ADM2_FR': 'admin1Name'}, inplace=True)
    niger['country'] = 'Niger'
    niger['admin1Name']=niger['admin1Name'].replace('Ville de Maradi', 'Maradi')
    niger_department_mapping = {
        'Iferouane': 'Iférouane',
        'Belbedji': 'Belbédji',
        'Ville de Niamey': 'Niamey',
        'Ville de Tahoua': 'Tahoua',
        'Keita': 'Takeita',
        'Falmey': 'Falmèy',
        'Maïné Soroa': 'Maïné-Soroa',
        'Ayerou': 'Ayérou',
        'Guidan Roumdji': 'Guidan-Roumdji',
        'Tchirozerine': 'Tchirozérine',
        'Ville de Zinder': 'Zinder',
    }
    for old, new in niger_department_mapping.items():
        niger['admin1Name'] = niger['admin1Name'].replace(old, new)

    senegal=gpd.read_file('/Users/haouabenaliabbo/Downloads/sen_admbnd_anat_20240520_ab_shp/sen_admbnda_adm2_anat_20240520.shp')
    senegal.rename(columns={'ADM2_FR': 'admin1Name'}, inplace=True)
    senegal['country'] = 'Sénégal'

    combined = pd.concat([benin, togo, civ, mali, burkina, niger, guinee, senegal], ignore_index=True)
    #combined.to_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/uemoa_departments.shp')
    
    return civ, mali, burkina, benin, togo, guinee, niger, senegal, combined 


# Load geographic data
combined0 = load_country_shapefiles()
benin, togo, civ, mali, burkina, niger, guinee, senegal, combined = load_shapefiles()
civ2, mali2, burkina2, benin2, togo2, guinee2, niger2, senegal2, combined2 = load_department_shapefiles()  





def main():

    '''Generic functions and initialisation'''

    # Initialize data classes
    benin_data = BeninData(service_type='bank')
    togo_data = TogoData(service_type='bank')
    #civ_data = CIVData(service_type='bank')
    niger_data = NigerData(service_type='bank')
    guinee_data = GuineeData(service_type='bank')

    # Initialize BankAgencies instances
    bank_agencies_benin = BankAgencies(
        benin_data.get_agency_counts(),
        benin_data.get_department_mapping(),
        benin_data.get_coordinates()
    )
    bank_agencies_togo = BankAgencies(
        togo_data.get_agency_counts(),
        togo_data.get_department_mapping(),
        togo_data.get_coordinates()
    )
    #bank_agencies_civ = BankAgencies(
    #    civ_data.get_agency_counts(),
    #    civ_data.get_department_mapping(),
    #    civ_data.get_coordinates()
    #)
    bank_agencies_niger = BankAgencies(
        niger_data.get_agency_counts(),
        niger_data.get_department_mapping(),
        niger_data.get_coordinates()
    )
    bank_agencies_guinee = BankAgencies(
        guinee_data.get_agency_counts(),
        guinee_data.get_department_mapping(),
        guinee_data.get_coordinates()
    )


    """"Indicator 2 : Demographic indicator
    # Calculate demographic indicators
    demo_indicator_benin = round_scores(indicator_calculator_benin.demographic_indicator(REF_INHABITANTS))
    demo_indicator_togo = round_scores(indicator_calculator_togo.demographic_indicator(REF_INHABITANTS))
    #demo_indicator_civ = round_scores(indicator_calculator_civ.demographic_indicator(REF_INHABITANTS))
    #demo_indicator_combined = {**demo_indicator_benin, **demo_indicator_togo, **demo_indicator_civ}
    #print(demo_indicator_combined)

    # calculate spatial demographic indicators
    spatial_demo_indicator_benin = round_scores(indicator_calculator_benin.spatial_demographic_indicator(REF_INHABITANTS, THRESHOLD))
    spatial_demo_indicator_togo = round_scores(indicator_calculator_togo.spatial_demographic_indicator(REF_INHABITANTS, THRESHOLD))
    #spatial_demo_indicator_civ = round_scores(indicator_calculator_civ.spatial_demographic_indicator(REF_INHABITANTS, THRESHOLD))
    #spatial_demo_indicator_combined = {**spatial_demo_indicator_benin, **spatial_demo_indicator_togo, **spatial_demo_indicator_civ}
    #print(spatial_demo_indicator_combined)

    Charts for demographic indicators
    # demographic indicators 
    chart_visualizer_benin = ChartVisualizer(demo_indicator_benin, type="régions", label="demographic_indicator", country="benin")
    chart_visualizer_benin.create_bar_chart()

    chart_visualizer_togo = ChartVisualizer(demo_indicator_togo, type="régions", label="demographic_indicator", country="togo")
    chart_visualizer_togo.create_bar_chart()

    chart_visualizer_civ = ChartVisualizer(demo_indicator_civ, type='régions', label="demographic_indicator", country="civ")
    #chart_visualizer_civ.create_bar_chart()

    chart_visualizer_combined = ChartVisualizer(demo_indicator_combined, type="régions", label="demographic_indicator", country="combined")
    chart_visualizer_combined.create_bar_chart()


    # spatial demographic indicators
    #chart_visualizer_benin = ChartVisualizer(spatial_demo_indicator_benin, title=f"Nombres d'agences pour {REF_INHABITANTS_BENIN} habitants pour l'agglomération urbaine", label="spatial_demographic_indicator", country="benin")
    #chart_visualizer_benin.create_bar_chart()

    #chart_visualizer_togo = ChartVisualizer(spatial_demo_indicator_togo, title=f"Nombres d'agences pour {REF_INHABITANTS_TOGO} habitants pour l'agglomération urbaine", label="spatial_demographic_indicator",  country="togo")
    #chart_visualizer_togo.create_bar_chart()

    #chart_visualizer_civ = ChartVisualizer(spatial_demo_indicator_civ, title=f"Nombres d'agences pour {REF_INHABITANTS_CIV} habitants pour l'agglomération urbaine", label="spatial_demographic_indicator", country="civ")
    #chart_visualizer_civ.create_bar_chart()

    #chart_visualizer_combined = ChartVisualizer(spatial_demo_indicator_combined, title=f"Nombres d'agences combiné", label="spatial_demographic_indicator", country="combined")
    #chart_visualizer_combined.create_bar_chart()

    """

    '''BENIN ADJUSTMENTS'''

    # Initialize data classes
    benin_data2 = BeninDepartmentData(service_type='bank')

    # Initialize BankAgencies instances
    bank_agencies_benin2 = BankAgencies(
        benin_data2.get_agency_counts(),
        benin_data2.get_department_mapping(),
        benin_data2.get_coordinates()
    )

    geographic_data_benin2 = GeographicData(benin_data2.get_coordinates())

    neighbors_benin2 = geographic_data_benin2.compute_neighbors(distance_threshold=THRESHOLD)

    '''Indicator 1 : ISIBF score'''

    # Calculate ISIBF values
    indicator_calculator_benin2 = IndicatorCalculator(bank_agencies_benin2.get_agency_counts(), neighbors_benin2, benin_data2.get_adult_population(), alpha=ALPHA_BENIN, threshold=THRESHOLD, department_mapping=benin_data2.get_department_mapping(), area=benin_data2.get_area())
    isibf_departments_benin = indicator_calculator_benin2.calculate_isibf2()
    # Global normalization and formatting
    isibf_regions_benin = mean_scores(isibf_departments_benin, benin_data2.get_department_mapping())

    # Normalization by countries
    isibf_departments_benin_norm = format_scores(normalize_scores(isibf_departments_benin))
    isibf_regions_benin_norm = format_scores(mean_scores(normalize_scores(isibf_departments_benin), benin_data2.get_department_mapping()))

    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries
    map_visualizer_benin2 = MapVisualizer(benin2, isibf_departments_benin_norm, label="ISIBF", type="commune", lat=9.5, lon=2.3, zoom=6.5, country="benin")
    #map_visualizer_benin2.create_choropleth()
    map_visualizer_benin2.create_leaflet()

    map_visualizer_benin_regions = MapVisualizer(benin, isibf_regions_benin_norm, label="ISIBF", type="département", lat=9.5, lon=2.3, zoom=6.5, country="benin")
    #map_visualizer_benin_regions.create_choropleth()
    map_visualizer_benin_regions.create_leaflet()

    '''Indicator 2 : Demographic indicator'''

    # demographic indicators
    demo_indicator_benin = round(indicator_calculator_benin2.demographic_indicator_country())

    '''Indicator 3 : Geographic indicator'''

    # geographic indicators
    geo_indicator_benin = round(indicator_calculator_benin2.geographic_indicator())







    ''' TOGO ADJUSTMENTS'''

    # Initialize data classes
    togo_data2 = TogoDepartmentData(service_type='bank')

    # Initialize BankAgencies instances
    bank_agencies_togo2 = BankAgencies(
        togo_data2.get_agency_counts(),
        togo_data2.get_department_mapping(),
        togo_data2.get_coordinates()
    )

    geographic_data_togo2 = GeographicData(togo_data2.get_coordinates())

    neighbors_togo2 = geographic_data_togo2.compute_neighbors(distance_threshold=THRESHOLD)

    '''Indicator 1 : ISIBF score'''

    # Calculate ISIBF values

    indicator_calculator_togo2 = IndicatorCalculator(bank_agencies_togo2.get_agency_counts(), neighbors_togo2, togo_data2.get_adult_population(), alpha=ALPHA_TOGO, threshold=THRESHOLD, department_mapping=togo_data2.get_department_mapping(), area=togo_data2.get_area())
    isibf_departments_togo = indicator_calculator_togo2.calculate_isibf2()
    # Global normalization and formatting
    isibf_regions_togo = mean_scores(isibf_departments_togo, togo_data2.get_department_mapping())

    # Normalization by countries
    isibf_departments_togo_norm = format_scores(normalize_scores(isibf_departments_togo))

    isibf_regions_togo_norm = format_scores(mean_scores(normalize_scores(isibf_departments_togo), togo_data2.get_department_mapping()))

    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries

    map_visualizer_togo2 = MapVisualizer(togo2, isibf_departments_togo_norm, label="ISIBF", type="préfecture", lat=8.6, lon=0.9, zoom=6.5, country="togo")
    #map_visualizer_togo2.create_choropleth()
    map_visualizer_togo2.create_leaflet()

    map_visualizer_togo_regions = MapVisualizer(togo, isibf_regions_togo_norm, label="ISIBF", type="région", lat=8.6, lon=0.9, zoom=6.5, country="togo")
    #map_visualizer_togo_regions.create_choropleth()
    map_visualizer_togo_regions.create_leaflet()



    '''Indicator 2 : Demographic indicator'''

    # demographic indicators
    demo_indicator_togo=round(indicator_calculator_togo2.demographic_indicator_country())

    '''Indicator 3 : Geographic indicator'''

    # geographic indicators
    geo_indicator_togo = round(indicator_calculator_togo2.geographic_indicator()) 



    '''COTE D'IVOIRE ADJUSTMENTS'''

    # Initialize data classes
    civ_data2 = CIVDepartmentData(service_type='bank')

    # Initialize BankAgencies instances
    bank_agencies_civ2 = BankAgencies(
        civ_data2.get_agency_counts(),
        civ_data2.get_department_mapping(),
        civ_data2.get_coordinates()
    )

    geographic_data_civ2 = GeographicData(civ_data2.get_coordinates())

    neighbors_civ2 = geographic_data_civ2.compute_neighbors(distance_threshold=THRESHOLD)

    '''Indicator 1 : ISIBF score'''

    # Calculate ISIBF values
    indicator_calculator_civ2 = IndicatorCalculator(bank_agencies_civ2.get_agency_counts(), neighbors_civ2, civ_data2.get_adult_population(), alpha=ALPHA_CIV, threshold=THRESHOLD, department_mapping=civ_data2.get_department_mapping(), area=civ_data2.get_area())
    isibf_departments_civ = indicator_calculator_civ2.calculate_isibf2()
    # Global normalization and formatting
    isibf_regions_civ = mean_scores(isibf_departments_civ, civ_data2.get_department_mapping())


    # Normalization by countries
    isibf_departments_civ_norm = format_scores(normalize_scores(isibf_departments_civ))
    isibf_regions_civ_norm = format_scores(mean_scores(normalize_scores(isibf_departments_civ), civ_data2.get_department_mapping()))

    


    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries
    map_visualizer_civ = MapVisualizer(civ2, isibf_departments_civ_norm, label="ISIBF", type="département", lat=7.5, lon=-5.5, zoom=6.5, country="civ")
    #map_visualizer_civ.create_choropleth()
    map_visualizer_civ.create_leaflet()

    map_visualizer_civ_regions = MapVisualizer(civ, isibf_regions_civ_norm, label="ISIBF", type="district", lat=7.5, lon=-5.5, zoom=6.5, country="civ")
    #map_visualizer_civ_regions.create_choropleth()
    map_visualizer_civ_regions.create_leaflet()



    '''Indicator 2 : Demographic indicator'''

    # demographic indicators
    demo_indicator_civ=round(indicator_calculator_civ2.demographic_indicator_country())

    #demo_indicator_civ_regions=format_scores(mean_scores(indicator_calculator_civ2.demographic_indicator(REF_INHABITANTS), civ_data2.get_department_mapping()))

    #chart_visualizer_civ = ChartVisualizer(demo_indicator_civ_regions, type="districts", label="demographic_indicator", country="civ")
    #chart_visualizer_civ.create_bar_chart()

    '''Indicator 3 : Geographic indicator'''

    # geographic indicators
    geo_indicator_civ = round(indicator_calculator_civ2.geographic_indicator())





    '''GUINEE ADJUSTMENTS'''

    # Initialize data classes
    guinee_data2 = GuineeDepartmentData(service_type='bank')

    # Initialize BankAgencies instances
    bank_agencies_guinee2 = BankAgencies(
        guinee_data2.get_agency_counts(),
        guinee_data2.get_department_mapping(),
        guinee_data2.get_coordinates()
    )

    geographic_data_guinee2 = GeographicData(guinee_data2.get_coordinates())

    neighbors_guinee2 = geographic_data_guinee2.compute_neighbors(distance_threshold=THRESHOLD)

    '''Indicator 1 : ISIBF score'''

    # Calculate ISIBF values
    indicator_calculator_guinee2 = IndicatorCalculator(bank_agencies_guinee2.get_agency_counts(), neighbors_guinee2, guinee_data2.get_adult_population(), alpha=ALPHA_GUINEE, threshold=THRESHOLD, department_mapping=guinee_data2.get_department_mapping(), area=guinee_data2.get_area())
    isibf_departments_guinee = indicator_calculator_guinee2.calculate_isibf2()
    # Global normalization and formatting
    isibf_regions_guinee = mean_scores(isibf_departments_guinee, guinee_data2.get_department_mapping())

    # Normalization by countries
    isibf_departments_guinee_norm = format_scores(normalize_scores(isibf_departments_guinee))

    isibf_regions_guinee_norm = format_scores(mean_scores(normalize_scores(isibf_departments_guinee), guinee_data2.get_department_mapping()))

    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries

    map_visualizer_guinee = MapVisualizer(guinee2, isibf_departments_guinee_norm, label="ISIBF", type="secteur", lat=11.8, lon=-15, zoom=7.5, country="guinee")
    #map_visualizer_guinee.create_choropleth()
    map_visualizer_guinee.create_leaflet()

    map_visualizer_guinee_regions = MapVisualizer(guinee, isibf_regions_guinee_norm, label="ISIBF", type="région", lat=11.8, lon=-15, zoom=7.5, country="guinee")
    #map_visualizer_guinee_regions.create_choropleth()
    map_visualizer_guinee_regions.create_leaflet()

    '''Indicator 2 : Demographic indicator'''
    demo_indicator_guinee=round(indicator_calculator_guinee2.demographic_indicator_country())

    '''Indicator 3 : Geographic indicator'''

    # geographic indicators
    geo_indicator_guinee = round(indicator_calculator_guinee2.geographic_indicator())



    '''NIGER ADJUSTMENTS'''

    # Initialize data classes
    niger_data2 = NigerDepartmentData(service_type='bank')
    
    # Initialize BankAgencies instances
    bank_agencies_niger2 = BankAgencies(
        niger_data2.get_agency_counts(),
        niger_data2.get_department_mapping(),
        niger_data2.get_coordinates()
    )

    geographic_data_niger2 = GeographicData(niger_data2.get_coordinates())

    neighbors_niger2 = geographic_data_niger2.compute_neighbors(distance_threshold=THRESHOLD)

    '''Indicator 1 : ISIBF score'''

    # Calculate ISIBF values
    indicator_calculator_niger2 = IndicatorCalculator(bank_agencies_niger2.get_agency_counts(), neighbors_niger2, niger_data2.get_adult_population(), alpha=ALPHA_NIGER, threshold=THRESHOLD, department_mapping=niger_data2.get_department_mapping(), area=niger_data2.get_area())
    isibf_departments_niger = indicator_calculator_niger2.calculate_isibf2()
    # Global normalization and formatting
    isibf_regions_niger = mean_scores(isibf_departments_niger, niger_data2.get_department_mapping())

    # Normalization by countries
    isibf_departments_niger_norm = format_scores(normalize_scores(isibf_departments_niger))

    isibf_regions_niger_norm = format_scores(mean_scores(normalize_scores(isibf_departments_niger), niger_data2.get_department_mapping()))

    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries

    map_visualizer_niger = MapVisualizer(niger2, isibf_departments_niger_norm, label="ISIBF", type="département", lat=17.6, lon=8.1, zoom=5.5, country="niger")
    #map_visualizer_niger.create_choropleth()
    map_visualizer_niger.create_leaflet()

    map_visualizer_niger_regions = MapVisualizer(niger, isibf_regions_niger_norm, label="ISIBF", type="région", lat=17.6, lon=8.1, zoom=5.5, country="niger")
    #map_visualizer_niger_regions.create_choropleth()
    map_visualizer_niger_regions.create_leaflet()

    '''Indicator 2 : Demographic indicator'''

    # demographic indicators
    demo_indicator_niger=round(indicator_calculator_niger2.demographic_indicator_country())

    '''Indicator 3 : Geographic indicator'''

    # geographic indicators
    geo_indicator_niger = round(indicator_calculator_niger2.geographic_indicator())

        


    """MALI INTRODUCTION"""

    mali_data = MaliData(service_type='bank')

    bank_agencies_mali = BankAgencies(
        mali_data.get_agency_counts(),
        mali_data.get_department_mapping(),
        mali_data.get_coordinates()
    )

    geographic_data_mali = GeographicData(mali_data.get_coordinates())

    neighbors_mali = geographic_data_mali.compute_neighbors(distance_threshold=THRESHOLD)

    '''Indicator 1 : ISIBF score'''

    # Calculate ISIBF values
    indicator_calculator_mali = IndicatorCalculator(bank_agencies_mali.get_agency_counts(), neighbors_mali, mali_data.get_adult_population(), alpha=ALPHA_MALI, threshold=THRESHOLD, department_mapping=mali_data.get_department_mapping(), area=mali_data.get_area())
    isibf_departments_mali = indicator_calculator_mali.calculate_isibf2()


    # Normalization by country
    isibf_departments_mali_norm = format_scores(normalize_scores(isibf_departments_mali))
    isibf_regions_mali_norm = format_scores(mean_scores(normalize_scores(isibf_departments_mali), mali_data.get_department_mapping()))

    # Global normalization and formatting
    isibf_regions_mali = mean_scores(isibf_departments_mali, mali_data.get_department_mapping())

    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries
    map_visualizer_mali_regions = MapVisualizer(mali, isibf_regions_mali_norm, label="ISIBF", type="région", lat=17.5, lon=-4.5, zoom=5.5, country="mali")
    #map_visualizer_mali_regions.create_choropleth()
    map_visualizer_mali_regions.create_leaflet()

    map_visualizer_mali = MapVisualizer(mali2, isibf_departments_mali_norm, label="ISIBF", type="cercle", lat=17.5, lon=-4.5, zoom=5.5, country="mali")
    #map_visualizer_mali.create_choropleth()
    map_visualizer_mali.create_leaflet()

    '''Indicator 2 : Demographic indicator'''

    # demographic indicators
    demo_indicator_mali=round(indicator_calculator_mali.demographic_indicator_country())

    '''Indicator 3 : Geographic indicator'''

    # geographic indicators
    geo_indicator_mali = round(indicator_calculator_mali.geographic_indicator())




    """BURKINA FASO INTRODUCTION"""

    burkina_data = BurkinaDepartmentData(service_type='bank')

    bank_agencies_burkina = BankAgencies(
        burkina_data.get_agency_counts(),
        burkina_data.get_department_mapping(),
        burkina_data.get_coordinates()
    )

    geographic_data_burkina = GeographicData(burkina_data.get_coordinates())

    neighbors_burkina = geographic_data_burkina.compute_neighbors(distance_threshold=THRESHOLD)

    '''Indicator 1 : ISIBF score'''

    # Calculate ISIBF values
    indicator_calculator_burkina = IndicatorCalculator(bank_agencies_burkina.get_agency_counts(), neighbors_burkina, burkina_data.get_adult_population(), alpha=ALPHA_BURKINA, threshold=THRESHOLD, department_mapping=burkina_data.get_department_mapping(), area=burkina_data.get_area())
    isibf_departments_burkina = indicator_calculator_burkina.calculate_isibf2()

    # Normalization by country
    isibf_departments_burkina_norm = format_scores(normalize_scores(isibf_departments_burkina))
    isibf_regions_burkina_norm = format_scores(mean_scores(normalize_scores(isibf_departments_burkina), burkina_data.get_department_mapping()))

    # Global normalization and formatting
    isibf_regions_burkina = mean_scores(isibf_departments_burkina, burkina_data.get_department_mapping())

    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries
    map_visualizer_burkina_regions = MapVisualizer(burkina, isibf_regions_burkina_norm, label="ISIBF", type="région", lat=12.5, lon=-1.5, zoom=5.5, country="burkina")
    #map_visualizer_burkina_regions.create_choropleth()
    map_visualizer_burkina_regions.create_leaflet()

    map_visualizer_burkina = MapVisualizer(burkina2, isibf_departments_burkina_norm, label="ISIBF", type="province", lat=12.5, lon=-1.5, zoom=5.5, country="burkina")
    #map_visualizer_burkina.create_choropleth()
    map_visualizer_burkina.create_leaflet()

    '''Indicator 2 : Demographic indicator'''

    # demographic indicators
    demo_indicator_burkina=round(indicator_calculator_burkina.demographic_indicator_country())

    '''Indicator 3 : Geographic indicator'''

    # geographic indicators
    geo_indicator_burkina = round(indicator_calculator_burkina.geographic_indicator())




    
    """SENEGAL INTRODUCTION"""

    senegal_data = SenegalDepartmentData(service_type='bank')

    bank_agencies_senegal = BankAgencies(
        senegal_data.get_agency_counts(),
        senegal_data.get_department_mapping(),
        senegal_data.get_coordinates()
    )

    geographic_data_senegal = GeographicData(senegal_data.get_coordinates())

    neighbors_senegal = geographic_data_senegal.compute_neighbors(distance_threshold=THRESHOLD)

    '''Indicator 1 : ISIBF score'''

    # Calculate ISIBF values
    indicator_calculator_senegal = IndicatorCalculator(bank_agencies_senegal.get_agency_counts(), neighbors_senegal, senegal_data.get_adult_population(), alpha=ALPHA_SENEGAL, threshold=THRESHOLD, department_mapping=senegal_data.get_department_mapping(), area=senegal_data.get_area())
    isibf_departments_senegal = indicator_calculator_senegal.calculate_isibf2()

    # Normalization by country
    isibf_departments_senegal_norm = format_scores(normalize_scores(isibf_departments_senegal))

    isibf_regions_senegal_norm = format_scores(mean_scores(normalize_scores(isibf_departments_senegal), senegal_data.get_department_mapping()))

    # Global normalization and formatting
    isibf_regions_senegal = mean_scores(isibf_departments_senegal, senegal_data.get_department_mapping())

    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries
    map_visualizer_senegal_regions = MapVisualizer(senegal, isibf_regions_senegal_norm, label="ISIBF", type="région", lat=14.5, lon=-15, zoom=5.5, country="senegal")
    #map_visualizer_senegal_regions.create_choropleth()
    map_visualizer_senegal_regions.create_leaflet()

    map_visualizer_senegal = MapVisualizer(senegal2, isibf_departments_senegal_norm, label="ISIBF", type="département", lat=14.5, lon=-15, zoom=5.5, country="senegal")
    #map_visualizer_senegal.create_choropleth()
    map_visualizer_senegal.create_leaflet()

    '''Indicator 2 : Demographic indicator'''

    # demographic indicators
    demo_indicator_senegal=round(indicator_calculator_senegal.demographic_indicator_country())

    '''Indicator 3 : Geographic indicator'''

    # geographic indicators
    geo_indicator_senegal = round(indicator_calculator_senegal.geographic_indicator())




    
    """MAPS COMBINED VISUALIZATION"""

    # Normalization by countries
    isibf_combined_norm = {**isibf_regions_benin_norm, **isibf_regions_togo_norm, **isibf_regions_civ_norm, **isibf_regions_mali_norm, **isibf_regions_burkina_norm, **isibf_regions_niger_norm, **isibf_regions_guinee_norm, **isibf_regions_senegal_norm}

    #print(isibf_regions_mali_norm, isibf_niger_norm)
    # Global normalization and formatting
    isibf_combined_department_norm = {**isibf_departments_benin_norm, **isibf_departments_togo_norm, **isibf_departments_civ_norm, **isibf_departments_mali_norm, **isibf_departments_burkina_norm, **isibf_departments_niger_norm, **isibf_departments_guinee_norm, **isibf_departments_senegal_norm}
    
    map_visualizer_combined_departments = MapVisualizer(combined2, isibf_combined_department_norm, label="ISIBF", type="département", lat=15, lon=-4, zoom=5.45, country="combined")
    #map_visualizer_combined_departments.create_choropleth()
    map_visualizer_combined_departments.create_leaflet()
    



    # Maps for normalization by countries
    map_visualizer_combined = MapVisualizer(combined, isibf_combined_norm, label="ISIBF", type="région", lat=15, lon=-4, zoom=5.45, country="combined")
    #map_visualizer_combined.create_choropleth()
    map_visualizer_combined.create_leaflet()

    mean_scores_countries={
        "Bénin": mean(isibf_regions_benin),
        "Togo": mean(isibf_regions_togo),
        "Côte d\'Ivoire": mean(isibf_regions_civ),
        "Mali": mean(isibf_regions_mali),
        "Burkina Faso": mean(isibf_regions_burkina),
        "Niger": mean(isibf_regions_niger),
        "Guinée Bissau": mean(isibf_regions_guinee),
        "Sénégal": mean(isibf_regions_senegal)
    }

    map_visualizer_combined2 = MapVisualizer(combined0, mean_scores_countries, label="ISIBF", type="pays", lat=15, lon=-4, zoom=5.45, country="combined")
    #map_visualizer_combined2.create_choropleth()
    map_visualizer_combined2.create_leaflet()


    """CHARTS COMBINED VISUALIZATION"""

    # demographic indicators
    demo_indicator_combined = {
        "Bénin": demo_indicator_benin,
        "Burkina Faso": demo_indicator_burkina,
        "Côte d\'Ivoire": demo_indicator_civ,
        "Guinée Bissau": demo_indicator_guinee,
        "Mali": demo_indicator_mali,
        "Niger": demo_indicator_niger,
        "Sénégal": demo_indicator_senegal,
        "Togo": demo_indicator_togo,
    }



    chart_visualizer_combined = ChartVisualizer(demo_indicator_combined, label="demographic_indicator", title="100 000 habitants")
    #chart_visualizer_combined.create_bar_chart()

    
    geo_indicator_combined = {
        "Bénin": geo_indicator_benin,
        "Burkina Faso": geo_indicator_burkina,
        "Côte d\'Ivoire": geo_indicator_civ,
        "Guinée Bissau": geo_indicator_guinee,
        "Mali": geo_indicator_mali,
        "Niger": geo_indicator_niger,
        "Sénégal": geo_indicator_senegal,
        "Togo": geo_indicator_togo,
    }

    chart_visualizer_combined_geo = ChartVisualizer(geo_indicator_combined, label="geographic_indicator", title="10 000 km²")
    chart_visualizer_combined_geo.create_bar_chart()



   
if __name__ == "__main__":
    main()
