import requests
import json
from datetime import datetime

# This is a hypothetical function and endpoint
def upload_data_to_meteociel(data):
    url = 'https://api.meteociel.com/v1/upload'  # Hypothetical URL
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer YOUR_API_KEY'}  # Hypothetical headers
    response = requests.post(url, data=json.dumps(data), headers=headers)
    
    if response.status_code == 200:
        print("Data successfully uploaded to Meteociel.")
    else:
        print(f"Failed to upload data. Status code: {response.status_code}, Response: {response.text}")

# Example data structure, adjust according to actual requirements
data = {
    "station_id": "YOUR_STATION_ID",
    "temperature": 22.5,  # Example temperature
    "humidity": 45,       # Example humidity
    "pressure": 1013,     # Example pressure
    "timestamp": datetime.now().isoformat()
}

upload_data_to_meteociel(data)
