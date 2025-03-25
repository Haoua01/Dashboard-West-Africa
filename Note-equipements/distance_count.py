import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Load commune data
df = pd.read_csv('data_all_clean_communes_latest_v6_geoc.csv')

# Load the neighbors.json data
with open('neighbors_great_circle4.json', 'r') as f:
    neighbors_data = json.load(f)

points = np.arange(0, 151, 5) 

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

        if population_atm_percentage>=80:
            print(f"Country: {df['Country'].iloc[0]}")
            print(f"Distance Threshold: {distance_threshold}")
            break
        
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
    "au \ Bénin": ["benin", "Communes"],
    "au \ Burkina \ Faso": ["burkina", "Communes"],
    "au \ Mali": ["mali", "Communes"],
    "au \ Niger": ["niger", "Communes"],
}
country_dict2 = {
    "en \ Côte \ d'Ivoire": ["civ", "Sous-préfectures"],
    "en \ Guinée-Bissau": ["guinee", "Secteurs"],
    "au \ Sénégal": ["senegal", "Arrondissements"],
    "au \ Togo": ["togo", "Communes"]
}

distance_branch = {}
distance_atm = {}
for country in df['Country'].unique():
    if country == 'guinee':
        continue
    count = df[df['Country'] == country]
    access_branch_percentages, access_atm_percentages = calculate_access(count, neighbors_data.get(country, {}), points)
    distance_branch[country]=access_branch_percentages
    distance_atm[country]=access_atm_percentages

for country in df['Country'].unique():
    count = df[df['Country'] == country]
    access_branch_percentages, access_atm_percentages = calculate_access(count, neighbors_data.get(country, {}), points)
    distance_branch[country]=access_branch_percentages


# Temp storage for lists of values per distance
all_branch = defaultdict(list)
all_atm = defaultdict(list)

# Aggregate values per distance
for country in df['Country'].unique():
    for i, d in enumerate(points):
        all_branch[d].append(distance_branch[country][i])
        if country=="guinee":
            continue
        all_atm[d].append(distance_atm[country][i])

# Compute mean per distance
distance_branch['UEMOA'] = [sum(all_branch[d])/len(all_branch[d]) for d in points]
distance_atm['UEMOA'] = [sum(all_atm[d])/len(all_atm[d]) for d in points]



i = 0
for country_name, code in country_dict1.items():
    country = code[0]
    admin_level = code[1]
    count = df[df['Country'] == country]
    if country=="guinee":
        access_branch_percentages = distance_branch[country]
        axs[i].plot(points, distance_branch[country], marker='o', markersize=5, linestyle='-', label=f'Agences $\mathbf{{{country_name}}}$', color='red')
        axs[i].plot(points, distance_branch['UEMOA'], marker='o', markersize=5, linestyle='--', label=f'Moyenne UEMOA', color='red')
        axs[i].set_xlabel('Temps de trajet (minutes)')
        axs[i].set_ylabel('% De la Population')
        axs[i].legend()
        axs[i].grid(True)
    else: 
        access_branch_percentages, access_atm_percentages = distance_branch[country], distance_atm[country]
        # Plot the data on the current subplot
        axs[i].plot(points, distance_branch[country], marker='o', markersize=5, linestyle='-', label=f'Agences $\mathbf{{{country_name}}}$', color='red')
        axs[i].plot(points, distance_branch['UEMOA'], marker='o', markersize=5, linestyle='--', label=f'Moyenne UEMOA', color='red')
        axs[i].plot(points, distance_atm[country],  marker='^', linestyle='-', label=f'DAB', color='blue')
        axs[i].plot(points, distance_atm['UEMOA'],  marker='^', linestyle='--', label='Moyenne UEMOA', color='blue')
        axs[i].set_xlabel('Distance (km)')
        axs[i].set_ylabel('% De la Population')
        axs[i].legend()
        axs[i].grid(True)
    #axs[i].set_ylim(bottom=0)  # Ensure the y-axis starts at 0
    i += 1


# Adjust layout and show the plot
plt.tight_layout()
plt.show()


