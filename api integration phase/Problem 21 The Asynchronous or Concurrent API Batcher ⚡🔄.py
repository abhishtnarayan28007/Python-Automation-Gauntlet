import requests
import time
import os 
from dotenv import load_dotenv
import json
load_dotenv()
batch_results = []
api_key = os.getenv("API_TOKEN")
if not api_key:
    print("couldn't access the key, terminating the program right here")
    exit()
post_ids = [1,2,3,4,5]
for id in post_ids:
    header = {"Authorization": f"Bearer {api_key}","Accept": "application/json"}
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}",
                                headers=header,timeout=5)    
    try:
        if response.status_code == 200:
            print(f"data for post_id {id} received successfully")
            id = response.json()["id"]
            title = response.json()["title"]
            batch_results.append({"id":id,"title":title})
        else:
            print(f"Failed to fetch post {id}")
            continue
    except requests.exceptions.RequestException as err:
        print(f"error occured while fetching data for post {id} due to : {err}")
        continue
print(f"number of successfully fetched posts : {len(batch_results)}")
with open("batch_summary.json","w",encoding="utf-8") as file:
    json.dump(batch_results,file,indent=4)