import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

# Load commune data
df = pd.read_csv('data_all_clean_communes_latest_v6_geoc.csv')
df['Equipments']=df['Total_bran']+df['Total_ATMs']

# Load the neighbors.json data
with open('neighbors_great_circle2.json', 'r') as f:
    neighbors_data = json.load(f)

# Get the unique country codes
country_code = df['Country'].unique()

# Create subplots for each country

# Flatten the axes array to make it easier to iterate
fig = plt.figure(figsize=(12, 8))

country_dict1 = {
    "Bénin": ["benin", "Communes"],
    "Burkina Faso": ["burkina", "Communes"],
    "Côte d'Ivoire": ["civ", "Sous-préfectures"],
    "Guinée-Bissau": ["guinee", "Secteurs"],
    "Mali": ["mali", "Communes"],
    "Niger": ["niger", "Communes"],
    "Sénégal": ["senegal", "Arrondissements"],
    "Togo": ["togo", "Communes"]
}




geographic_access=[]
demographic_access=[]
print("pop", df['Population'].mean())
print("area",df['Area'].mean())
for country_name, code in country_dict1.items():
    country = code[0]
    admin_level = code[1]
    print(f"superficie totale {country_name}:", df[df['Country'] == country]['Area'].sum())
    #print(f"Nombre d'équipements bancaires {country_name}:", df[df['Country'] == country]['Equipments'].sum())
    country_data = df[df['Country'] == country]
    demographic_access.append((country_data['Equipments'].sum() / country_data['Population'].sum()) * 100000)
    if country_name == "Guinée-Bissau":
        geographic_access.append((country_data['Equipments'].sum() / (country_data['Area'].sum())) * 10000)
    else:
        geographic_access.append((country_data['Equipments'].sum() / (country_data['Area'].sum()/100)) * 10000)


#add mean values
demographic_access.append(sum(demographic_access)/len(demographic_access))
geographic_access.append(sum(geographic_access)/len(geographic_access))

#update country_dict1
country_dict1["Moyenne \ UEMOA"] = ["demo", "geo"]
colors_green = ['C2' for _ in range(len(demographic_access)-1)] + ['C3']
colors_orange = ['C1' for _ in range(len(demographic_access)-1)] + ['C3']



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

