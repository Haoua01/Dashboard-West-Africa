from bank_agencies import BankAgencies
from geographic_data import GeographicData
from indicator_calculator import IndicatorCalculator
from data.benin_data import BeninData
from data.togo_data import TogoData
#from data.civ_data import CIVData
from map_visualizer import MapVisualizer
from chart_visualizer import ChartVisualizer
from utils import normalize_scores, format_scores, round_scores, mean_scores, mean, alpha_values, log_transform
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
from shapefile import Shapefile
from data.civ_commune_data import CIVCommuneData


# Import necessary Python libraries
import geopandas as gpd
import pandas as pd
import numpy as np
import requests
import os
from dotenv import load_dotenv
import time

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_GEOCODING_API_KEY")

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


#alpha_burkina_test = {'Balé': 0.0487, 'Banwa': 0.0567, 'Kossi': 0.1924, 'Mouhoun': 0.094, 'Nayala': 0.0629, 'Sourou': 0.1103, 'Comoé': 0.3178, 'Léraba': 0.0877, 'Kadiogo': 1.0, 'Boulgou': 0.1027, 'Koulpélogo': 0.0381, 'Kouritenga': 0.0359, 'Bam': 0.0721, 'Namentenga': 0.0696, 'Sanmatenga': 0.2356, 'Boulkiemdé': 0.5391, 'Sanguié': 0.192, 'Sissili': 0.0878, 'Ziro': 0.3411, 'Bazèga': 0.3336, 'Nahouri': 0.0467, 'Zoundwéogo': 0.054, 'Gnagna': 0.0759, 'Gourma': 0.1369, 'Komondjari': 0.0346, 'Kompienga': 0.1311, 'Tapoa': 0.4593, 'Houet': 0.3362, 'Kénédougou': 0.2546, 'Tuy': 0.0738, 'Loroum': 0.1808, 'Passoré': 0.1739, 'Yatenga': 0.3311, 'Zondoma': 0.035, 'Ganzourgou': 0.0538, 'Kourwéogo': 0.1838, 'Oubritenga': 0.0898, 'Oudalan': 0.2027, 'Séno': 0.1476, 'Soum': 0.2289, 'Yagha': 0.0303, 'Bougouriba': 0.0, 'Ioba': 0.0154, 'Noumbiel': 0.0053, 'Poni': 0.0796}



#define the alpha value for each country as constants
ALPHA_BENIN = alpha_countries['Benin']
ALPHA_TOGO = alpha_countries['Togo']
ALPHA_CIV = alpha_countries['Côte d\'Ivoire']
ALPHA_MALI = alpha_countries['Mali']
ALPHA_BURKINA = alpha_countries['Burkina Faso']
ALPHA_NIGER =  alpha_countries['Niger']
ALPHA_GUINEE = alpha_countries['Guinée Bissau']
ALPHA_SENEGAL = alpha_countries['Sénégal']


