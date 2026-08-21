import requests
import os 
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_TOKEN")
if not api_key:
    print("couldn't access the key, terminating the program right here")
    exit()
payload = {"title": "Updated Title via PATCH"}
header = {"Authorization": f'Bearer {api_key}','Content-Type':'application/json'}
payload2 = {"id": 1, "title": "Brand New Title via PUT", "body": "Brand new body content!", "userId": 1}
try:
    response = requests.patch("https://jsonplaceholder.typicode.com/posts/1",headers=header,
                              json=payload,timeout=5)
    if response.status_code == 200:
        print("data 'patched' successfully !")
        print(response.json())
    else:
        print(f"couldn't 'patch' data due to error : {response.status.code}")
    response2 = requests.put("https://jsonplaceholder.typicode.com/posts/1",headers=header,
                              json=payload2,timeout=5)
    if response2.status_code == 200:
        print("data 'put' successfully")
        print(response2.json())
    else:
        print(f"couldn't 'put' data due to error : {response2.status_code}")
except requests.exceptions.RequestException as err:
    print(f"error occured due to : {err}")
