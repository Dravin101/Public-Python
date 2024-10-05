Garmin GPX Data Parser
Overview
This Python script parses Garmin GPX files and extracts relevant data such as time, latitude, longitude, air temperature, heart rate, and cadence. The extracted data is then saved in individual CSV files for each GPX file and also combined into a single CSV file containing data from all processed GPX files.

Features
Parses multiple GPX files from a specified folder.
Extracts key data points from each GPX file, including:
Time
Latitude
Longitude
Air Temperature
Heart Rate
Cadence
Saves each GPX file's data to a corresponding CSV file.
Combines all parsed data into a single CSV file.
Requirements
Python 3.x
Required Python packages:
beautifulsoup4 (for parsing XML)
pandas (for data handling)
You can install the required packages using pip:

bash
Code kopiëren
pip install beautifulsoup4 pandas
Usage
1. Clone or Download the Script
You can clone or download this repository to your local machine.

2. Set Up Folder Structure
Place all your Garmin GPX files in a folder (e.g., C:\GarminData).

3. Run the Script
You can execute the script using the following command:

bash
Code kopiëren
python parse_garmin_data.py
The script will process all GPX files in the specified folder and generate the CSV files in the same folder.

4. Function Example
You can use the parse_garmin_data function in the script by specifying the folder path where the GPX files are stored.

python
Code kopiëren
parse_garmin_data("C:\\GarminData")
5. Output
The script will generate individual CSV files for each GPX file.
It will also create a file named all_data.csv in the specified folder that contains all the parsed data.
Example
Suppose your Garmin GPX files are in the folder C:\GarminData. Running the script will generate output files like this:

makefile
Code kopiëren
C:\GarminData\
    file1.gpx
    file2.gpx
    file1.csv
    file2.csv
    all_data.csv
Sample CSV Format
Each CSV file will use the ; delimiter, and the columns will contain the following:

time: Timestamp of the data point
lat: Latitude
lon: Longitude
atemp: Air temperature
hr: Heart rate
cad: Cadence
Notes
This script assumes the GPX files contain tags related to heart rate, cadence, and air temperature. If any of these are missing, the respective columns will remain empty for those data points.
The latitude and longitude values are saved using commas (,) instead of dots (.) for decimal points due to European formatting.
Contributing
If you have suggestions or improvements, feel free to fork the project and submit pull requests.

License
This project is licensed under the MIT License.
