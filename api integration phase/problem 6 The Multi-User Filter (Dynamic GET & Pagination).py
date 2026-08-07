import requests
url = "https://jsonplaceholder.typicode.com/posts"
titles = []

def get_user_posts(user_id, limit=3):
    try:    
        my_params = {"userId":user_id}
        response = requests.get(url,params=my_params)
        response.raise_for_status()
        data = response.json()
        if response.status_code == 200:
            if len(data) > 0:
                for item in data[:limit]:
                    titles.append(item.get("title"))
                print(f"the required result is =",titles)
            else:
                 print("alert! , no content found for existing user")
    except requests.exceptions.HTTPError as err:
        print("error due to = {err}")
    except requests.exceptions.RequestException as err2:
        print("error due to = {err2}")
user_id = int(input("Enter user_id : "))
data2 = get_user_posts(user_id)
    
