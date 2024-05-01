import os
import shutil

# Function to create folders if they don't exist
def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Dictionary mapping prefixes/suffixes to folder names
folder_mappings = {
    's': 'spanish',
    'Num': 'numbers',
    'min': 'minutes',
    'BT': 'Big Tex Sign On/Off',
    'BJ': 'Dart is back',
    'CA': 'Customer announcements',
    'Info': 'Information',
    'message': 'message',
    'BC': 'BC',
    'CC': 'CC',
    'clean': 'clean',
    'Dfw': 'Dfw',
    'DL': 'DL',
    'DV': 'DV',
    'EB': 'EB',
    'GF': 'GF',
    'Event': 'Event',
    'Stat': 'Stat',
    'TRE': 'TRE',
    'tc': 'tc',
    'tx': 'tx'
}

# Create folders
for folder in folder_mappings.values():
    create_folder(folder.lower())

# Organize files
for filename in os.listdir('.'):
    if not os.path.isfile(filename):
        continue
    
    # Remove file extension and convert to lowercase for comparison
    name_without_extension = os.path.splitext(filename)[0].lower()
    
    # Move file based on suffix or prefix
    for key, folder in folder_mappings.items():
        if name_without_extension.endswith('s') and key == 's':
            shutil.move(filename, folder_mappings['s'].lower())
            break
        elif name_without_extension.startswith(key.lower()):
            shutil.move(filename, folder.lower())
            break
