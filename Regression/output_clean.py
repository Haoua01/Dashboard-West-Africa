import pandas as pd
import glob
import os

main_folder_path = '/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Mai/results7'

#glob the files in the main folder
all_files = glob.glob(os.path.join(main_folder_path, '*.csv'))

results_list = []

results_raw = []

def get_mode(series):
    mode = series.mode()
    return mode[0] if not mode.empty else None


# for each file, add a column country name
for file_path in all_files:
    # Extract the country name from the file path
    country_name = os.path.basename(os.path.dirname(file_path))
    
    # Read the CSV file
    df = pd.read_csv(file_path)

    results_raw.append(df)
    
    # Add a new column with the country name and keep only between the 19th and 23rd character of the file name
    #df['country'] = file_path[-22:-19]
    print(country_name)

    # replace missing values of each column with the mean of the column
    for column in df.columns:
        if df[column].dtype in ['float64', 'int64']:
            # Replace NaN values with the mean of the column
            mean_value = df[column].mean()
            df[column].fillna(mean_value, inplace=True)
        else:
            # For non-numeric columns, you can choose to fill with a specific value or leave it as is
            # For example, you can fill with 'Unknown' or leave it as NaN
            df[column].fillna('Unknown', inplace=True)

    results_list.append(df)
    

# Concatenate all the results from the list
if results_list:
    result_df = pd.concat(results_list, ignore_index=True)


    # Output the final result to a CSV file
    output_path = '/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Mai/results7/output_corrected.csv'
    result_df.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")

if results_raw:
    result_raw_df = pd.concat(results_raw, ignore_index=True)

    # Output the raw results to a CSV file
    output_raw_path = '/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/Mai/results7/output_raw.csv'
    result_raw_df.to_csv(output_raw_path, index=False)
    print(f"Raw results saved to {output_raw_path}")