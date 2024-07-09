import requests
import os 
from dotenv import load_dotenv

load_dotenv()

GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')



def is_valid_address(address, postal_code, country_name):
    try:
        # Construct the request URL
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&components=postal_code:{postal_code}|country:{country_name}&key={GOOGLE_MAPS_API_KEY}"

        # Send the GET request
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            data = response.json()

            # Check if the address components are found and match the provided details
            if 'results' in data and len(data['results']) > 0:
                result = data['results'][0]

                # Check if all components (address, postal code, country) match
                if all(component in result['formatted_address'] for component in [address, postal_code, country_name]):
                    return True

            # If address combination not found or doesn't match
            return False

        else:
            print(f"Error: {response.status_code}, {response.text}")
            return False

    except Exception as e:
        print(f"Exception: {e}")
        return False
