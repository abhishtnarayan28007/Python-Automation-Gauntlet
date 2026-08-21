import requests
import os 
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_TOKEN")
if not api_key:
    print("couldn't access the key, terminating the program right here")
    exit()
new_post = {
    "title": "Mastering API Integrations",
    "body": "Building production-grade Python pipelines step by step!",
    "userId": 1}
header = {"Authorization": f'Bearer {api_key}','Content-Type':'application/json'}
try:
    response = requests.post("https://jsonplaceholder.typicode.com/posts",json=new_post,
                             headers=header,timeout=5)
    if response.status_code == 201:
        print("data added successfully")
        data = response.json()
        print(data)
    else:
        print(f"couldn't add data due to : {response.status_code}")
except requests.exceptions.RequestException as err:
        print(f"error occured due to : {err}")
    