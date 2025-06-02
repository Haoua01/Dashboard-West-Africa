import pandas as pd
import os

main_folder_path = '/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Mai/Survey'

# Create a list to store the results (to avoid repeated concat in the loop)
dfs = []
dfs_00 = []

# Iterate through the country folders in the main folder
for country_folder in os.listdir(main_folder_path):
    results_list = []
    # Construct the full path to the country folder
    country_folder_path = os.path.join(main_folder_path, country_folder)
    print(f"Processing country: {country_folder}")
    
    # Skip hidden files and folders (like .DS_Store)
    if country_folder.startswith('.') or not os.path.isdir(os.path.join(main_folder_path, country_folder)):
        continue

    # Path to the '00.dta' file in the country folder (adjusted file name)
    file_00_path = os.path.join(country_folder_path, f's00_me_{country_folder}.dta')
    file_00 = pd.read_stata(file_00_path, convert_categoricals=False)
    # Append the loaded DataFrame to the list
    dfs_00.append(file_00)
    
    if country_folder == 'gnb2021':
        file_00.rename(columns={'GPS__Latitude_m': 'GPS__Latitude', 'GPS__Longitude_m': 'GPS__Longitude'}, inplace=True)

    # Define the columns of interest
    columns_of_interest = ['grappe', 'GPS__Latitude', 'GPS__Longitude']
    
    # Ensure that the required columns exist in the '00' file
    required_columns = columns_of_interest
    if not all(col in file_00.columns for col in required_columns):
        print(f"Missing required columns in 00 file for {country_folder}. Skipping...")
        continue
    
    # Select only the columns of interest from '00.dta'
    file_00 = file_00[columns_of_interest]

    dict_files = {
        os.path.join(country_folder_path, f's04a_me_{country_folder}.dta') : ['grappe', 's04q18a', 's04q18b', 's04q28a', 's04q28b'], #4.18a.branch d'activ. ; 4.18b.cat.socioprof ; 4.28a.emploi princ exercé sur 12 mois ; 4.28b. secondaire
        os.path.join(country_folder_path, f's04b_me_{country_folder}.dta') : ['grappe', 's04q29b', 's04q42', 's04q43'], #4.29b. code emploi ; 4.30c. code activité ; 4.42. bulletin de salaire? ; 4.43. Salaire ; 
        os.path.join(country_folder_path, f's04c_me_{country_folder}.dta') : ['grappe', 's04q51b', 's04q52c', 's04q58'], #4.51b. code emploi ; 4.52c. code activité ; 4.58. revenu sur 12 mois du travail ; 
        os.path.join(country_folder_path, f's06_me_{country_folder}.dta') : ['grappe', 's06q01__1', 's06q01__2', 's06q01__3', 's06q01__4', 's06q01__5', 's06q02', 's06q05', 's06q07'], #6.01.1 compte bancaire? ; 6.01.2. compte en poste ? ; 6.01.3 compte micro finance? ; 6.01.4 mobile money? ; 6.01.5 carte prepayée? ; 6.02. a epargné ? ; 6.03. a demandé un credit sur 12 mois ? ; 6.05. a contracté un credit sur 12 mois ? ; 6.07 membre d'une tontine ? ; 6.12. credit aupres de qui ? ; 
        os.path.join(country_folder_path, f's10a_me_{country_folder}.dta') : ['grappe', 's10q04', 's10q05', 's10q06', 's10q08'], #10.04. a une entreprise de BTP? ; 10.05. entreprise de commerce ; 10.06. profession liberale (medecin etc) ; 10.04. date de creation ; 10.05. nombre d'employés ; 10.8 possède un etablissmeent de restauration?
        os.path.join(country_folder_path, f's10b_me_{country_folder}.dta') : ['grappe', 's10q17a', 's10q31', 's10q34'],# 's10q62d_1', 's10q62d_2'], 10.17a. branche activité ; 10.31. entreprise enregistrée au registre ? ; 10.34 source de financement à l'appui de la création de l'entreprise ; 10.62d_1. salaire hommes adultes sur 12 mois ; 10.62d_2. salaire femmes adultes sur 12 mois
        os.path.join(country_folder_path, f's12_me_{country_folder}.dta') : ['grappe', 's12q02'], #12.02. possession d'un equipement en bon etat de fonctionnement
        os.path.join(country_folder_path, f's13_1_me_{country_folder}.dta') : ['grappe', 's13q09'], #13.09 transfert quelconque recu par le menage sur 12 derniers mois
        os.path.join(country_folder_path, f's13_2_me_{country_folder}.dta') : ['grappe', 's13q20', 's13q21', 's13q22a', 's13q22b'] #13.20 motif du transfert recu, 13.21 mode du transfert recu ; 13.22a montant recu, 13.22b frequence des transferts recus
    }

    merged_other_files = pd.DataFrame()

    # Iterate through the dictionary of files
    for file_path, columns in dict_files.items():
        # Skip if the file doesn't exist
        if not os.path.exists(file_path):
            print(f"Skipping missing file: {file_path}")
            continue
        
        # Load the dataset
        df = pd.read_stata(file_path, convert_categoricals=False)
        df = df[columns]
        print(f"{columns} loaded")
        
        # Group by 'grappe' and compute the mean of numeric columns before merging
        numeric_cols = df.select_dtypes(include=['number']).columns
        df = df.groupby('grappe')[numeric_cols].mean().reset_index(drop=True)
        print(f"Grouping by 'grappe' completed for {file_path}")
        
        # Merge with the previous datasets
        if merged_other_files.empty:
            merged_other_files = df
        else:
            merged_other_files = pd.merge(merged_other_files, df, on='grappe', how='outer', suffixes=('_left', '_right'))
        print(f"Merging {file_path} completed")


    # Merge the '00' file with all other files based on 'grappe'
    full_merged_df = pd.merge(merged_other_files, file_00, on='grappe', how='left')
    print("Merging with 00 file completed")

    # Convert all columns to numeric (except for the group-by columns)
    numeric_cols = full_merged_df.select_dtypes(include=['number']).columns

    # Group by 'GPS__Latitude' and 'GPS__Longitude' and compute the mean of the numeric columns
    grouped_df = full_merged_df.groupby(['GPS__Latitude', 'GPS__Longitude'])[numeric_cols].mean().reset_index(drop=True)
    print("Grouping by GPS coordinates completed")

    # Save CSV for the country
    country_name = country_folder.split('_')[0]
    output_path = f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Mai/results7/{country_name}.csv'
    grouped_df.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")