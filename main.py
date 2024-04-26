import requests
import creds
import json

def fetch_openaq_data(api_key, limit=10000):
    base_url = 'https://api.openaq.org/v1'
    endpoint = '/measurements'
    parameters = {
        'limit': limit,    
        'order_by': 'datetime'  
    }
    headers = {'apikey': api_key}

    response = requests.get(base_url + endpoint, params=parameters, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None

def save_to_json(data, filename='openaq_data.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

api_key = creds.api_key

data = fetch_openaq_data(api_key)
if data:
    save_to_json(data)
    print("Air Quality data saved.")
else:
    print("Failed")
