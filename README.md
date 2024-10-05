# Garmin GPX Data Parser

## Overview

This Python script parses Garmin GPX files and extracts relevant data such as **time**, **latitude**, **longitude**, **air temperature**, **heart rate**, and **cadence**. The extracted data is saved in individual CSV files for each GPX file, and also combined into a single CSV file containing data from all processed GPX files.

## Features

- Parses multiple GPX files from a specified folder.
- Extracts key data points from each GPX file, including:
  - **Time**
  - **Latitude**
  - **Longitude**
  - **Air Temperature**
  - **Heart Rate**
  - **Cadence**
- Saves each GPX file's data to a corresponding CSV file.
- Combines all parsed data into a single CSV file (`all_data.csv`).

## Requirements

- **Python** 3.x
- Required Python packages:
  - `beautifulsoup4` (for parsing XML)
  - `pandas` (for data handling)

You can install the required packages using `pip`:

```bash
pip install beautifulsoup4 pandas
```

## Usage

### 1. Clone or Download the Repository

Clone the repository or download the script to your local machine:

```bash
git clone https://github.com/yourusername/garmin-gpx-parser.git
cd garmin-gpx-parser
```

### 2. Set Up Folder Structure

Ensure you have a folder containing your Garmin GPX files (e.g., `C:\GarminData`).

### 3. Run the Script

Run the script by specifying the folder path where your GPX files are stored:

```bash
python parse_garmin_data.py
```

This will process all GPX files in the specified folder and generate CSV files.

### 4. Function Example

You can also use the `parse_garmin_data()` function directly from the script, providing the folder path:

```python
from parse_garmin_data import parse_garmin_data

parse_garmin_data("C:\\GarminData")
```

### 5. Output

- The script will generate individual CSV files for each GPX file found in the folder.
- It will also create a combined file named `all_data.csv` containing all parsed data from the GPX files.

### Example Output Structure

Suppose your GPX files are stored in `C:\GarminData`, after running the script, the folder structure will look like this:

```
C:\GarminData\
    file1.gpx
    file2.gpx
    file1.csv
    file2.csv
    all_data.csv
```

### Sample CSV Format

Each CSV file will use the semicolon (`;`) as the delimiter, and will have the following columns:

| Column   | Description               |
|----------|---------------------------|
| `time`   | Timestamp of the data point|
| `lat`    | Latitude                   |
| `lon`    | Longitude                  |
| `atemp`  | Air temperature            |
| `hr`     | Heart rate                 |
| `cad`    | Cadence                    |

## Notes

- This script assumes that the GPX files contain specific tags related to heart rate (`<hr>`), cadence (`<cad>`), and air temperature (`<atemp>`). If any of these tags are missing, the respective columns will remain empty for those entries.
- Latitude and longitude values are saved using commas (`lat, lon`) instead of dots (`.`) for decimal points due to European formatting.

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/my-new-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/my-new-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Now the `README.md` is fully GitHub-compatible, with proper syntax for headings, code blocks, table formatting, and instructions for contributing. Let me know if you need further tweaks!
