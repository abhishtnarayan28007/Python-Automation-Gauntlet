import requests
url = "https://bored-api.appbrewery.com/random"
response = requests.get(url)
print(f"Status Code = {response.status_code}")
data = response.json()  # we didn't import json module !!
print(f"Activity = {data.get("activity","__")}")
print(f"Category = {data.get("type","__")}")
print(f"No. of participants required = {data.get("participants",0)}")
