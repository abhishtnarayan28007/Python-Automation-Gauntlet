import time
import requests

master_list = []

# Loop through pages 1, 2, and 3
for page in range(1, 4):
    my_params = {"_page": page, "_limit": 5}
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts",
            params=my_params,
            timeout=5
        )
        if response.status_code == 200:
            print(f"Page {page} data received successfully")
            data = response.json()
            
            # Extend master_list with the 5 posts from this page
            master_list.extend(data)
            
            # Rate limiting: Sleep between API REQUESTS, not items!
            time.sleep(1)
        else:
            print(f"Failed page {page}: {response.status_code}")
    except requests.exceptions.RequestException as err:
        print(f"Error on page {page}: {err}")
# Write to file
with open("paginated_posts.txt", "w", encoding="utf-8") as file:
    for post in master_list:
        file.write(f"ID: {post['id']} / Title: {post['title']}\n")

print("Paginated posts saved successfully!")
