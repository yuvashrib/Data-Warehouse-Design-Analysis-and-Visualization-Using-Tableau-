import pandas as pd
import os

# Define the directory containing the CSV files
directory = '/content/'

# List of months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# List to store merged DataFrames
merged_dfs = []

# Iterate over each month
for month in months:
    # Define the filename for the current month
    filename = f'{month}2023_Punctuality_Statistics_UK_airports.csv'

    # Check if the file exists in the directory
    if os.path.exists(os.path.join(directory, filename)):
        # Read main.csv and airport.csv into pandas DataFrames
        main_df = pd.read_csv(os.path.join(directory, filename), encoding='latin1')
        airport_df = pd.read_csv(os.path.join(directory, 'Airport_Dimension.csv'), encoding='latin1')
        city_df = pd.read_csv(os.path.join(directory, 'Destination_City_Dimension.csv'), encoding='latin1')
        airline_df = pd.read_csv(os.path.join(directory, 'Airline_Dimension.csv'), encoding='latin1')

        # Merge DataFrames based on airport name
        merged_df = pd.merge(main_df, airport_df, how='left', left_on='reporting_airport', right_on='airport_name')


        # Merge DataFrames based on city name
        merged_df = pd.merge(merged_df, city_df, how='left', left_on='origin_destination', right_on='city_name')

        # Merge DataFrames based on airline name
        merged_df = pd.merge(merged_df, airline_df, how='left', left_on='airline_name', right_on='airline_name')

        # Rename the ID columns for clarity
        merged_df.rename(columns={'airport_id': 'reporting_airport_id',
                                  'city_id': 'city_id',
                                  'airline_id': 'airline_id'}, inplace=True)

        # Optionally, drop the redundant columns
        merged_df.drop(columns=['airport_name', 'origin_destination','origin_destination_country', 'reporting_airport','airline_name','city_name',country_id], inplace=True)

        # Reset index to create a new column with sequential numbers starting from 1
        merged_df.reset_index(drop=True, inplace=True)
        merged_df['flight_id'] = merged_df.index + 1

        # Append the merged DataFrame to the list
        merged_dfs.append(merged_df)
    else:
        print(f"File not found for {month}")

# Concatenate all merged DataFrames into a single DataFrame
final_df = pd.concat(merged_dfs, ignore_index=True)

# Save the concatenated DataFrame to a new CSV file
final_df.to_csv('output.csv', index=False)

print("Output CSV file saved successfully.")
