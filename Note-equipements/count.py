import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

# Load commune data
df = pd.read_csv('data_all_clean_communes_latest_v7_geoc.csv')


categories = ['0', '1-2', '3-20', '21-50', '>50']


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

# Flatten the axes array to make it easier to iterate
fig, axs = plt.subplots(2, 2, figsize=(16, 12))  
axs = axs.flatten()

i=0

def calculate_access(df, country_dict):
    all_bars1 = []
    all_bars2 = []
    for country_name, code in country_dict.items():

        country = code[0]
        admin_level = code[1]

        count = df[df['Country'] == country]

        group_0=count[count['Total_bran']==0] #a remplacer par Total_bran pour les DAB
        pop_0=group_0['Population'].sum()

        group_1_3=count[(count['Total_bran']>=1) & (count['Total_bran']<=2)]
        pop_1_3=group_1_3['Population'].sum()

        group_4_20=count[(count['Total_bran']>=3) & (count['Total_bran']<=20)]
        pop_4_20=group_4_20['Population'].sum()

        group_21_100=count[(count['Total_bran']>=21) & (count['Total_bran']<=50)]
        pop_21_100=group_21_100['Population'].sum()

        group_100=count[count['Total_bran']>50]
        pop_100=group_100['Population'].sum()

        total_communes = count['ADM3_FR'].tolist()
        total_population = count['Population'].sum()

        percentage_0_communes = (len(group_0) / len(total_communes)) * 100
        percentage_0_population = (pop_0 / total_population) * 100

        percentage_1_3_communes = (len(group_1_3) / len(total_communes)) * 100
        percentage_1_3_population = (pop_1_3 / total_population) * 100

        percentage_4_20_communes = (len(group_4_20) / len(total_communes)) * 100
        percentage_4_20_population = (pop_4_20 / total_population) * 100

        percentage_21_100_communes = (len(group_21_100) / len(total_communes)) * 100
        percentage_21_100_population = (pop_21_100 / total_population) * 100

        percentage_100_communes = (len(group_100) / len(total_communes)) * 100
        percentage_100_population = (pop_100 / total_population) * 100

        barWidth = 0.26

        bars1 = [percentage_0_communes, percentage_1_3_communes, percentage_4_20_communes, percentage_21_100_communes, percentage_100_communes]
        bars2 = [percentage_0_population, percentage_1_3_population, percentage_4_20_population, percentage_21_100_population, percentage_100_population]

        all_bars1.append(bars1)
        all_bars2.append(bars2)
    return all_bars1, all_bars2

barWidth = 0.15

all_bars1, all_bars2 = calculate_access(df, countries)
avg_bars1 = np.mean(all_bars1, axis=0)
avg_bars2 = np.mean(all_bars2, axis=0)

fig, axs = plt.subplots(2, 2, figsize=(14, 10))
axs = axs.flatten()

all_bars1, all_bars2 = calculate_access(df, country_dict1)
for k, (country_name, (country_code, admin_level)) in enumerate(country_dict1.items()):
    bars1 = all_bars1[k]
    bars2 = all_bars2[k]
    r1 = np.arange(len(categories))
    r2 = [x + barWidth for x in r1]
    r3 = [x + 2*barWidth for x in r1]
    r4 = [x + 3*barWidth for x in r1]

    axs[k].bar(r1, avg_bars1, color='C0', width=barWidth, edgecolor='black', label=f'Moyenne UEMOA', alpha=0.3, hatch='//')
    axs[k].bar(r2, avg_bars2, color='C1', width=barWidth, edgecolor='black', label='Moyenne UEMOA', alpha=0.3, hatch='//')
    axs[k].bar(r1, bars1, color='C0', width=barWidth, edgecolor='grey', label=f'% {admin_level} $\mathbf{{{country_name}}}$')
    axs[k].bar(r2, bars2, color='C1', width=barWidth, edgecolor='grey', label='% Population')

    for j in range(len(categories)):
        # Valeurs pays (toujours affichées)
        axs[k].text(r1[j], bars1[j]/2, f"{bars1[j]:.1f}", ha='center', va='bottom', fontsize=8, fontweight='bold')
        axs[k].text(r2[j], bars2[j]/2, f"{bars2[j]:.1f}", ha='center', va='bottom', fontsize=8, fontweight='bold')

        # Moyenne UEMOA : affichée seulement si elle dépasse visuellement
        #if avg_bars1[j] > bars1[j]:
            #axs[k].text(r1[j], avg_bars1[j], f"{avg_bars1[j]:.1f}", ha='center', va='bottom', fontsize=8, color='black')

        #if avg_bars2[j] > bars2[j]:
            #axs[k].text(r2[j], avg_bars2[j], f"{avg_bars2[j]:.1f}", ha='center', va='bottom', fontsize=8, color='black')

    axs[k].set_xlabel("Nombre d'agences bancaires")
    axs[k].set_ylabel("Pourcentage (%)")
    axs[k].set_xticks([r + 0.5*barWidth for r in range(len(categories))])
    axs[k].set_xticklabels(categories)
    axs[k].legend()

plt.tight_layout()
plt.show()



