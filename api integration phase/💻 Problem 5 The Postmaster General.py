import requests
url = "https://jsonplaceholder.typicode.com/posts"
headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": "MyAwesomeApp/1.0"
}
my_post_data = {
    "title": "API Integration Level Up 🚀",
    "body": "Sending my very first POST request data packet!",
    "userId": 5
}
try:
    # 🎯 Task: Make the POST request using requests.post()
    # 💡 Hint: Pass url, json=my_post_data, headers=headers, and timeout=5
    response = requests.post(url,headers=headers,json=my_post_data,timeout=5)
    response.raise_for_status()
    created_data = response.json()
    print("Server Response:", created_data)   
    new_id = created_data.get("id")
    print(f"🎉 Post created successfully with ID: {new_id}")
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
except requests.exceptions.RequestException as err:
    print(f"Connection Error: {err}")