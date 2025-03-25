import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

# Load commune data
df = pd.read_csv('data_all_clean_communes_latest_v6_geoc.csv')
df['Equipments']=df['Total_bran']+df['Total_ATMs']
df['GCD_km']=df["Population"]/df["Area"]


# Load the neighbors.json data
with open('neighbors_great_circle2.json', 'r') as f:
    neighbors_data = json.load(f)


points = np.arange(0, 101, 10)

df['Equipments'] = df['Total_bran'] + df['Total_ATMs']

def calculate_access(df, neighbor_data, points):
    communes_with_atm = df[df['Equipments'] > 0]
    communes_without_atm = df[df['Equipments'] == 0]
    
    total_area = df['Area'].sum()
    total_population = df['Population'].sum()
    total_communes = df['ADM3_FR'].tolist()
    
    area_with_access = communes_with_atm['Area'].sum()
    population_with_access = communes_with_atm['Population'].sum()
    
    access_percentages = []
    population_percentages = []
    
    for distance_threshold in points:
        communes_with_access = set(communes_with_atm['ADM3_FR'].tolist())
        area_covered = area_with_access
        population_covered = population_with_access

        for commune in communes_without_atm['ADM3_FR']:
            for neighbor, distance in neighbor_data.get(commune, {}).items():
                if distance <= distance_threshold and neighbor in communes_with_access:
                    communes_with_access.add(commune)
                    population_covered += communes_without_atm[communes_without_atm['ADM3_FR'] == commune]['Population'].values[0]
                    break

        access_percentage = (len(communes_with_access) / len(total_communes)) * 100
        area_percentage = (area_covered / total_area) * 100
        population_percentage = (population_covered / total_population) * 100
        
        access_percentages.append(access_percentage)
        population_percentages.append(population_percentage)
    
    return access_percentages, population_percentages

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

for country_name, code in country_dict2.items():
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



barWidth = 0.26

bars1 = np.round(demographic_access,1)
bars2 = np.round(geographic_access,1)
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]

i = 0

plt.bar(r1, bars1, color=colors_orange, width=barWidth, edgecolor='grey', label='EB pour 100 000 habitants')
#plt.bar(r2, bars2, color=colors_green, width=barWidth, edgecolor='grey', label='EB pour 10 000 km²')

xtick_labels = list(country_dict1.keys())
xtick_labels[-1] = r"$\bf{" + xtick_labels[-1] + "}$"



#display percentages on bars
for j in range(len(bars1)):
    plt.xticks([r for r in range(len(bars2))], xtick_labels)
    plt.text(r1[j], bars1[j], bars1[j], ha='center', va='bottom')
    #plt.text(r2[j], bars2[j], round(bars2[j],2), ha='center', va='bottom')
    plt.xlabel('Pays', labelpad=15) 
    plt.ylabel("Nombre d'équipements bancaires (EB)", labelpad=20)
    plt.legend()
plt.show()

