import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

# Load commune data
df = pd.read_csv('data_all_clean_communes_latest_v3.csv')

# Load the neighbors.json data
with open('neighbors_great_circle2.json', 'r') as f:
    neighbors_data = json.load(f)

df['Total_bran']=df['Total_bran']+df['Total_bran']


categories = ['0', '1-2', '3-20', '21-99', '>100']


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

# Flatten the axes array to make it easier to iterate
fig, axs = plt.subplots(2, 2, figsize=(16, 12))  
axs = axs.flatten()

i=0
for dict in [country_dict2]:
    for country_name, code in dict.items():

        country = code[0]
        admin_level = code[1]

        count = df[df['Country'] == country]

        group_0=count[count['Total_bran']==0]
        pop_0=group_0['Population'].sum()
        area_0=group_0['Area'].sum()

        group_1_3=count[(count['Total_bran']>=1) & (count['Total_bran']<=2)]
        pop_1_3=group_1_3['Population'].sum()
        area_1_3=group_1_3['Area'].sum()

        group_4_20=count[(count['Total_bran']>=3) & (count['Total_bran']<=20)]
        pop_4_20=group_4_20['Population'].sum()
        area_4_20=group_4_20['Area'].sum()

        group_20_99=count[(count['Total_bran']>=21) & (count['Total_bran']<=99)]
        pop_20_99=group_20_99['Population'].sum()
        area_20_99=group_20_99['Area'].sum()

        group_100=count[count['Total_bran']>=100]
        pop_100=group_100['Population'].sum()
        area_100=group_100['Area'].sum()

        total_communes = count['ADM3_FR'].tolist()
        total_area = count['Area'].sum()  
        total_population = count['Population'].sum()

        percentage_0_communes = (len(group_0) / len(total_communes)) * 100
        percentage_0_area = (area_0 / total_area) * 100
        percentage_0_population = (pop_0 / total_population) * 100

        percentage_1_3_communes = (len(group_1_3) / len(total_communes)) * 100
        percentage_1_3_area = (area_1_3 / total_area) * 100
        percentage_1_3_population = (pop_1_3 / total_population) * 100

        percentage_4_20_communes = (len(group_4_20) / len(total_communes)) * 100
        percentage_4_20_area = (area_4_20 / total_area) * 100
        percentage_4_20_population = (pop_4_20 / total_population) * 100

        percentage_20_99_communes = (len(group_20_99) / len(total_communes)) * 100
        percentage_20_99_area = (area_20_99 / total_area) * 100
        percentage_20_99_population = (pop_20_99 / total_population) * 100

        percentage_100_communes = (len(group_100) / len(total_communes)) * 100
        percentage_100_area = (area_100 / total_area) * 100
        percentage_100_population = (pop_100 / total_population) * 100

        barWidth = 0.26

        bars1 = [percentage_0_communes, percentage_1_3_communes, percentage_4_20_communes, percentage_20_99_communes, percentage_100_communes]
        bars2 = [percentage_0_area, percentage_1_3_area, percentage_4_20_area, percentage_20_99_area, percentage_100_area]
        bars3 = [percentage_0_population, percentage_1_3_population, percentage_4_20_population, percentage_20_99_population, percentage_100_population]

        r1 = np.arange(len(bars1))
        r2 = [x + barWidth for x in r1]
        r3 = [x + barWidth for x in r2]

        axs[i].bar(r1, bars1, color='C0', width=barWidth, edgecolor='grey', label=f'{admin_level}')
        axs[i].bar(r2, bars2, color='C2', width=barWidth, edgecolor='grey', label='Superficie')
        axs[i].bar(r3, bars3, color='C1', width=barWidth, edgecolor='grey', label='Population')

        #display percentages on bars
        for j in range(len(bars1)):
            axs[i].text(j, bars1[j], f"{bars1[j]:.1f}", ha='center', va='bottom')
            axs[i].text(j+barWidth, bars2[j], f"{bars2[j]:.1f}", ha='center', va='bottom')
            axs[i].text(j+2*barWidth, bars3[j], f"{bars3[j]:.1f}", ha='center', va='bottom')

        axs[i].set_xlabel('Nombre d\'agences bancaires')
        axs[i].set_ylabel('Pourcentage (%)')
        axs[i].set_title(f'Accès aux agences bancaires {country_name}')
        axs[i].set_xticks([r + barWidth for r in range(len(bars1))])
        axs[i].set_xticklabels(categories)
        axs[i].legend()
        i+=1
    plt.show()



