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

# Calcul des moyennes UEMOA
mean_zero = np.mean(zero)
mean_atm2 = np.mean(atm2)
mean_branch2 = np.mean(branch2)
mean_all_services = np.mean(all_services)

# Ajout de la moyenne aux listes
zero.append(mean_zero)
atm2.append(mean_atm2)
branch2.append(mean_branch2)
all_services.append(mean_all_services)

# Données pour le graphique
countries = list(country_dict1.keys()) + ["Moyenne UEMOA"]
x = np.arange(len(countries))
width = 0.8  # Largeur des barres

# Création de la figure et de l'axe
fig, ax = plt.subplots(figsize=(12, 6))

# Couleurs
colors = ["#d9534f", "#5bc0de", "grey", "#8e44ad"]
darker_colors = ["#a12e28", "#2989a0", "grey", "#5e3370"]




# Empilement des barres
# Empilement des barres avec transparence sur la dernière (Moyenne UEMOA)
bars1 = ax.bar(x[:-1], zero[:-1], width, color=colors[2], label='Aucun service')
bar1_moy = ax.bar(x[-1], zero[-1], width, color=darker_colors[2])

bars2 = ax.bar(x[:-1], atm2[:-1], width, bottom=np.array(zero[:-1]), color=colors[1], label='DAB sans agences')
bar2_moy = ax.bar(x[-1], atm2[-1], width, bottom=zero[-1], color=darker_colors[1])

bars3 = ax.bar(x[:-1], branch2[:-1], width, bottom=np.array(zero[:-1]) + np.array(atm2[:-1]), color=colors[0], label='Agences sans DAB')
bar3_moy = ax.bar(x[-1], branch2[-1], width, bottom=zero[-1] + atm2[-1], color=darker_colors[0])

bars4 = ax.bar(x[:-1], all_services[:-1], width, bottom=np.array(zero[:-1]) + np.array(atm2[:-1]) + np.array(branch2[:-1]), color=colors[3], label='Agences et DAB')
bar4_moy = ax.bar(
    x[-1], all_services[-1], width,
    bottom=zero[-1] + atm2[-1] + branch2[-1],
    color=darker_colors[3]
)

# Ajout de la valeur sur la barre Moyenne UEMOA
for bars in [bar1_moy, bar2_moy, bar3_moy, bar4_moy]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + height/2, f"{height:.1f}%", 
                    ha='center', va='center', fontsize=9, color="black", fontweight='bold')
            
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_y() + height/2, f"{height:.1f}%", 
                    ha='center', va='center', fontsize=9, color="black")

# Labels et légendes
ax.set_xlabel("Pays", fontsize=12)
ax.set_ylabel("Pourcentage de communes", fontsize=12)
ax.set_xticklabels(countries, fontsize=11)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=11)

ax.set_xticks(x)
for label in ax.get_xticklabels():
    if label.get_text() == "Moyenne UEMOA":
        label.set_fontweight('bold')


# Affichage propre
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()
