import json

# Charger les distances depuis le fichier JSON
with open("neighbors_great_circle4.json", "r") as f:
    distances = json.load(f)

# Vitesse moyenne en km/h
vitesse = 30

# Fonction pour convertir distances en temps (minutes)
def convert_distances_to_minutes(distances_dict, vitesse):
    times_dict = {}
    for pays, villes in distances_dict.items():
        times_dict[pays] = {}
        for ville1, voisins in villes.items():
            times_dict[pays][ville1] = {}
            for ville2, distance in voisins.items():
                temps_minutes = round((distance / vitesse) * 60, 1)  # minutes
                times_dict[pays][ville1][ville2] = temps_minutes
    return times_dict

# Conversion
times_in_minutes = convert_distances_to_minutes(distances, vitesse)

# Sauvegarde
with open("travel_times_minutes_v2.json", "w") as f:
    json.dump(times_in_minutes, f, indent=2)

print("Conversion terminée : distances → temps de trajet (en minutes).")
