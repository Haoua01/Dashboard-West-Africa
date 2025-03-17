import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

# Load commune data
df = pd.read_csv('data_all_clean_communes_latest_v4.csv')
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
colors = plt.cm.Reds(np.linspace(0.1, 0.8, len(sizes_bran)))


# Créer le diagramme en camembert
plt.pie(sizes_bran, labels=labels, colors=colors,autopct='%1.1f%%', startangle=140)

# Ajouter un titre
plt.title('Répartition des agences bancaires par pays', fontsize=14, fontweight='bold', ha='center', va='top', pad=40)


# Afficher le graphique
plt.axis('equal')  # Assure que le camembert est circulaire
plt.show()
