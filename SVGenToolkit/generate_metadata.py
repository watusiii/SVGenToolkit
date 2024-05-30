import json
import os

def generate_json_files(num_files, folder_name):
    # Ensure the folder exists
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    for i in range(1, num_files + 1):
        data = {
            "name": f"SVG Art #{i:02}",
            "creator": "HBarbarian",
            "description": "An awesome NFT!",
            "type": "image/svg",
            "properties": {
                "license": "MIT-0",
                "collection": "My Collection"
            }
        }
        
        file_name = os.path.join(folder_name, f"{i}.json")  # Save to 'metadata' folder
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"File created: {file_name}")

# Number of JSON files to create and folder name
generate_json_files(333, "metadata")
