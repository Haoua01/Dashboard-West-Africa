from bank_agencies import BankAgencies
from geographic_data import GeographicData
from indicator_calculator import IndicatorCalculator
from data.benin_data import BeninData
from data.togo_data import TogoData
from data.civ_data import CIVData
from map_visualizer import MapVisualizer
from chart_visualizer import ChartVisualizer
from utils import normalize_scores, format_scores, round_scores, mean_scores
from data.civ_department_data import CIVDepartmentData
from data.mali_data import MaliData

# Import necessary Python libraries
import geopandas as gpd
import pandas as pd

# Constants
THRESHOLD = 200  # Distance threshold for neighbors
ALPHA_BENIN = 1.04  # Alpha value for ISIBF calculation in Benin
ALPHA_TOGO = 1.009  # Alpha value for ISIBF calculation in Togo
ALPHA_CIV = 1.02  # Alpha value for ISIBF calculation in Côte d'Ivoire
ALPHA_MALI = 1.04  # Alpha value for ISIBF calculation in Mali
ALPHA_ALL = max(ALPHA_BENIN, ALPHA_TOGO, ALPHA_CIV, ALPHA_MALI)  # Maximum alpha value for global normalization
REF_INHABITANTS = 100000  # Reference number of inhabitants for demographic indicator


def load_shapefiles():
    benin = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/ben_adm_1m_salb_2019_shapes') #change path once folder updated on GitHub
    togo = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/Shapefiles_togo') #change path once folder updated on GitHub
    civ = gpd.read_file("/Users/haouabenaliabbo/Downloads/202303_OSM2IGEO_COTE_D_IVOIRE_SHP_WGS84_4326/H_OSM_ADMINISTRATIF/DISTRICT.shp") #change path once folder updated on GitHub
    mali = gpd.read_file('/Users/haouabenaliabbo/Downloads/mali_adm_ab_shp/mli_admbnda_adm1_1m_gov_20211220.shp')

    # Add columns for country names
    togo['ADM1_REF'] = 'Togo'
    civ['country'] = "Côte d'Ivoire"
    mali['country'] = "Mali"

    # Rename columns for consistency
    benin = benin.rename(columns={'adm1_name': 'admin1Name'})
    benin = benin.rename(columns={'adm0_name': 'country'})
    togo = togo.rename(columns={'ADM1_FR': 'admin1Name'})
    togo = togo.rename(columns={'ADM1_REF': 'country'})
    civ = civ.rename(columns={'NOM': 'admin1Name'})
    mali = mali.rename(columns={'ADM1_FR': 'admin1Name'})

    # Rename regions with common names to avoid conflicts
    benin['admin1Name'] = benin['admin1Name'].replace('Oueme', 'Ouémé')
    togo['admin1Name'] = togo['admin1Name'].replace('Savanes', 'Savanes_Togo')
    civ['admin1Name'] = civ['admin1Name'].replace('Savanes', 'Savanes_CIV')

    # Fusion shapefiles for combined maps
    combined = pd.concat([benin, togo, civ, mali], ignore_index=True)
    #print(combined[['admin1Name', 'country']])

    return benin, togo, civ, mali, combined

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

    return civ, mali 


# Load geographic data
benin, togo, civ, mali, combined = load_shapefiles()
civ2, mali2 = load_department_shapefiles()  



