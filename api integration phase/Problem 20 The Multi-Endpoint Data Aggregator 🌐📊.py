import requests
import os 
from dotenv import load_dotenv
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
if not API_TOKEN:
    print("couldn't access the key")
    exit()
try:
    header = {"Authorization": f"Bearer {API_TOKEN}","Accept": "application/json"}
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1",headers=header,timeout=5)
    if response.status_code == 200:
        data = response.json()
        title = data["title"]
        post_id = data["id"]
        response2 = requests.get(f"https://jsonplaceholder.typicode.com/users/{data["userId"]}",
                                 headers=header,timeout=5)
        if response2.status_code == 200:
            user_details = response2.json()
            name = user_details["name"]
            email = user_details["email"]
            with open("post_summary.txt","w") as file:
                file.write(f"PostId : {post_id} , Title : {title}\n")
                file.write(f"Name : {name} , Email : {email}")
        else:
            print(f"couldn't access the user related server due to error : {response2.status.code}")
    else:
        print(f"couldn't access the post related server due to error : {response.status_code}")
except requests.exceptions.RequestException as err:
    print(f"error due to {err}")
