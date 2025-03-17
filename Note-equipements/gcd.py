import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

# Load commune data
df = pd.read_csv('data_all_clean_communes_latest_v4.csv')

df['Equipments']=df['Total_bran']+df['Total_ATMs']

# Load the neighbors.json data
with open('neighbors_great_circle2.json', 'r') as f:
    neighbors_data = json.load(f)

density_mapping = {
    1: "Le rural à habitat très dispersé",
    2: "Le rural à habitat dispersé",
    3: "Les bourgs ruraux",
    4: "Les petites villes",
    5: "Les ceintures urbaines",
    6: "Les centres urbains intermédiaires",
    7: "Les grands centres urbains"
}


def calculate_access(df, neighbor_data):
    distances_by_level = {level: {'sum': 0, 'count': 0} for level in df['GCD'].unique()}
    
    # Extract communes that already have branches
    communes_with_branch = df[df['Equipments'] > 0]
    communes_without_branch = df[df['Equipments'] == 0]
    
    communes_with_access = set(communes_with_branch['ADM3_FR'].tolist())

    for commune in communes_with_branch['ADM3_FR']:
        gcd = df[df['ADM3_FR'] == commune]['GCD'].values[0]
        distances_by_level[gcd]['count'] += 1  # Just increment the count
    
    # Loop through communes without branches and check if they are within the catchment area
    for commune in communes_without_branch['ADM3_FR']:
        for neighbor, distance in neighbor_data.get(commune, {}).items():
            if neighbor in communes_with_access:
                communes_with_access.add(commune)
                gcd1 = df[df['ADM3_FR'] == commune]['GCD'].values[0]
                distances_by_level[gcd1]['sum'] += distance
                distances_by_level[gcd1]['count'] += 1
                break
    
    # Compute the mean distance for each level
    for level, data in distances_by_level.items():
        print(level, data)
        if data['count'] > 0:
            data['mean'] = data['sum'] / data['count']
        else:
            data['mean'] = 0

    access = [data['mean'] for level, data in distances_by_level.items()]
    
    return access


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

density_mapping_multi_line = [
    "Rural à\nhabitat très\n dispersé",
    "Rural à\nhabitat \n dispersé",
    "Bourgs\nruraux",
    "Petites\nvilles",
    "Ceintures\nurbaines",
    "Centres\nurbains\nintermédiaires",
    "Grands\ncentres \nurbains"
]

i = 0
for dict in [country_dict1]:
    # Loop over each country and plot its percentage data in different subplots
    for country_name, code in dict.items():
        country = code[0]
        admin_level = code[1]
        count = df[df['Country'] == country]
        bars1= calculate_access(count, neighbors_data.get(country, {}))
        r1 = np.arange(len(bars1))
        barWidth = 0.26
        axs[i].bar(r1, bars1, color='C0', width=barWidth, edgecolor='grey')
        axs[i].set_xlabel('Grille communale de densité')
        axs[i].set_ylabel('Distance moyenne (km)')
        axs[i].set_title(f'Accès aux agences bancaires {country_name}')
        axs[i].set_xticks(r1)  # Ensure the ticks match the bars
        axs[i].set_xticklabels(density_mapping_multi_line) 


    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()


