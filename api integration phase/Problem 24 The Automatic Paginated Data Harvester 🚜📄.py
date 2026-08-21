import requests
import time
import os 
from dotenv import load_dotenv
import json
load_dotenv()
all_posts = []
page = 1
api_key = os.getenv("API_TOKEN")
if not api_key:
    print("couldn't access the key, terminating the program right here")
    exit()
header = {"Authorization": f"Bearer {api_key}","Accept": "application/json"}
while True:
    try:
        my_params = {"_page":page,"_limit":5}
        response = requests.get("https://jsonplaceholder.typicode.com/posts",headers=header
                            ,params=my_params,timeout=5)
        if response.status_code == 200:
            data = response.json()
            all_posts.extend(data)
            print(f"Fetched {len(data)} items from page {page}")
            time.sleep(1)
            if not data:
                print(f"Finished harvesting! Total pages crawled: {page - 1}")
                break
            page += 1
        else:
            print(f"error : {response.status_code}")
    except requests.exceptions.RequestException as err:
        print(f"error occured due to : {err}")
with open("harvested_post.json","w",encoding="utf-8") as file:
    json.dump(all_posts, file, indent=4)
    


    

