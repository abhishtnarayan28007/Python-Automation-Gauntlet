import os 
import requests
from dotenv import load_dotenv
live_weather = []
load_dotenv()
key = os.getenv("WEATHER_API_KEY")
if not key:
    print("key not found with the name WEATHER_API_KEY")
try:
    my_params = {"q":"Hardoi","APPID":key,"units":"metric"}
    response = requests.get("https://api.openweathermap.org/data/2.5/weather",params=my_params,timeout=5)
    if response.status_code == 200:
        print("data received successfully")
        data = response.json()
        print(data["name"])
        print(data["sys"]["country"])
        print(data["main"]["temp"])
        print(data["main"]["feels_like"])
        print(data["weather"][0]["description"])
    elif response.status_code == 404:
        print("❌ City not found! Please check the spelling.")
except requests.exceptions.RequestException as err:
    print(f"error occured due to : {err}")