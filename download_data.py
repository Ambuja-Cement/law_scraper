import json
import os
import requests

def download_and_save_files(data):
    # Create folder if it doesn't exist
    folder_name = "downloaded_files"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    for entry in data:
        # Extract data from JSON
        file_name = entry["name"]
        download_link = entry["download_link"]

        # Download file
        response = requests.get(download_link, verify=False)
        if response.status_code == 200:
            # Save the file in the folder with the name extracted from JSON
            file_path = os.path.join(folder_name, file_name + ".pdf")
            with open(file_path, "wb") as file:
                file.write(response.content)
            print("File downloaded and saved as:", file_path)
        else:
            print(f"Failed to download the file: {file_name}")

# Read JSON data from file
with open("cleaned_law_data.json", "r") as file:
    json_data = json.load(file)

# Download and save files
download_and_save_files(json_data)
