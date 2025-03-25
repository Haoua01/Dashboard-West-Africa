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

points = np.arange(0, 101, 10)

df['Equipments'] = df['Total_bran'] + df['Total_ATMs']

import pandas as pd

# Initialize the data list
data = []

def calculate_access(df, neighbor_data, points):
    communes_with_equipments = df[df['Equipments'] > 0]
    communes_without_equipments = df[df['Equipments'] == 0]
    
    total_area = df['Area'].sum()
    total_population = df['Population'].sum()
    total_communes = df['ADM3_FR'].tolist()
    
    area_with_access = communes_with_equipments['Area'].sum()
    population_with_access = communes_with_equipments['Population'].sum()
    
    access_percentages = []
    area_percentages = []
    population_percentages = []
    
    for distance_threshold in points:
        communes_with_access = set(communes_with_equipments['ADM3_FR'].tolist())
        area_covered = area_with_access
        population_covered = population_with_access
        uncovered_communes = []  # List to store communes that remain uncovered

        for commune in communes_without_equipments['ADM3_FR']:
            covered = False
            for neighbor, distance in neighbor_data.get(commune, {}).items():
                if distance <= distance_threshold and neighbor in communes_with_access:
                    communes_with_access.add(commune)
                    area_covered += communes_without_equipments[communes_without_equipments['ADM3_FR'] == commune]['Area'].values[0]
                    population_covered += communes_without_equipments[communes_without_equipments['ADM3_FR'] == commune]['Population'].values[0]
                    covered = True 
                    break

            # If a commune is still uncovered after checking all neighbors, append it to the list
            if not covered:
                uncovered_communes.append(commune)

        # Calculate the percentages
        access_percentage = (len(communes_with_access) / len(total_communes)) * 100
        area_percentage = (area_covered / total_area) * 100
        population_percentage = (population_covered / total_population) * 100

        if population_percentage>=95: 
            print(f"Country: {df['Country'].iloc[0]}")
            
            # Save to CSV
            data.append({
                'Pays': df['Country'].iloc[0],
                'Seuil (km)': distance_threshold,
                '% Communes': np.round(access_percentage, 1),
                '% Superficie': np.round(area_percentage, 1),
                '% Population': np.round(population_percentage, 1),
                'Nombre communes exclues': len(uncovered_communes)
            })
            break
        
        access_percentages.append(access_percentage)
        area_percentages.append(area_percentage)
        population_percentages.append(population_percentage)
    
    return access_percentages, area_percentages, population_percentages




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

countries = {
    "au \ Bénin": ["benin", "Communes"],
    "au \ Burkina \ Faso": ["burkina", "Communes"],
    "au \ Mali": ["mali", "Communes"],
    "au \ Niger": ["niger", "Communes"],
    "en \ Côte \ d'Ivoire": ["civ", "Sous-préfectures"],
    "en \ Guinée-Bissau": ["guinee", "Secteurs"],
    "au \ Sénégal": ["senegal", "Arrondissements"],
    "au \ Togo": ["togo", "Communes"]
}

for country_name, code in countries.items():
    access, area, pop = calculate_access(df[df['Country'] == code[0]], neighbors_data.get(code[0], {}), points)
df = pd.DataFrame(data)
df.to_csv('population_95_len.csv', index=False)


# Initialisation
distance_access = {}
distance_area = {}
distance_pop = {}

# Calcul par pays
for country in df['Country'].unique():
    count = df[df['Country'] == country]
    access, area, pop = calculate_access(count, neighbors_data.get(country, {}), points)
    distance_access[country] = access
    distance_area[country] = area
    distance_pop[country] = pop

# Moyennes UEMOA
all_access = defaultdict(list)
all_area = defaultdict(list)
all_pop = defaultdict(list)

for country in df['Country'].unique():
    for i, d in enumerate(points):
        all_access[d].append(distance_access[country][i])
        all_area[d].append(distance_area[country][i])
        all_pop[d].append(distance_pop[country][i])

distance_access['UEMOA'] = [sum(all_access[d]) / len(all_access[d]) for d in points]
distance_area['UEMOA'] = [sum(all_area[d]) / len(all_area[d]) for d in points]
distance_pop['UEMOA'] = [sum(all_pop[d]) / len(all_pop[d]) for d in points]

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(16, 12))
axs = axs.flatten()
i = 0

for country_name, code in countries.items():
    country = code[0]
    admin_level = code[1]

    axs[i].plot(points, distance_access[country], marker='o', linestyle='-', color='C1', label=f'{admin_level} $\mathbf{{{country_name}}}$')
    axs[i].plot(points, distance_access['UEMOA'], linestyle='--', color='C1', label='Moyenne communes UEMOA')
    axs[i].plot(points, distance_area[country], marker='s', linestyle='-', color='C2', label=f'Superficie')
    axs[i].plot(points, distance_area['UEMOA'], linestyle='--', color='C2', label='Moyenne superficie UEMOA')
    axs[i].plot(points, distance_pop[country], marker='^', linestyle='-', color='C0', label=f'Population')
    axs[i].plot(points, distance_pop['UEMOA'], linestyle='--', color='C0', label='Moyenne population UEMOA')
    axs[i].set_xlabel("Distance (km)")
    axs[i].set_ylabel("Pourcentage (%)")
    axs[i].grid(True)
    axs[i].legend()
    i += 1

plt.tight_layout()
plt.show()