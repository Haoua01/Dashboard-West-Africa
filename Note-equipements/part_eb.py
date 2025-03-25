import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

# Load commune data
df = pd.read_csv('data_all_clean_communes_latest_v6_geoc.csv')
df['Equipments']=df['Total_bran']+df['Total_ATMs']
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

# Données
labels = country_dict1.keys()

sizes_bran = df.groupby('Country')['Total_bran'].sum()
sizes_dab = df.groupby('Country')['Total_ATMs'].sum()

#define a nuance of blues according to sizes
colors_reds = plt.cm.Reds(np.linspace(0.1, 0.8, len(sizes_bran)))
colors_blues = plt.cm.Blues(np.linspace(0.1, 0.8, len(sizes_dab)))


# Créer le diagramme en camembert avec les labels des pays seulement en gras
#plt.pie(sizes_bran, labels=labels, colors=colors_reds,autopct='%1.1f%%', startangle=140, textprops={'weight': 'bold'})
plt.pie(sizes_dab, labels=labels, colors=colors_blues,autopct='%1.1f%%', startangle=140, textprops={'weight': 'bold'}, )
# Ajouter un titre
plt.title('DAB', fontsize=14, fontweight='bold', ha='center', va='top', pad=40)


# Afficher le graphique
plt.axis('equal')  # Assure que le camembert est circulaire
plt.show()
