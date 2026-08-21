import requests
import time
import os 
from dotenv import load_dotenv
import json
load_dotenv()
api_key = os.getenv("API_TOKEN")
if not api_key:
    print("couldn't access the key, terminating the program right here")
    exit()
base_delay = 2
max_retries = 3
header = {"Authorization": f"Bearer {api_key}","Accept": "application/json"}
for attempt in range(1, max_retries + 1):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1",headers=header,timeout=5)
        if response.status_code == 200:
            print(f"Successfully retrieved data in attempt {attempt}!")
            data = response.json()
            break
        else:
            delay = base_delay ** attempt
            print(f"couldn't load data in attempt {attempt} due to error : {response.status_code}")
            print(f"Attempt failed. Retrying in {delay} seconds...")
    except requests.exceptions.RequestException as err:
        delay = base_delay ** attempt
        print(f"error occured upon request during attempt {attempt} , {err}")
        print(f"Attempt failed. Retrying in {delay} seconds...")
    time.sleep(delay)
    continue
else:
    print("Pipeline failed: Maximum retry limit reached.")
