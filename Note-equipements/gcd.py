import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load commune data
df = pd.read_csv('data_all_clean_communes_latest_v7_geoc.csv')

# Load the neighbors.json data
with open('neighbors_great_circle2.json', 'r') as f:
    neighbors_data = json.load(f)

density_mapping = {
    1: "Rural",
    2: "Périurbain",
    3: "Urbain"
}

points = np.arange(0, 101, 10) 

def calculate_access(df, neighbor_data, points):
    access_branch_levels = []
    access_atm_levels = []
    for level in range(1, 4):
        df_level = df[df['GCD'] == level]

        distance_branch = 0
        distance_atm = 0

        communes_with_branch = df_level[df_level['Total_bran'] > 0]
        communes_with_atm = df_level[df_level['Total_ATMs'] > 0]

        communes_without_branch = df_level[df['Total_bran'] == 0]
        communes_without_atm = df_level[df['Total_ATMs'] == 0]

        count_branch=len(communes_with_branch)
        count_atm=len(communes_with_atm)

        for distance_threshold in points: 
            communes_with_branch_access = set(communes_with_branch['ADM3_FR'].tolist())
            communes_with_atm_access = set(communes_with_atm['ADM3_FR'].tolist())
            
            # Loop through communes without branches to check if they are within the catchment area
            for commune in communes_without_branch['ADM3_FR']:

                for neighbor, distance in neighbor_data.get(commune, {}).items():
                    if distance <= distance_threshold and neighbor in communes_with_branch_access:
                        communes_with_branch_access.add(commune) 
                        distance_branch += distance
                        count_branch += 1
                        break

            for commune in communes_without_atm['ADM3_FR']:
                for neighbor, distance in neighbor_data.get(commune, {}).items():
                    if distance <= distance_threshold and neighbor in communes_with_atm_access:
                        communes_with_atm_access.add(commune)
                        distance_atm += distance
                        count_atm += 1
                        break

            mean_distance_branch = distance_branch / count_branch
            mean_distance_atm = distance_atm / count_atm

        access_branch_levels.append(np.round(mean_distance_branch,1))
        access_atm_levels.append(np.round(mean_distance_atm,1))

    return access_branch_levels, access_atm_levels

categories = ['Rural', 'Périurbain', 'Urbain']


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


all_bars1 = []
all_bars2 = []
for country_name, code in countries.items():
    country = code[0]
    level = code[1]
    access_branch, access_atm = calculate_access(df, neighbors_data[country], points)
    all_bars1.append(access_branch)
    all_bars2.append(access_atm)


barWidth = 0.15

avg_bars1=[]
avg_bars2=[]
for level in range(1, 4):
    avg_bars1.append(np.mean([bars[level-1] for bars in all_bars1]))
    avg_bars2.append(np.mean([bars[level-1] for bars in all_bars2]))

fig, axs = plt.subplots(2, 2, figsize=(14, 10))
axs = axs.flatten()

for k, (country_name, (country_code, admin_level)) in enumerate(country_dict2.items()):
    bars1 = calculate_access(df, neighbors_data[country_code], points)[0]
    bars2 = calculate_access(df, neighbors_data[country_code], points)[1]
    r1 = np.arange(len(categories))
    r2 = [x + barWidth for x in r1]
    # 1. Moyenne UEMOA en fond (dessinées en premier)
    axs[k].bar(r1, avg_bars1, color='C3', width=barWidth, edgecolor='black', label='Moyenne UEMOA', alpha=0.3, hatch='//')
    axs[k].bar(r2, avg_bars2, color='C0', width=barWidth, edgecolor='black', label='Moyenne UEMOA', alpha=0.3, hatch='//')

    # 2. Barres du pays (dessinées ensuite, donc "par-dessus")
    axs[k].bar(r1, bars1, color='C3', width=barWidth, edgecolor='grey', label=f'Agences $\mathbf{{{country_name}}}$')
    axs[k].bar(r2, bars2, color='C0', width=barWidth, edgecolor='grey', label='DAB')


    for j in range(len(categories)):
        # Valeurs pays (toujours affichées)
        axs[k].text(r1[j], bars1[j], f"{bars1[j]:.1f}", ha='center', va='bottom', fontsize=8, fontweight='bold')
        axs[k].text(r2[j], bars2[j], f"{bars2[j]:.1f}", ha='center', va='bottom', fontsize=8, fontweight='bold')

        # Moyenne UEMOA : affichée seulement si elle dépasse visuellement
        if avg_bars1[j] > bars1[j]:
            axs[k].text(r1[j], avg_bars1[j], f"{avg_bars1[j]:.1f}", ha='center', va='bottom', fontsize=8, color='black')

        if avg_bars2[j] > bars2[j]:
            axs[k].text(r2[j], avg_bars2[j], f"{avg_bars2[j]:.1f}", ha='center', va='bottom', fontsize=8, color='black')


    axs[k].set_xlabel("Classe de densité")
    axs[k].set_ylabel("Distance moyenne (km)")
    axs[k].set_xticks([r+barWidth/2 for r in range(len(categories))])
    axs[k].set_xticklabels(categories)
    axs[k].legend()

plt.tight_layout()
plt.show()



