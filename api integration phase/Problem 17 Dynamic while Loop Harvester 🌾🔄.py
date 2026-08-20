import requests
import time
master_list = []
page = 1
max_pages = 15
while page <= max_pages:
    try:
        my_params = {"_page":page,"_limit":10}
        response = requests.get("https://jsonplaceholder.typicode.com/posts",params=my_params,timeout=5)
        if response.status_code == 200:
            print(f"data received successfully for page : {page}")
            data = response.json()
            if data == []:
                print("empty data !")
                break
            master_list.extend(data)
            time.sleep(1)
        else:
            print(f"couldn't load data due to : {response.status.code}")
    except requests.exceptions.RequestException as err:
        print(f"error due to due : {err}")
    page+=1
with open("paginated_posts2.txt","w") as file:
    for post in master_list:
        file.write(f"ID: {post['id']} / Title: {post['title']}\n")
print("Paginated posts saved successfully!")