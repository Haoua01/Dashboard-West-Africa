from bank_agencies import BankAgencies
from geographic_data import GeographicData
from indicator_calculator import IndicatorCalculator
from data.benin_data import BeninData
from data.togo_data import TogoData
from data.civ_data import CIVData
from map_visualizer import MapVisualizer
from chart_visualizer import ChartVisualizer
from utils import normalize_scores, format_scores, round_scores

# Import necessary Python libraries
import geopandas as gpd
import pandas as pd

# Constants
THRESHOLD = 200  # Distance threshold for neighbors
ALPHA_BENIN = 1.04  # Alpha value for ISIBF calculation in Benin
ALPHA_TOGO = 1.009  # Alpha value for ISIBF calculation in Togo
ALPHA_CIV = 1.02  # Alpha value for ISIBF calculation in Côte d'Ivoire
REF_INHABITANTS_BENIN = 100000  # Reference number of inhabitants for Benin
REF_INHABITANTS_TOGO = 70000  # Reference number of inhabitants for Togo
REF_INHABITANTS_CIV = 350000  # Reference number of inhabitants for Côte d'Ivoire

def load_shapefiles():
    benin = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/ben_adm_1m_salb_2019_shapes') #change path once folder updated on GitHub
    togo = gpd.read_file('/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Dashboard/Shapefiles_togo') #change path once folder updated on GitHub
    civ = gpd.read_file("/Users/haouabenaliabbo/Downloads/202303_OSM2IGEO_COTE_D_IVOIRE_SHP_WGS84_4326/H_OSM_ADMINISTRATIF/DISTRICT.shp") #change path once folder updated on GitHub

    # Add columns for country names
    togo['ADM1_REF'] = 'Togo'
    civ['ID'] = "Côte d'Ivoire"

    # Rename columns for consistency
    benin = benin.rename(columns={'adm1_name': 'admin1Name'})
    benin = benin.rename(columns={'adm0_name': 'country'})
    togo = togo.rename(columns={'ADM1_FR': 'admin1Name'})
    togo = togo.rename(columns={'ADM1_REF': 'country'})
    civ = civ.rename(columns={'NOM': 'admin1Name'})
    civ = civ.rename(columns={'ID': 'country'})

    # Rename regions with common names to avoid conflicts
    benin['admin1Name'] = benin['admin1Name'].replace('Oueme', 'Ouémé')
    togo['admin1Name'] = togo['admin1Name'].replace('Savanes', 'Savanes_Togo')
    civ['admin1Name'] = civ['admin1Name'].replace('Savanes', 'Savanes_CIV')

    # Fusion shapefiles for combined maps
    combined = pd.concat([benin, togo, civ], ignore_index=True)

    return benin, togo, civ, combined

def main():

    '''Generic functions and initialisation'''
    # Load geographic data
    benin, togo, civ, combined = load_shapefiles()

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
    isibf_combined_norm = {**isibf_benin_norm, **isibf_togo_norm, **isibf_civ_norm}

    # Global normalization and formatting
    isibf_all = {**isibf_benin, **isibf_togo, **isibf_civ}
    isibf_all_norm = format_scores(normalize_scores(isibf_all))


    '''Map visualization for ISIBF score'''

    # Maps for normalization by countries
    map_visualizer_benin = MapVisualizer(benin, isibf_benin_norm, label="ISIBF", lat=9.5, lon=2.3, country="benin")
    map_visualizer_benin.create_choropleth()

    map_visualizer_togo = MapVisualizer(togo, isibf_togo_norm, label="ISIBF", lat=8.6, lon=0.9, country="togo")
    map_visualizer_togo.create_choropleth()

    map_visualizer_civ = MapVisualizer(civ, isibf_civ_norm, label="ISIBF", lat=7.5, lon=-4.0, country="civ")
    map_visualizer_civ.create_choropleth()

    map_visualizer_combined = MapVisualizer(combined, isibf_combined_norm, label="ISIBF", lat=8.5, lon=-2, country="combined")
    map_visualizer_combined.create_choropleth()


    # Maps for global normalization
    map_visualizer_benin = MapVisualizer(benin, isibf_all_norm, label="ISIBF2", lat=9.5, lon=2.3, country="benin")
    map_visualizer_benin.create_choropleth()

    map_visualizer_togo = MapVisualizer(togo, isibf_all_norm, label="ISIBF2", lat=8.6, lon=0.9, country="togo")
    map_visualizer_togo.create_choropleth()

    map_visualizer_civ = MapVisualizer(civ, isibf_all_norm, label="ISIBF2", lat=7.5, lon=-4.0, country="civ")
    map_visualizer_civ.create_choropleth()

    map_visualizer_combined = MapVisualizer(combined, isibf_all_norm, label="ISIBF2", lat=8.5, lon=-2, country="combined")
    map_visualizer_combined.create_choropleth()


    """"Indicator 2 : Demographic indicator"""
    # Calculate demographic indicators
    demo_indicator_benin = round_scores(indicator_calculator_benin.demographic_indicator(REF_INHABITANTS_BENIN))
    demo_indicator_togo = round_scores(indicator_calculator_togo.demographic_indicator(REF_INHABITANTS_TOGO))
    demo_indicator_civ = round_scores(indicator_calculator_civ.demographic_indicator(REF_INHABITANTS_CIV))
    demo_indicator_combined = {**demo_indicator_benin, **demo_indicator_togo, **demo_indicator_civ}
    print(demo_indicator_combined)

    # Create and save bar charts
    chart_visualizer_benin = ChartVisualizer(demo_indicator_benin, title=f"Nombres d'agences pour {REF_INHABITANTS_BENIN} habitants par ville", label="demographic_indicator", country="benin")
    chart_visualizer_benin.create_bar_chart()

    chart_visualizer_togo = ChartVisualizer(demo_indicator_togo, title=f"Nombres d'agences pour {REF_INHABITANTS_TOGO} habitants par ville", label="demographic_indicator",  country="togo")
    chart_visualizer_togo.create_bar_chart()

    chart_visualizer_civ = ChartVisualizer(demo_indicator_civ, title=f"Nombres d'agences pour {REF_INHABITANTS_CIV} habitants par ville", label="demographic_indicator", country="civ")
    chart_visualizer_civ.create_bar_chart()

    chart_visualizer_combined = ChartVisualizer(demo_indicator_combined, title=f"Nombres d'agences pour combiné", label="demographic_indicator", country="combined")
    chart_visualizer_combined.create_bar_chart()
    

if __name__ == "__main__":
    main()
