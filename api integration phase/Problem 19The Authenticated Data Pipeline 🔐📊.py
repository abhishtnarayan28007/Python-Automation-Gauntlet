import requests
import os 
from dotenv import load_dotenv
load_dotenv()
master_list = []
API_TOKEN = os.getenv("API_TOKEN")
if not API_TOKEN:
    print("couldn't access the key")
    exit()
try:
    headers = {"Authorization": f"Bearer {API_TOKEN}","Accept": "application/json"}
    my_params = {"_limit":5}
    response = requests.get("https://jsonplaceholder.typicode.com/posts",params=my_params,
                            headers=headers,timeout=5)
    if response.status_code == 200:
        print("data received successfully")
        data = response.json()
        for item in data:
            if item["id"] % 2 == 0:
                master_list.append(item)
    else:
        print(f"couldn't load data due to error : {response.status_code}")
except requests.exceptions.RequestException as err:
    print(f"error due to : {err}")
with open("filtered_posts.txt", "w") as file:
    for post in master_list:
        file.write(f"ID: {post['id']} | Title: {post['title']}\n")
print(f"number of posts : {len(master_list)}")    
for post in master_list:
    print("Title : ",post["title"])


