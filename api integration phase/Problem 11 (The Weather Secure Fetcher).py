import os
import requests
from dotenv import load_dotenv
 
load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

if not api_key:
    print("❌ Error: WEATHER_API_KEY not found in .env file!")

my_params = {
    "city": "Ghaziabad",
    "appid": api_key
}
try:
    response = requests.get("https://postman-echo.com/get", params=my_params, timeout=5)
    if response.status_code == 200:
        print(response.json()["args"])
    else: 
        print(f"error due to : {response.status_code}")
except requests.exceptions.RequestException as err:
    print(f"error occured due to : {err}")