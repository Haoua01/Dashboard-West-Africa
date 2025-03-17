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

def calculate_access(df, neighbor_data, points):
    communes_with_branch = df[df['Total_bran'] > 0]
    communes_with_atm = df[df['Total_ATMs'] > 0]
    
    communes_without_branch = df[df['Total_bran'] == 0]
    communes_without_atm = df[df['Total_ATMs'] == 0]    
    
    total_population = df['Population'].sum()  # Total population of all communes
    population_branch_access = communes_with_branch['Population'].sum()  # Population covered by communes with branches
    population_atm_access = communes_with_atm['Population'].sum()  # Population covered by communes with branches
    
    access_branch_percentages = []
    access_atm_percentages = []
    
    uncovered_communes = []  # To store communes that remain uncovered
    
    for distance_threshold in points:  # Adjust distance range as necessary
        communes_with_branch_access = set(communes_with_branch['ADM3_FR'].tolist())
        communes_with_atm_access = set(communes_with_atm['ADM3_FR'].tolist())
        population_branch_covered = population_branch_access 
        population_atm_covered=population_atm_access
        
        # Loop through communes without branches to check if they are within the catchment area
        for commune in communes_without_branch['ADM3_FR']:
            covered = False
            for neighbor, distance in neighbor_data.get(commune, {}).items():
                if distance <= distance_threshold and neighbor in communes_with_branch_access:
                    communes_with_branch_access.add(commune)
                    population_branch_covered += communes_without_branch[communes_without_branch['ADM3_FR'] == commune]['Population'].values[0]
                    covered = True
                    break
            
            if not covered:
                uncovered_communes.append({
                    'Commune': commune,
                    'Country': communes_without_branch[communes_without_branch['ADM3_FR'] == commune]['Country'].values[0],
                    'Distance Threshold': distance_threshold,
                    'Area': communes_without_branch[communes_without_branch['ADM3_FR'] == commune]['Area'].values[0],
                    'Population_branch': communes_without_branch[communes_without_branch['ADM3_FR'] == commune]['Population'].values[0]
                })

        for commune in communes_without_atm['ADM3_FR']:
            covered = False
            for neighbor, distance in neighbor_data.get(commune, {}).items():
                if distance <= distance_threshold and neighbor in communes_with_atm_access:
                    communes_with_atm_access.add(commune)
                    population_atm_covered += communes_without_atm[communes_without_atm['ADM3_FR'] == commune]['Population'].values[0]
                    covered = True
                    break

        population_branch_percentage = (population_branch_covered / total_population) * 100
        population_atm_percentage = (population_atm_covered / total_population) * 100
        
        access_branch_percentages.append(population_branch_percentage)
        access_atm_percentages.append(population_atm_percentage)
    
    # Convert uncovered communes to a DataFrame and save as CSV
    uncovered_df = pd.DataFrame(uncovered_communes)
    uncovered_df.to_csv('uncovered_communes2_all.csv', index=False)
    
    return access_branch_percentages, access_atm_percentages

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
    "en Guinée-Bissau": ["guinee", "Secteurs"],
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
        access_branch_percentages, access_atm_percentages = calculate_access(count, neighbors_data.get(country, {}), points)
        
 
        # Plot the data on the current subplot
        axs[i].plot(points, access_branch_percentages, marker='o', markersize=5, linestyle='-', label=f'Agences bancaires', color='red')
        axs[i].plot(points, access_atm_percentages, marker='o', markersize=5, linestyle='-', label='DAB', color='blue')
        
        axs[i].set_title(f'Accès aux agences bancaires et DAB {country_name}')
        axs[i].set_xlabel('Distance (km)')
        axs[i].set_ylabel('% De la Population')
        axs[i].legend()
        axs[i].grid(True)
        #axs[i].set_ylim(bottom=0)  # Ensure the y-axis starts at 0
        i += 1


    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()


