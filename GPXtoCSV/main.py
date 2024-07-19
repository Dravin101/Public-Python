import os
from bs4 import BeautifulSoup
import pandas as pd

def parse_garmin_data(root_folder):
    """
    Parses Garmin GPX data files in the specified folder and converts them to CSV format.
    
    This function reads all GPX files in the specified root folder, extracts relevant data
    (time, latitude, longitude, air temperature, heart rate, cadence), and saves the data
    to individual CSV files for each GPX file and a combined CSV file for all data.
    
    Parameters:
    root_folder (str): The path to the folder containing GPX files.

    Example:
    >>> parse_garmin_data("C:\\GarminData")
    This will parse all GPX files in the folder and save the data to CSV files in the same folder.
    """

    # List all files in the root folder
    files = os.listdir(root_folder)
    
    # Initialize a list to hold data from all files
    table_all = []
    
    # Iterate over each file in the folder
    for f in files:
        # Open and read the contents of the file
        with open(os.path.join(root_folder, f), "r") as file:
            contents = file.read()
        
        # Parse the file content as XML
        soup = BeautifulSoup(contents, 'xml')
        datax = soup.find_all()
        
        # Initialize a list to hold data for the current file
        table = []
        
        # Initialize a dictionary to hold current data points
        dict1 = {'time': '', 'lat': '', 'lon': '', 'atemp': '', 'hr': '', 'cad': ''}
        
        # Iterate over each XML element
        for data in datax:
            children = len(list(data.children))
            if children == 1:
                print(f"{data.name} : {data.get_text()}")
                dict1[data.name] = data.get_text()
                if data.name == 'cad':
                    print("set complete")
                    table.append(dict1.copy())
                    table_all.append(dict1.copy())
                    dict1 = {'time': '', 'lat': '', 'lon': '', 'atemp': '', 'hr': '', 'cad': ''}
            elif data.name == 'trkpt':
                d2 = data.attrs
                dict1['lat'] = d2['lat'].replace('.', ',')
                dict1['lon'] = d2['lon'].replace('.', ',')
        
        print('file done')
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(table)
        print(df.head())
        
        # Save the DataFrame to a CSV file
        df.to_csv(os.path.join(root_folder, os.path.basename(f).replace('gpx', 'csv')), sep=';')
    
    # Convert the list of all data to a DataFrame
    df_total = pd.DataFrame(table_all)
    print(df_total.head())
    
    # Save the combined DataFrame to a CSV file
    df_total.to_csv(os.path.join(root_folder, 'all_data.csv'), sep=';')

# Example usage
if __name__ == "__main__":
    parse_garmin_data("C:\\GarminData")