#print('Access to infrastructures:', alpha_countries)
"""
def load_country_shapefiles():
    benin = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Benin_Shapefiles/ben_admbnda_adm0_1m_salb_20190816.shp')
    civ = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/CIV_Shapefiles/civ_admbnda_adm0_cntig_20180706')
    togo = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Togo_Shapefiles/tgo_admbnda_adm0_inseed_itos_20210107.shp')
    mali = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Mali_Shapefiles/mli_admbnda_adm0_1m_gov_20211220.shp')
    burkina = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Burkina_Shapefiles/geoBoundaries-BFA-ADM0-all/geoBoundaries-BFA-ADM0_simplified.shp')
    niger = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Niger_Shapefiles/NER_admbnda_adm0_IGNN_20230720.shp')
    guinee = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Guinee_Shapefiles/gnb_admbnda_adm0_1m_salb_20210609.shp')
    senegal = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Senegal_Shapefiles/sen_admbnda_adm0_anat_20240520.shp')

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

    tchad = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Tchad_Shapefiles/tcd_admbnda_adm0_ocha/tcd_admbnda_adm0_ocha.shp')
    tchad['country']='Tchad'



    combined = pd.concat([benin, togo, civ, mali, burkina, niger, guinee, senegal], ignore_index=True)
    combined_with_td = pd.concat([benin, togo, civ, mali, burkina, niger, guinee, senegal, tchad], ignore_index=True)

    combined_with_borders = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/QGIS/uemoa_countries_borders.shp')

    combined_with_borders_with_td = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/uemoa_and_tchad_borders.shp')

    combined_with_td.to_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/uemoa_countries_and_tchad.shp')

    return combined, combined_with_borders, combined_with_borders_with_td

def load_shapefiles():
    benin = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Benin_Shapefiles/ben_admbnda_adm1_1m_salb_20190816.shp')
    civ = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/CIV_Shapefiles/civ_admbnda_adm1_cntig_ocha_itos_20180706')
    togo = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Togo_Shapefiles/tgo_admbnda_adm1_inseed_itos_20210107.shp')
    mali = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Mali_Shapefiles/mli_admbnda_adm1_1m_gov_20211220.shp')
    burkina = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Burkina_Shapefiles/geoBoundaries-BFA-ADM1-all/geoBoundaries-BFA-ADM1_simplified.shp')
    niger = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Niger_Shapefiles/NER_admbnda_adm1_IGNN_20230720.shp')
    guinee = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Guinee_Shapefiles/gnb_admbnda_adm1_1m_salb_20210609.shp')
    senegal = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Senegal_Shapefiles/sen_admbnda_adm1_anat_20240520.shp')
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
    benin = benin.rename(columns={'ADM1_FR': 'admin1Name'})
    #benin = benin.rename(columns={'adm0_name': 'country'})
    togo = togo.rename(columns={'ADM1_FR': 'admin1Name'})
    #togo = togo.rename(columns={'ADM1_REF': 'country'})
    civ = civ.rename(columns={'ADM0_FR': 'admin1Name'})
    mali = mali.rename(columns={'ADM1_FR': 'admin1Name'})
    burkina = burkina.rename(columns={'shapeName': 'admin1Name'})
    niger = niger.rename(columns={'ADM1_FR': 'admin1Name'})
    guinee = guinee.rename(columns={'ADM1_FR': 'admin1Name'})
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

    benin = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Benin_Shapefiles/ben_admbnda_adm2_1m_salb_20190816.shp')
    civ = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/CIV_Shapefiles/civ_admbnda_adm2_cntig_ocha_itos_20180706')
    togo = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Togo_Shapefiles/tgo_admbnda_adm2_inseed_itos_20210107.shp')
    mali = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Mali_Shapefiles/mli_admbnda_adm2_1m_gov_20211220.shp')
    burkina = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Burkina_Shapefiles/geoBoundaries-BFA-ADM2-all/geoBoundaries-BFA-ADM2_simplified.shp')
    niger = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Niger_Shapefiles/NER_admbnda_adm2_IGNN_20230720.shp')
    guinee = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Guinee_Shapefiles/gnb_admbnda_adm2_1m_salb_20210609.shp')
    senegal = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Senegal_Shapefiles/sen_admbnda_adm2_anat_20240520.shp')
    
    #civ= gpd.read_file('/Users/haouabenaliabbo/Downloads/civ_admbnda_adm2_cntig_ocha_itos_20180706 (2)/civ_admbnda_adm2_cntig_ocha_itos_20180706.shp')
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

    #mali= gpd.read_file('/Users/haouabenaliabbo/Downloads/mali_adm_ab_shp/mli_admbnda_adm2_1m_gov_20211220.shp')
    mali= mali.rename(columns={'ADM2_FR': 'admin1Name'})
    mali['admin1Name'] = mali['admin1Name'].replace('Bafoulabe', 'Bafoulabé')

    #burkina=gpd.read_file('/Users/haouabenaliabbo/Downloads/geoBoundaries-BFA-ADM2-all/geoBoundaries-BFA-ADM2_simplified.shp')
    burkina = burkina.rename(columns={'shapeName': 'admin1Name'})
    burkina['admin1Name']=burkina['admin1Name'].replace('Komonjdjari', 'Komondjari')
    #burkina['admin1Name']=burkina['admin1Name'].replace('Kouritenga', 'Kourittenga')
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

    #benin = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/ben_adm_1m_salb_2019_shapes/ben_admbnda_adm2_1m_salb_20190816.shp')
    benin = benin.rename(columns={'ADM3_FR': 'admin1Name'})
    benin['country'] = 'Bénin'
    commune_replacements_benin = {'Djakotome': 'Djakotomey', 'Dogbo-tota': 'Dogbo-Tota', 'Kopargo': 'Copargo', 'Banikoara': 'Banikoara', 'Gogounou': 'Gogounou', 'Kandi': 'Kandi', 'Karimama': 'Karimama', 'Malanville': 'Malanville', 'Segbana': 'Segbana', 'Kerou': 'Kérou', 'Kobli': 'Cobly', 'Kouande': 'Kouandé', 'Materi': 'Matéri', 'Natitingou': 'Natitingou', 'Pehunco': 'Péhunco', 'Tanguieta': 'Tanguiéta', 'Allada': 'Allada', 'Kpomasse': 'Kpomassè', 'Ouidah': 'Ouidah', 'Toffo': 'Toffo', 'Ze': 'Zè', 'Bembereke': 'Bembéréké', 'Kalale': 'Kalalé', 'Nikki': 'Nikki', 'Parakou': 'Parakou', 'Perere': 'Pèrèrè', 'Sinende': 'Sinendé', 'Tchaourou': 'Tchaourou', 'Bante': 'Bantè', 'Glazoue': 'Glazoué', 'Ouesse': 'Ouèssè', 'Savalou': 'Savalou', 'Save': 'Savè', 'Aplahoue': 'Aplahoué', 'Klouekanme': 'Klouékanmè', 'Lalo': 'Lalo', 'Toviklin': 'Toviklin', 'Bassila': 'Bassila', 'Djougou': 'Djougou', 'Ouake': 'Ouaké', 'Cotonou': 'Cotonou', 'Athieme': 'Athiémé', 'Bopa': 'Bopa', 'Come': 'Comè', 'Houeyogbe': 'Houéyogbé', 'Lokossa': 'Lokossa', 'Adjohoun': 'Adjohoun', 'Avrankou': 'Avrankou', 'Bonou': 'Bonou', 'Dangbo': 'Dangbo', 'Ifangni': 'Ifangni', 'Ketou': 'Kétou', 'Pobe': 'Pobè', 'Sakete': 'Sakété', 'Abomey': 'Abomey', 'Agbangnizoun': 'Agbangnizoun', 'Bohicon': 'Bohicon', 'Cove': 'Covè', 'Djidja': 'Djidja', 'Ouinhi': 'Ouinhi', 'Zogbodomey': 'Zogbodomey', 'Aguegues': 'Aguégués', 'Boukoumbe': 'Boukoumbé', 'Toukountouna': 'Toucountouna', 'Abomey-calavi': 'Abomey-Calavi', 'So-ava': 'Sô-Ava', 'Tori-bossito': 'Tori-Bossito', 'Ndali': 'N\'Dali', 'Dassa': 'Dassa-Zoumé', 'Grand-popo': 'Grand-Popo', 'Adjara': 'Adjarra', 'Akpro-misserete': 'Akpro-Missérété', 'Porto-novo': 'Porto-Novo', 'Seme-kpodji': 'Sèmè-Kpodji', 'Adja-ouere': 'Adja-Ouèrè', 'Za-kpota': 'Za-Kpota', 'Zangnanado': 'Zagnanado'}


    # Replace names in 'admin1Name' column based on the above mappings
    for old_name, new_name in commune_replacements_benin.items():
        benin['admin1Name'] = benin['admin1Name'].replace(old_name, new_name)

    #togo = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/Shapefiles_togo/tgo_admbnda_adm2_inseed_itos_20210107.shp')
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

    #guinee = gpd.read_file('/Users/haouabenaliabbo/Downloads/gnb_admbnda_1m_salb_20210609_shp/gnb_admbnda_adm2_1m_salb_20210609.shp')
    guinee = guinee.rename(columns={'ADM3_FR': 'admin1Name'})
    guinee['country'] = 'Guinée Bissau'
    secteurs_mapping = {'Gabu': 'Gabú', 'Gamamudo/Ganadu': 'Gamamundo', 'Cacheu/Calequisse': 'Cacheu', 'Caio': 'Caió', 'Boe': 'Boé', 'Gabu': 'Gabú', 'Bissora': 'Bissorã', 'Mansoa': 'Mansôa', 'Catio': 'Catió', 'Sector Autonomo de Bissau': 'Bissau', 'Prabis': 'Prábis', 'Quinhamel': 'Quinhámel', 'Galomaro/Cosse':'Galomaro'}
    for old_name, new_name in secteurs_mapping.items():
        guinee['admin1Name'] = guinee['admin1Name'].replace(old_name, new_name)

    #niger=gpd.read_file('/Users/haouabenaliabbo/Downloads/ner_adm_ignn_20230720_ab_shp/NER_admbnda_adm2_IGNN_20230720.shp')
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
    

    #senegal=gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Senegal_Shapefiles/sen_admbnda_adm2_anat_20240520.shp')
    senegal.rename(columns={'ADM2_FR': 'admin1Name'}, inplace=True)
    senegal['country'] = 'Sénégal'

    combined = pd.concat([benin, togo, civ, mali, burkina, niger, guinee, senegal], ignore_index=True)
    #combined.to_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/uemoa_departments.shp')
    
    return civ, mali, burkina, benin, togo, guinee, niger, senegal, combined 


# Load geographic data
combined0, combined_with_borders, combined_td = load_country_shapefiles()
benin, togo, civ, mali, burkina, niger, guinee, senegal, combined = load_shapefiles()
civ2, mali2, burkina2, benin2, togo2, guinee2, niger2, senegal2, combined2 = load_department_shapefiles()  
geo_tchad = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/geo_tchad_isibf.shp')
tchad = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/Tchad_Shapefiles/tcd_admbnda_adm0_ocha/tcd_admbnda_adm0_ocha.shp')
tchad = tchad.rename(columns={'admin0Name':'admin1Name'})


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


    Indicator 2 : Demographic indicator
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



    BENIN ADJUSTMENTS

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

    print(isibf_regions_benin_norm)

    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries
    map_visualizer_benin2 = MapVisualizer(benin2, isibf_departments_benin_norm, label="ISIBF", type="commune", lat=9.5, lon=2.3, zoom=6.5, country="benin")
    #map_visualizer_benin2.create_choropleth()
    #map_visualizer_benin2.create_leaflet()

    map_visualizer_benin_regions = MapVisualizer(benin, isibf_regions_benin_norm, label="ISIBF", type="département", lat=9.5, lon=2.3, zoom=6.5, country="benin")
    #map_visualizer_benin_regions.create_choropleth()
    #map_visualizer_benin_regions.create_leaflet()

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
    #map_visualizer_togo2.create_leaflet()

    map_visualizer_togo_regions = MapVisualizer(togo, isibf_regions_togo_norm, label="ISIBF", type="région", lat=8.6, lon=0.9, zoom=6.5, country="togo")
    #map_visualizer_togo_regions.create_choropleth()
    #map_visualizer_togo_regions.create_leaflet()



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
    #map_visualizer_civ.create_leaflet()

    map_visualizer_civ_regions = MapVisualizer(civ, isibf_regions_civ_norm, label="ISIBF", type="district", lat=7.5, lon=-5.5, zoom=6.5, country="civ")
    #map_visualizer_civ_regions.create_choropleth()
    #map_visualizer_civ_regions.create_leaflet()




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
    #map_visualizer_guinee.create_leaflet()

    map_visualizer_guinee_regions = MapVisualizer(guinee, isibf_regions_guinee_norm, label="ISIBF", type="région", lat=11.8, lon=-15, zoom=7.5, country="guinee")
    #map_visualizer_guinee_regions.create_choropleth()
    #map_visualizer_guinee_regions.create_leaflet()

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
    #map_visualizer_niger.create_leaflet()

    map_visualizer_niger_regions = MapVisualizer(niger, isibf_regions_niger_norm, label="ISIBF", type="région", lat=17.6, lon=8.1, zoom=5.5, country="niger")
    #map_visualizer_niger_regions.create_choropleth()
    #map_visualizer_niger_regions.create_leaflet()

    '''Indicator 2 : Demographic indicator'''

    # demographic indicators
    demo_indicator_niger=round(indicator_calculator_niger2.demographic_indicator_country())

    '''Indicator 3 : Geographic indicator'''

    # geographic indicators
    geo_indicator_niger = round(indicator_calculator_niger2.geographic_indicator())

        


    MALI INTRODUCTION

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
    #map_visualizer_mali_regions.create_leaflet()

    map_visualizer_mali = MapVisualizer(mali2, isibf_departments_mali_norm, label="ISIBF", type="cercle", lat=17.5, lon=-4.5, zoom=5.5, country="mali")
    #map_visualizer_mali.create_choropleth()
    #map_visualizer_mali.create_leaflet()

    '''Indicator 2 : Demographic indicator'''

    # demographic indicators
    demo_indicator_mali=round(indicator_calculator_mali.demographic_indicator_country())

    '''Indicator 3 : Geographic indicator'''

    # geographic indicators
    geo_indicator_mali = round(indicator_calculator_mali.geographic_indicator())




    '''BURKINA FASO INTRODUCTION'''

    burkina_data = BurkinaDepartmentData(service_type='bank')

    bank_agencies_burkina = BankAgencies(
        burkina_data.get_agency_counts(),
        burkina_data.get_department_mapping(),
        burkina_data.get_coordinates()
    )

    geographic_data_burkina = GeographicData(burkina_data.get_coordinates())
    
    #neighbors_burkina = {'Balé': {'Mouhoun': 33, 'Sanguié': 18, 'Sissili': 4, 'Tuy': 7}, 'Bam': {'Loroum': 8, 'Passoré': 1, 'Sanmatenga': 18, 'Soum': 26, 'Yatenga': 4}, 'Banwa': {'Houet': 26, 'Kossi': 23, 'Mouhoun': 2}, 'Bazèga': {'Boulkiemdé': 35, 'Kadiogo': 277, 'Ziro': 63, 'Zoundwéogo': 13}, 'Bougouriba': {'Comoé': 5, 'Houet': 2, 'Ioba': 7, 'Poni': 6, 'Tuy': 1}, 'Boulgou': {'Gourma': 5, 'Koulpélogo': 18, 'Kouritenga': 9, 'Nahouri': 1, 'Zoundwéogo': 11}, 'Boulkiemdé': {'Bazèga': 35, 'Kadiogo': 38, 'Kourwéogo': 167, 'Passoré': 132, 'Sanguié': 159, 'Ziro': 37}, 'Comoé': {'Bougouriba': 5, 'Houet': 32, 'Kénédougou': 5, 'Léraba': 27, 'Poni': 22}, 'Ganzourgou': {'Kadiogo': 1, 'Kouritenga': 31, 'Namentenga': 5, 'Oubritenga': 11, 'Sanmatenga': 6}, 'Gnagna': {'Gourma': 6, 'Komondjari': 23, 'Kouritenga': 3, 'Namentenga': 31, 'Séno': 5, 'Yagha': 12}, 'Gourma': {'Boulgou': 5, 'Gnagna': 6, 'Komondjari': 26, 'Kompienga': 42, 'Koulpélogo': 3, 'Kouritenga': 13, 'Tapoa': 24}, 'Houet': {'Banwa': 26, 'Bougouriba': 2, 'Comoé': 32, 'Kénédougou': 64, 'Mouhoun': 1, 'Tuy': 24}, 'Ioba': {'Bougouriba': 7, 'Sissili': 4, 'Tuy': 9}, 'Kadiogo': {'Bazèga': 277, 'Boulkiemdé': 38, 'Ganzourgou': 1, 'Kourwéogo': 111, 'Oubritenga': 259}, 'Komondjari': {'Gnagna': 23, 'Gourma': 26, 'Yagha': 6}, 'Kompienga': {'Gourma': 42, 'Koulpélogo': 27, 'Tapoa': 47}, 'Kossi': {'Banwa': 23, 'Mouhoun': 3, 'Nayala': 1}, 'Koulpélogo': {'Boulgou': 18, 'Gourma': 3, 'Kompienga': 27}, 'Kouritenga': {'Boulgou': 9, 'Ganzourgou': 31, 'Gnagna': 3, 'Gourma': 13, 'Namentenga': 4}, 'Kourwéogo': {'Boulkiemdé': 167, 'Kadiogo': 111, 'Oubritenga': 8, 'Passoré': 62}, 'Kénédougou': {'Comoé': 5, 'Houet': 64, 'Léraba': 17}, 'Loroum': {'Bam': 8, 'Soum': 34, 'Yatenga': 55}, 'Léraba': {'Comoé': 27, 'Kénédougou': 17}, 'Mouhoun': {'Balé': 33, 'Banwa': 2, 'Houet': 1, 'Kossi': 3, 'Nayala': 3, 'Sanguié': 2, 'Tuy': 12}, 'Nahouri': {'Boulgou': 1, 'Sissili': 7, 'Ziro': 54, 'Zoundwéogo': 4}, 'Namentenga': {'Ganzourgou': 5, 'Gnagna': 31, 'Kouritenga': 4, 'Sanmatenga': 35, 'Soum': 1, 'Séno': 5}, 'Nayala': {'Kossi': 1, 'Mouhoun': 3, 'Passoré': 14, 'Sanguié': 46, 'Sourou': 23}, 'Noumbiel': {'Poni': 6}, 'Oubritenga': {'Ganzourgou': 11, 'Kadiogo': 259, 'Kourwéogo': 8, 'Passoré': 3, 'Sanmatenga': 9}, 'Oudalan': {'Soum': 39, 'Séno': 46}, 'Passoré': {'Bam': 1, 'Boulkiemdé': 132, 'Kourwéogo': 62, 'Nayala': 14, 'Oubritenga': 3, 'Sanguié': 41, 'Sanmatenga': 1, 'Sourou': 22, 'Yatenga': 8, 'Zondoma': 9}, 'Poni': {'Bougouriba': 6, 'Comoé': 22, 'Noumbiel': 6}, 'Sanguié': {'Balé': 18, 'Boulkiemdé': 159, 'Mouhoun': 2, 'Nayala': 46, 'Passoré': 41, 'Sissili': 3}, 'Sanmatenga': {'Bam': 18, 'Ganzourgou': 6, 'Namentenga': 35, 'Oubritenga': 9, 'Passoré': 1, 'Soum': 29}, 'Sissili': {'Balé': 4, 'Ioba': 4, 'Nahouri': 7, 'Sanguié': 3, 'Ziro': 45}, 'Soum': {'Bam': 26, 'Loroum': 34, 'Namentenga': 1, 'Oudalan': 39, 'Sanmatenga': 29, 'Séno': 5}, 'Sourou': {'Nayala': 23, 'Passoré': 22, 'Yatenga': 31, 'Zondoma': 37}, 'Séno': {'Gnagna': 5, 'Namentenga': 5, 'Oudalan': 46, 'Soum': 5, 'Yagha': 11}, 'Tapoa': {'Gourma': 24, 'Kompienga': 47}, 'Tuy': {'Balé': 7, 'Bougouriba': 1, 'Houet': 24, 'Ioba': 9, 'Mouhoun': 12}, 'Yagha': {'Gnagna': 12, 'Komondjari': 6, 'Séno': 11}, 'Yatenga': {'Bam': 4, 'Loroum': 55, 'Passoré': 8, 'Sourou': 31, 'Zondoma': 59}, 'Ziro': {'Bazèga': 63, 'Boulkiemdé': 37, 'Nahouri': 54, 'Sissili': 45}, 'Zondoma': {'Passoré': 9, 'Sourou': 37, 'Yatenga': 59}, 'Zoundwéogo': {'Bazèga': 13, 'Boulgou': 11, 'Nahouri': 4}}
    neighbors_burkina = geographic_data_burkina.compute_neighbors(distance_threshold=THRESHOLD)


    #print(neighbors_burkina.keys())
    #print a list of the keys of the dictionary neighbors_burkina

    '''Indicator 1 : ISIBF score'''

    # Calculate ISIBF values
    indicator_calculator_burkina = IndicatorCalculator(bank_agencies_burkina.get_agency_counts(), neighbors_burkina, burkina_data.get_adult_population(), alpha=ALPHA_BURKINA, threshold=THRESHOLD, department_mapping=burkina_data.get_department_mapping(), area=burkina_data.get_area())
    #indicator_calculator_burkina = IndicatorCalculator(bank_agencies_burkina.get_agency_counts(), neighbors_burkina, burkina_data.get_adult_population(), alpha=alpha_burkina_test, threshold=THRESHOLD, department_mapping=burkina_data.get_department_mapping(), area=burkina_data.get_area())
    isibf_departments_burkina = indicator_calculator_burkina.calculate_isibf2()

    #print(isibf_departments_burkina)

    # Normalization by country
    isibf_departments_burkina_norm = format_scores(normalize_scores(isibf_departments_burkina))
    isibf_regions_burkina_norm = format_scores(mean_scores(normalize_scores(isibf_departments_burkina), burkina_data.get_department_mapping()))

    # Global normalization and formatting
    isibf_regions_burkina = mean_scores(isibf_departments_burkina, burkina_data.get_department_mapping())

    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries
    map_visualizer_burkina_regions = MapVisualizer(burkina, isibf_regions_burkina_norm, label="ISIBF", type="région", lat=12.5, lon=-1.5, zoom=5.5, country="burkina")
    #map_visualizer_burkina_regions.create_choropleth()
    #map_visualizer_burkina_regions.create_leaflet()

    map_visualizer_burkina = MapVisualizer(burkina2, isibf_departments_burkina_norm, label="ISIBF", type="province", lat=12.5, lon=-1.5, zoom=5.5, country="burkina_test")
    #map_visualizer_burkina.create_choropleth()
    #map_visualizer_burkina.create_leaflet()

    

    '''Indicator 2 : Demographic indicator'''

    # demographic indicators
    demo_indicator_burkina=round(indicator_calculator_burkina.demographic_indicator_country())

    '''Indicator 3 : Geographic indicator'''

    # geographic indicators
    geo_indicator_burkina = round(indicator_calculator_burkina.geographic_indicator())




    
    '''SENEGAL INTRODUCTION'''

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
    #map_visualizer_senegal_regions.create_leaflet()

    map_visualizer_senegal = MapVisualizer(senegal2, isibf_departments_senegal_norm, label="ISIBF", type="département", lat=14.5, lon=-15, zoom=5.5, country="senegal")
    #map_visualizer_senegal.create_choropleth()
    #map_visualizer_senegal.create_leaflet()

    agences_senegal=bank_agencies_senegal.get_agency_counts()
    agences_senegal["Dakar"]=30
    map_visualizer_senegal_agences = MapVisualizer(senegal2, agences_senegal, label="Agences", type="département", lat=14.5, lon=-15, zoom=5.5, country="senegal")
    #map_visualizer_senegal_agences.create_leaflet()

    agences_senegal_regions_mean=mean_scores(agences_senegal, senegal_data.get_department_mapping())
    agences_senegal_regions_mean["Dakar"]=40
    map_visualizer_senegal_agences_regions = MapVisualizer(senegal, agences_senegal_regions_mean, label="Agences", type="région", lat=14.5, lon=-15, zoom=5.5, country="senegal")
    #map_visualizer_senegal_agences_regions.create_leaflet()

    #print(isibf_departments_senegal)


    '''Indicator 2 : Demographic indicator'''

    # demographic indicators
    demo_indicator_senegal=round(indicator_calculator_senegal.demographic_indicator_country())

    '''Indicator 3 : Geographic indicator'''

    # geographic indicators
    geo_indicator_senegal = round(indicator_calculator_senegal.geographic_indicator())




    
    '''MAPS COMBINED VISUALIZATION'''

    # Normalization by countries
    isibf_combined_norm = {**isibf_regions_benin_norm, **isibf_regions_togo_norm, **isibf_regions_civ_norm, **isibf_regions_mali_norm, **isibf_regions_burkina_norm, **isibf_regions_niger_norm, **isibf_regions_guinee_norm, **isibf_regions_senegal_norm}

    #print(isibf_regions_mali_norm, isibf_niger_norm)
    # Global normalization and formatting
    isibf_combined_department_norm = {**isibf_departments_benin_norm, **isibf_departments_togo_norm, **isibf_departments_civ_norm, **isibf_departments_mali_norm, **isibf_departments_burkina_norm, **isibf_departments_niger_norm, **isibf_departments_guinee_norm, **isibf_departments_senegal_norm}
    
    map_visualizer_combined_departments = MapVisualizer(combined2, isibf_combined_department_norm, label="ISIBF", type="département", lat=15, lon=-4, zoom=5.45, country="combined")
    #map_visualizer_combined_departments.create_choropleth()
    #map_visualizer_combined_departments.create_leaflet()

    map_visualizer_combined_departments_with_borders = MapVisualizer(combined2, isibf_combined_department_norm, label="ISIBF", type="département", lat=15, lon=-4, zoom=5.45, country="combined_with_borders")
    #map_visualizer_combined_departments.create_leaflet_combined(combined_with_borders)
    

    #print(isibf_combined_department_norm)

    # Maps for normalization by countries
    map_visualizer_combined = MapVisualizer(combined, isibf_combined_norm, label="ISIBF", type="région", lat=15, lon=-4, zoom=5.45, country="combined")
    #map_visualizer_combined.create_choropleth()
    #map_visualizer_combined.create_leaflet()

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

    '''
    print(isibf_departments_benin_norm)
    print(isibf_departments_togo_norm)
    print(isibf_departments_civ_norm)
    print(isibf_departments_mali_norm)
    print(isibf_departments_burkina_norm)
    print(isibf_departments_niger_norm)
    print(isibf_departments_guinee_norm)
    print(isibf_departments_senegal_norm)
    '''

    map_visualizer_combined2 = MapVisualizer(combined0, mean_scores_countries, label="ISIBF", type="pays", lat=15, lon=-4, zoom=5.45, country="combined")
    #map_visualizer_combined2.create_choropleth()
    #map_visualizer_combined2.create_leaflet()


    '''Maps combined with Tchad'''
    isibf_regions_tchad = {"N'Djamena": 5.508046127770763, 'Ouaddaï': 2.880630720837979, 'Logone Occidental': 3.20090286343193, 'Moyen-Chari': 2.070372131646714, 'Salamat': 1.0333818923122666, 'Mayo-Kebbi Ouest': 1.8456656640568787, 'Guéra': 1.6124302397549715, 'Logone Oriental': 2.1925175850448966, 'Mayo-Kebbi Est': 1.3154519302757048, 'Wadi Fira': 1.1886780683709246, 'Lac': 1.4134860104756544, 'Kanem': 1.2100934407210915, 'Barh-El-Gazel': 0.1515574028241689, 'Batha': 0.16474096485537132, 'Borkou': 0.0008791171251454577, 'Chari-Baguirmi': 0.3796319514328078, 'Ennedi Est': 0.008052993607244645, 'Ennedi Ouest': 0.00602662856352827, 'Hadjer-Lamis': 0.6708420408750191, 'Mandoul': 0.7325523720119412, 'Sila': 0.1004561899738713, 'Tandjilé': 0.9376712447389833, 'Tibesti': 0.0}

    mean_scores_tchad= mean(isibf_regions_tchad)
    tchad['ISIBF'] = mean_scores_tchad

    map_visualizer_combined_departments_with_td = MapVisualizer(combined2, isibf_combined_department_norm, label="ISIBF", type="département", lat=15, lon=1, zoom=5.45, country="combined_and_tchad")
    #map_visualizer_combined_departments_with_td.create_leaflet_combined_tchad(geo_tchad, combined_td)

    map_visualizer_combined_with_td = MapVisualizer(combined0, mean_scores_countries, label="ISIBF", type="country", lat=15, lon=1, zoom=5.45, country="combined_and_tchad")
    #map_visualizer_combined_with_td.create_leaflet_combined_tchad(tchad, combined_td)




    '''CHARTS COMBINED VISUALIZATION'''

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
    #chart_visualizer_combined_geo.create_bar_chart()


    #print(isibf_departments_burkina, isibf_departments_burkina_norm)

"""
shp_civ=Shapefile('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Econometrics/Note 2/data_all_clean_communes_latest_v2.shp')
civ3=shp_civ.load_shapefile()
civ3['country'] = "UEMOA"



