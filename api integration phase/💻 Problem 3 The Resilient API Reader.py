import requests
query_params = {"type": "diy", "participants": 2}
try:
    response = requests.get("https://bored-api.appbrewery.com/filter",params=query_params)
    response.raise_for_status()
    data = response.json()
    print("Success! Data received:", data)
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error occurred: {err}")
except requests.exceptions.RequestException as err2:
    print(f"Network/Connection Error occurred: {err2}")    