def main():

    '''Generic functions and initialisation'''

    # Initialize data classes
    benin_data = BeninData(service_type='bank')
    togo_data = TogoData(service_type='bank')
    civ_data = CIVData(service_type='bank')

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
    bank_agencies_civ = BankAgencies(
        civ_data.get_agency_counts(),
        civ_data.get_department_mapping(),
        civ_data.get_coordinates()
    )

    # Create instances of GeographicData for neighbor calculations
    geographic_data_benin = GeographicData(benin_data.get_coordinates())
    geographic_data_togo = GeographicData(togo_data.get_coordinates())
    geographic_data_civ = GeographicData(civ_data.get_coordinates())

    # Compute neighbors
    neighbors_benin = geographic_data_benin.compute_neighbors(distance_threshold=THRESHOLD)
    neighbors_togo = geographic_data_togo.compute_neighbors(distance_threshold=THRESHOLD)
    neighbors_civ = geographic_data_civ.compute_neighbors(distance_threshold=THRESHOLD)

    '''Indicator 1 : ISIBF score'''

    # Calculate ISIBF values
    indicator_calculator_benin = IndicatorCalculator(bank_agencies_benin.get_agency_counts(), neighbors_benin, benin_data.get_adult_population(), alpha=ALPHA_BENIN, threshold=THRESHOLD, department_mapping=benin_data.get_department_mapping())
    isibf_benin = indicator_calculator_benin.calculate_isibf()

    indicator_calculator_togo = IndicatorCalculator(bank_agencies_togo.get_agency_counts(), neighbors_togo, togo_data.get_adult_population(), alpha=ALPHA_TOGO, threshold=THRESHOLD, department_mapping=togo_data.get_department_mapping())
    isibf_togo = indicator_calculator_togo.calculate_isibf()

    indicator_calculator_civ = IndicatorCalculator(bank_agencies_civ.get_agency_counts(), neighbors_civ, civ_data.get_adult_population(), alpha=ALPHA_CIV, threshold=THRESHOLD, department_mapping=civ_data.get_department_mapping())
    isibf_civ = indicator_calculator_civ.calculate_isibf()


    # Normalize for each countries and format
    isibf_benin_norm = format_scores(normalize_scores(isibf_benin))
    isibf_togo_norm = format_scores(normalize_scores(isibf_togo))
    isibf_civ_norm = format_scores(normalize_scores(isibf_civ))


    '''Map visualization for ISIBF score

    # Maps for normalization by countries
    map_visualizer_benin = MapVisualizer(benin, isibf_benin_norm, label="ISIBF", type="régions", lat=9.5, lon=2.3, country="benin")
    map_visualizer_benin.create_choropleth()

    map_visualizer_togo = MapVisualizer(togo, isibf_togo_norm, label="ISIBF", type="régions", lat=8.6, lon=0.9, country="togo")
    map_visualizer_togo.create_choropleth()

    map_visualizer_civ = MapVisualizer(civ, isibf_civ_norm, label="ISIBF", type="districts", lat=7.5, lon=-5.5, country="civ")
    map_visualizer_civ.create_choropleth()


    # Maps for global normalization
    map_visualizer_benin = MapVisualizer(benin, isibf_all_norm, label="ISIBF2", type="régions", lat=9.5, lon=2.3, country="benin")
    map_visualizer_benin.create_choropleth()

    map_visualizer_togo = MapVisualizer(togo, isibf_all_norm, label="ISIBF2",  type="régions", lat=8.6, lon=0.9, country="togo")
    map_visualizer_togo.create_choropleth()

    map_visualizer_civ = MapVisualizer(civ, isibf_all_norm, label="ISIBF2",  type="districts", lat=7.5, lon=-5.5, country="civ")
    #map_visualizer_civ.create_choropleth()

    '''

    """"Indicator 2 : Demographic indicator"""
    # Calculate demographic indicators
    demo_indicator_benin = round_scores(indicator_calculator_benin.demographic_indicator(REF_INHABITANTS))
    demo_indicator_togo = round_scores(indicator_calculator_togo.demographic_indicator(REF_INHABITANTS))
    demo_indicator_civ = round_scores(indicator_calculator_civ.demographic_indicator(REF_INHABITANTS))
    demo_indicator_combined = {**demo_indicator_benin, **demo_indicator_togo, **demo_indicator_civ}
    #print(demo_indicator_combined)

    # calculate spatial demographic indicators
    spatial_demo_indicator_benin = round_scores(indicator_calculator_benin.spatial_demographic_indicator(REF_INHABITANTS, THRESHOLD))
    spatial_demo_indicator_togo = round_scores(indicator_calculator_togo.spatial_demographic_indicator(REF_INHABITANTS, THRESHOLD))
    spatial_demo_indicator_civ = round_scores(indicator_calculator_civ.spatial_demographic_indicator(REF_INHABITANTS, THRESHOLD))
    spatial_demo_indicator_combined = {**spatial_demo_indicator_benin, **spatial_demo_indicator_togo, **spatial_demo_indicator_civ}
    #print(spatial_demo_indicator_combined)

    """Charts for demographic indicators
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

    '''COTE D'IVOIRE ADJUSTMENTS : Generic functions and initialisation'''

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
    indicator_calculator_civ2 = IndicatorCalculator(bank_agencies_civ2.get_agency_counts(), neighbors_civ2, civ_data2.get_adult_population(), alpha=ALPHA_CIV, threshold=THRESHOLD, department_mapping=civ_data2.get_department_mapping())
    isibf_departments_civ = indicator_calculator_civ2.calculate_isibf2()
    # Global normalization and formatting
    isibf_regions_civ = mean_scores(isibf_departments_civ, civ_data2.get_department_mapping())


    # Normalization by countries
    isibf_departments_civ_norm = format_scores(normalize_scores(isibf_departments_civ))
    isibf_regions_civ_norm = format_scores(mean_scores(normalize_scores(isibf_departments_civ), civ_data2.get_department_mapping()))


    



    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries
    map_visualizer_civ = MapVisualizer(civ2, isibf_departments_civ_norm, label="ISIBF", type="départements", lat=7.5, lon=-5.5, country="civ")
    #map_visualizer_civ.create_choropleth()

    map_visualizer_civ_regions = MapVisualizer(civ, isibf_regions_civ_norm, label="ISIBF", type="districts", lat=7.5, lon=-5.5, country="civ")
    #map_visualizer_civ_regions.create_choropleth()



    '''Indicator 2 : Demographic indicator'''

    # demographic indicators

    demo_indicator_civ_regions=format_scores(mean_scores(indicator_calculator_civ2.demographic_indicator(REF_INHABITANTS), civ_data2.get_department_mapping()))

    chart_visualizer_civ = ChartVisualizer(demo_indicator_civ_regions, type="districts", label="demographic_indicator", country="civ")
    #chart_visualizer_civ.create_bar_chart()

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
    indicator_calculator_mali = IndicatorCalculator(bank_agencies_mali.get_agency_counts(), neighbors_mali, mali_data.get_adult_population(), alpha=ALPHA_MALI, threshold=THRESHOLD, department_mapping=mali_data.get_department_mapping())
    isibf_departments_mali = indicator_calculator_mali.calculate_isibf2()
    print(isibf_departments_mali)


    # Normalization by country
    isibf_departments_mali_norm = format_scores(normalize_scores(isibf_departments_mali))
    isibf_regions_mali_norm = format_scores(mean_scores(normalize_scores(isibf_departments_mali), mali_data.get_department_mapping()))

    # Global normalization and formatting
    isibf_regions_mali = mean_scores(isibf_departments_mali, mali_data.get_department_mapping())

    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries
    map_visualizer_mali_regions = MapVisualizer(mali, isibf_regions_mali_norm, label="ISIBF", type="régions", lat=17.5, lon=-4.5, country="mali")
    #map_visualizer_mali_regions.create_choropleth()

    map_visualizer_mali = MapVisualizer(mali2, isibf_departments_mali_norm, label="ISIBF", type="cercles", lat=17.5, lon=-4.5, country="mali")
    #map_visualizer_mali.create_choropleth()
    
    """MAPS COMBINED VISUALIZATION"""

    # Normalization by countries
    isibf_combined_norm = {**isibf_benin_norm, **isibf_togo_norm, **isibf_regions_civ_norm, **isibf_regions_mali_norm}


    # Global normalization and formatting
    isibf_all = {**isibf_benin, **isibf_togo, **isibf_regions_civ, **isibf_regions_mali}
    print(isibf_all)
    isibf_all_norm = format_scores(normalize_scores(isibf_all))

    # Maps for normalization by countries
    map_visualizer_combined = MapVisualizer(combined, isibf_combined_norm, label="ISIBF", type="régions", lat=8.5, lon=-2, country="combined")
    map_visualizer_combined.create_choropleth()

    # Maps for global normalization
    map_visualizer_combined = MapVisualizer(combined, isibf_all_norm, label="ISIBF2", type="régions", lat=8.5, lon=-2, country="combined")
    map_visualizer_combined.create_choropleth()

    

   
if __name__ == "__main__":
    main()
