import requests
header = {"User-Agent": "MyAwesomeApp/1.0","x-api-key": "DEMO-API-KEY"}
try:
    response = requests.get("https://api.thecatapi.com/v1/images/search",headers=header,timeout=5)
    response.raise_for_status()
    data = response.json()
    print("Full Response Data:", data)
    if isinstance(data,list) and len(data) > 0:
        cat_url = data[0].get("url")
        print(f"🐱 Here is your Cat Image URL: {cat_url}")
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
except requests.exceptions.RequestException as err:
    print(f"Connection Error: {err}")