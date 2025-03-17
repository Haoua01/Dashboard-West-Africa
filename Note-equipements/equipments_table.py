import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

# Load commune data
df = pd.read_csv('data_all_clean_communes_latest_v4.csv')

countries = df['Country'].unique()
#count the number of branches and ATMs for each country
total_bran = df.groupby('Country')['Total_bran'].sum()
total_atm = df.groupby('Country')['Total_ATMs'].sum()

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

#create a table with the number of branches and ATMs for each country
equipments_table = pd.DataFrame({'Total branches': total_bran, 'Total ATMs': total_atm})
#add Equipments column
equipments_table['Equipments'] = equipments_table['Total branches'] + equipments_table['Total ATMs']
#use the country_dict1 keys as index
equipments_table.index = country_dict1.keys()
#convert data to integer
equipments_table = equipments_table.astype(int)

#rename columns
equipments_table.columns = ['Agences bancaires', 'DAB', 'Total EB']


print(equipments_table)

#save the table to a csv file
equipments_table.to_csv('equipments_table.csv')
#plot the table
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')

#plot the table
ax.table(cellText=equipments_table.values, colLabels=equipments_table.columns, rowLabels=equipments_table.index, loc='center', cellLoc='center', colColours=['#f5f5f5', '#f5f5f5', '#f5f5f5'])
plt.show()
