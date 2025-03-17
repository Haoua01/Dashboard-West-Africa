import pandas as pd
import json

# Load data
df = pd.read_csv('data_all_clean_communes_latest_v2.csv')
#distance_matrix = neighbors.json
distance_matrix = json.load(open('neighbors.json'))




# Create a list to store the results
results = []

# Get the unique country codes
country_code = df['Country'].unique()

# Loop over each country and calculate the metrics
for country in country_code:
    # Count the total number of branches in each country
    count = df[df['Country'] == country]
    branch_count = count["Total_bran"].sum()
    #to int Total_geoc
    #geocoded = count["Total_geoc"].sum()


    
    # Count the number of communes without a single branch
    count_zero = df[(df['Country'] == country) & (df['Total_bran'] == 0)].shape[0]
    count_not_zero = df[(df['Country'] == country) & (df['Total_bran'] != 0)].shape[0]
    
    
    # Create inclusion index (number of communes with a branch / total branches)
    inclusion_index = (count_not_zero) / count.shape[0]
    
    # Append the results to the list
    results.append([country, count.shape[0], branch_count, count_not_zero, count_zero, inclusion_index])

# Create a DataFrame from the results list
results_df = pd.DataFrame(results, columns=['Country', 'Total Communes', 'Total Branches', 'Communes With', 'Communes Without', 'Inclusion Index'])

print(results_df)

# Save the results to a CSV file
results_df.to_csv('results.csv', index=False)










