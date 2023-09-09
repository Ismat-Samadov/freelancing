import os
import zipfile
import csv
from xml.etree import ElementTree as ET
from geopy.distance import great_circle

# Function to extract KML from KLZ and save it as a KML file
def extract_kml_from_klz(klz_path, output_dir):
    with zipfile.ZipFile(klz_path, 'r') as zip_ref:
        # Extract the KML file
        kml_files = [f for f in zip_ref.namelist() if f.lower().endswith('.kml')]
        if kml_files:
            kml_file = kml_files[0]  # Assuming there's only one KML file in each KLZ
            kml_content = zip_ref.read(kml_file)

            # Construct the target KML filename
            target_kml_filename = os.path.splitext(os.path.basename(klz_path))[0] + ".kml"
            target_kml_path = os.path.join(output_dir, target_kml_filename)

            # Write the KML content to the target KML file in binary mode
            with open(target_kml_path, 'wb') as target_kml_file:
                target_kml_file.write(kml_content)

            return target_kml_path

# Function to extract coordinates from KML content
def extract_coordinates(kml_content):
    coordinates = []

    try:
        root = ET.fromstring(kml_content)
        placemarks = root.findall(".//Placemark")

        for placemark in placemarks:
            coordinates_elem = placemark.find(".//coordinates")
            if coordinates_elem is not None:
                coordinates_text = coordinates_elem.text.strip()
                coordinates.extend([c.strip() for c in coordinates_text.split()])

    except ET.ParseError as e:
        print(f"Error parsing KML content: {e}")

    return coordinates

# Function to calculate distance between two sets of coordinates
def calculate_distance(coords1, coords2):
    coord1 = coords1.split(',')
    coord2 = coords2.split(',')

    lat1, lon1 = map(float, coord1[:2])
    lat2, lon2 = map(float, coord2[:2])

    coord1 = (lat1, lon1)
    coord2 = (lat2, lon2)

    return great_circle(coord1, coord2).meters

# Main function
if __name__ == "__main__":
    input_directory = "C:/Users/Ismat/freelancing/klz_to_klm/"
    output_directory = "C:/Users/Ismat/freelancing/klz_to_klm/output"
    output_csv_file = "C:/Users/Ismat/freelancing/klz_to_klm/output/output.csv"  # Specify the full path

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    kml_files = []

    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.lower().endswith('.kmz'):
                klz_path = os.path.join(root, file)
                try:
                    target_kml_path = extract_kml_from_klz(klz_path, output_directory)
                    if target_kml_path:
                        with open(target_kml_path, 'r', encoding='utf-8') as kml_file:
                            kml_content = kml_file.read()
                            coordinates = extract_coordinates(kml_content)
                            if coordinates:
                                kml_files.append(coordinates)
                except PermissionError as e:
                    print(f"Permission denied for file: {klz_path}. Skipping.")

    # Calculate distances and write the collected data to a CSV file
    with open(output_csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Distance (meters)'])

        for i in range(len(kml_files)):
            for j in range(i + 1, len(kml_files)):
                distance_meters = calculate_distance(kml_files[i][0], kml_files[j][0])
                csv_writer.writerow([distance_meters])

    print(f"CSV file '{output_csv_file}' has been created.")
