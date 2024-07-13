import os
import requests
from dotenv import load_dotenv

load_dotenv()

GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')

def is_valid_postal_code(postal_code, country_name):
    try:
        # Construct the request URL
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={postal_code}&components=country:{country_name}&key={GOOGLE_MAPS_API_KEY}"

        # Send the GET request
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            data = response.json()

            # Check if the postal code is found and matches the country
            if 'results' in data and len(data['results']) > 0:
                result = data['results'][0]
                for component in result.get('address_components', []):
                    if 'postal_code' in component.get('types', []):
                        if component['long_name'] == postal_code:
                            return True

            # If postal code not found or doesn't match
            return False

        else:
            print(f"Error: {response.status_code}, {response.text}")
            return False

    except Exception as e:
        print(f"Exception: {e}")
        return False