def main2():
    # Initialize data classes
    civ_data3 = CIVCommuneData(service_type='bank', shp=shp_civ)

    # Initialize BankAgencies instances
    bank_agencies_civ3 = BankAgencies(
        civ_data3.get_agency_counts(),
        civ_data3.get_department_mapping(),
        civ_data3.get_coordinates()
    )


    geographic_data_civ3 = GeographicData(civ_data3.get_coordinates())

    neighbors_civ3 = geographic_data_civ3.compute_neighbors2(distance_threshold=100, countries=["benin", "burkina", "civ", "guinee", "mali", "niger", "senegal", "togo"])
    #count_civ=bank_agencies_civ3.get_agency_counts()
    """

    '''Indicator 1 : ISIBF score'''

    # Calculate ISIBF values

    indicator_calculator_civ3 = IndicatorCalculator(count_civ, neighbors_civ3, civ_data3.get_adult_population(), alpha=1.01, threshold=100, department_mapping=civ_data3.get_department_mapping(), area=civ_data3.get_area())
    isibf_communes_civ = indicator_calculator_civ3.calculate_isibf3()




    # Normalization by country
    isibf_communes_civ_norm = format_scores(normalize_scores(isibf_communes_civ))
 
    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries
    map_visualizer_civ_communes = MapVisualizer(civ3, isibf_communes_civ_norm, label="ISIBF", type="commune_log2_v3", lat=15, lon=-4, zoom=5.45, country="uemoa")
    map_visualizer_civ_communes.create_leaflet_commune()

    """
 

if __name__ == "__main__":
    main2()
