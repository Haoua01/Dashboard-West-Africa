import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

# Load commune data
df = pd.read_csv('data_all_clean_communes_latest_v3.csv')

# Load the neighbors.json data
with open('neighbors_great_circle2.json', 'r') as f:
    neighbors_data = json.load(f)


points = np.linspace(0, 100, 100)

df['Equipments']=df['Total_bran']+df['Total_ATMs']

def calculate_access(df, neighbor_data, points):
    # Extract communes that already have branches
    communes_with_branch = df[df['Total_ATMs'] > 0]
    
    # Extract communes without branches
    total_communes = df['ADM3_FR'].tolist()
    communes_without_branch = df[df['Total_ATMs'] == 0]
    
    # Initialize variables for area and population percentages
    total_area = df['Area'].sum()  # Total area of all communes
    total_population = df['Population'].sum()  # Total population of all communes
    
    area_with_access = communes_with_branch['Area'].sum()  # Area covered by communes with branches
    population_with_access = communes_with_branch['Population'].sum()  # Population covered by communes with branches
    
    access_percentages = []
    area_percentages = []
    population_percentages = []
    
    uncovered_communes = []  # To store communes that remain uncovered
    
    for distance_threshold in points:  # Adjust distance range as necessary
        communes_with_access = set(communes_with_branch['ADM3_FR'].tolist())
        area_covered = area_with_access
        population_covered = population_with_access
        
        # Loop through communes without branches to check if they are within the catchment area
        for commune in communes_without_branch['ADM3_FR']:
            covered = False
            for neighbor, distance in neighbor_data.get(commune, {}).items():
                if distance <= distance_threshold and neighbor in communes_with_access:
                    communes_with_access.add(commune)
                    area_covered += communes_without_branch[communes_without_branch['ADM3_FR'] == commune]['Area'].values[0]
                    population_covered += communes_without_branch[communes_without_branch['ADM3_FR'] == commune]['Population'].values[0]
                    covered = True
                    break
            

        
        # Compute percentage of communes, area, and population covered
        access_percentage = (len(communes_with_access) / len(total_communes)) * 100
        area_percentage = (area_covered / total_area) * 100
        population_percentage = (population_covered / total_population) * 100
        
        access_percentages.append(access_percentage)
        area_percentages.append(area_percentage)
        population_percentages.append(population_percentage)
    
    # Convert uncovered communes to a DataFrame and save as CSV
    uncovered_df = pd.DataFrame(uncovered_communes)
    uncovered_df.to_csv('uncovered_communes_dab.csv', index=False)
    
    return access_percentages, area_percentages, population_percentages

# Get the unique country codes
country_code = df['Country'].unique()

# Create subplots for each country

# Flatten the axes array to make it easier to iterate
fig, axs = plt.subplots(2, 2, figsize=(16, 12))  
axs = axs.flatten()

country_dict1 = {
    "au Bénin": ["benin", "Communes"],
    "au Burkina Faso": ["burkina", "Communes"],
    "au Mali": ["mali", "Communes"],
    "au Niger": ["niger", "Communes"],
}
country_dict2 = {
    "en Côte d'Ivoire": ["civ", "Sous-préfectures"],
    #"en Guinée-Bissau": ["guinee", "Secteurs"],
    "au Sénégal": ["senegal", "Arrondissements"],
    "au Togo": ["togo", "Communes"]
}



i = 0
for dict in [country_dict2]:
    # Loop over each country and plot its percentage data in different subplots
    for country_name, code in dict.items():
        country = code[0]
        admin_level = code[1]
        count = df[df['Country'] == country]
        access_percentages, area_percentages, population_percentages = calculate_access(count, neighbors_data.get(country, {}), points)
        
 
        # Plot the data on the current subplot
        axs[i].plot(points, access_percentages, marker='o', markersize=5, linestyle='-', label=f'{admin_level}')
        axs[i].plot(points, population_percentages, marker='o', markersize=5, linestyle='-', label='Population')
        axs[i].plot(points, area_percentages, marker='o', markersize=5, linestyle='-', label='Superficie')
        
        axs[i].set_title(f'Accès aux DAB {country_name}')
        axs[i].set_xlabel('Distance (km)')
        axs[i].set_ylabel('Pourcentage (%)')
        axs[i].legend()
        axs[i].grid(True)
        #axs[i].set_ylim(bottom=0)  # Ensure the y-axis starts at 0
        i += 1


    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()


