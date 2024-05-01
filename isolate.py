import os

# Function to create dictionaries mapping station IDs to names
def create_station_mapping(input_file):
    station_id_to_name = {}
    station_name_to_id = {}
    with open(input_file, 'r') as f:
        for line in f:
            if 'STATION' in line:
                parts = line.split(',')
                station_id = parts[0].strip()
                station_name = parts[2].strip()
                station_id_to_name[station_id] = station_name
                station_name_to_id[station_name] = station_id
    return station_id_to_name, station_name_to_id

# Function to rename audio files based on station IDs
def rename_audio_files(directory, station_id_to_name):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            # Check if the file name contains a station ID
            for station_id, station_name in station_id_to_name.items():
                if station_id in filename:
                    # Construct the new file name
                    new_filename = filename.replace(station_id, station_name.replace("/", "-"))
                    # Rename the file
                    os.rename(filepath, os.path.join(root, new_filename))
                    print(f"Renamed {filename} to {new_filename}")
                    break

# Path to the input file containing station IDs and names
input_file = 'stations.txt'

# Directory containing audio files
audio_directory = 'DART'

# Create dictionaries mapping station IDs to names
station_id_to_name, station_name_to_id = create_station_mapping(input_file)

# Rename audio files based on station IDs
rename_audio_files(audio_directory, station_id_to_name)
