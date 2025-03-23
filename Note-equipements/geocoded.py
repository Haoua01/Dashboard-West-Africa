import pandas as pd
import json

# Load data
df = pd.read_csv('data_all_clean_communes_latest_v6_geoc.csv')


country_dict1 = {
    "Bénin": ["benin", 202, 305],
    "Burkina Faso": ["burkina", 362, 595],
    "Côte d'Ivoire": ["civ", 664, 951],
    "Guinée-Bissau": ["guinee", 36, 92],
    "Mali": ["mali", 458, 411],
    "Niger": ["niger", 192, 194],
    "Sénégal": ["senegal", 562, 739],
    "Togo": ["togo", 271, 372]
}

# Create a list to store the results
results1 = []
results11 = []
results2=[]


# Get the unique country codes
country_code = df['Country'].unique()

# Loop over each country and calculate the metrics
for country_name, code in country_dict1.items():
    country = code[0]
    coba_branch = code[1]
    coba_atm = code[2]
    # Count the total number of branches in each country
    count = df[df['Country'] == country]
    branch_count = count["Total_bran"].sum()
    atm_count = count["Total_ATMs"].sum()
    #branch_count to_int
    branch_count = int(branch_count)
    atm_count = int(atm_count)
    precision = round((abs(branch_count-coba_branch)/ coba_branch),2)
    precision2 = round((abs(atm_count-coba_atm)/ coba_atm),2)
    #to int Total_geoc
    geocoded = int(count["Total_geoc"].sum())

    # Compute the percentage of geocoded branches
    percent_geocoded = round((geocoded / branch_count) * 100, 1)
    
    # Append the results to the list
    results1.append([country_name, coba_branch, branch_count, precision])
    results11.append([country_name, coba_atm, atm_count, precision2])
    results2.append([country_name, branch_count, geocoded, percent_geocoded])

# Create a DataFrame from the results list
results_df1 = pd.DataFrame(results1, columns=['Pays', 'Comission Bancaire 2023', 'Total Agences Collectées', 'Ecart relatif'])
results_df11 = pd.DataFrame(results11, columns=['Pays', 'Comission Bancaire 2023', 'Total DAB Collectées', 'Ecart relatif'])
results_df2 = pd.DataFrame(results2, columns=['Pays', 'Total Agences Collectées', 'Agences Geocodées', 'Pourcentage Geocodées'])


print(results_df11)

# Save the results to a CSV file
results_df1.to_csv('precision.csv', index=False)
results_df11.to_csv('precision_atm.csv', index=False)
results_df2.to_csv('geocoded.csv', index=False)






"""geocoded_capital = []
for country_name, code in country_dict1.items():
    pays=code[0]
    region=code[1]
    nb=df[(df['Country'] == pays) & (df['ADM2_FR'] == region)]['Total_geoc'].sum()
    percent=round((nb/df[(df['Country'] == pays) & (df['ADM2_FR'] == region)]['Total_bran'].sum())*100, 1)
    geocoded_capital.append([nb, percent])
geocoded_capital= pd.DataFrame(geocoded_capital, columns=['Agences Geocodées Capitales', 'Geocodées Capitales (%)'])
geocoded_capital.index = country_dict1.keys()
print(geocoded_capital)"""