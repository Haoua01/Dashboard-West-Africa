import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Chargement des données
df = pd.read_csv('data_all_clean_communes_latest_v6_geoc.csv')

# Dictionnaire des pays
country_dict1 = {
    "Bénin": ["benin"],
    "Burkina Faso": ["burkina"],
    "Côte d'Ivoire": ["civ"],
    "Guinée-Bissau": ["guinee"],
    "Mali": ["mali"],
    "Niger": ["niger"],
    "Sénégal": ["senegal"],
    "Togo": ["togo"]
}

# Initialisation des listes
branch2, atm2, all_services, zero = [], [], [], []

# Calcul des proportions
for country_name, code in country_dict1.items():
    country = code[0]

    count = df[df['Country'] == country].shape[0]

    count_all = df[(df['Country'] == country) & (df['Total_bran'] != 0) & (df['Total_ATMs'] != 0)].shape[0]
    count_zero = df[(df['Country'] == country) & (df['Total_bran'] == 0) & (df['Total_ATMs'] == 0)].shape[0]
    count_atm2 = df[(df['Country'] == country) & (df['Total_bran'] == 0) & (df['Total_ATMs'] != 0)].shape[0]
    count_branch2 = df[(df['Country'] == country) & (df['Total_bran'] != 0) & (df['Total_ATMs'] == 0)].shape[0]

    zero.append((count_zero/count)*100)
    branch2.append((count_branch2/count)*100)
    atm2.append((count_atm2/count)*100)
    all_services.append((count_all/count)*100)

# Données pour le graphique
countries = list(country_dict1.keys())
x = np.arange(len(countries))
width = 0.8  # Largeur des barres

# Création de la figure et de l'axe
fig, ax = plt.subplots(figsize=(12, 6))

# Empilement des barres avec des couleurs distinctes
colors = ["#d9534f", "#5bc0de", "#f0ad4e", "#5cb85c"]
bars1 = ax.bar(x, zero, width, color=colors[0], label='Aucun service')
bars2 = ax.bar(x, atm2, width, bottom=np.array(zero), color=colors[1], label='DAB sans agences')
bars3 = ax.bar(x, branch2, width, bottom=np.array(zero) + np.array(atm2), color=colors[2], label='Agences sans DAB')
bars4 = ax.bar(x, all_services, width, bottom=np.array(zero) + np.array(atm2) + np.array(branch2), color=colors[3], label='Agences et DAB')

# Ajout des valeurs sur les barres
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + height/2, f"{height:.1f}%", 
                    ha='center', va='center', fontsize=10, color="black")

# Labels et légendes
ax.set_xlabel("Pays", fontsize=12, fontweight="bold")
ax.set_ylabel("Pourcentage de communes", fontsize=12, fontweight="bold")
ax.set_title("Répartition des Établissements Bancaires (EB) dans les communes", fontsize=14, fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(countries, rotation=45, ha="right", fontsize=11)
ax.legend(loc="upper left", fontsize=11)

# Affichage propre
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
