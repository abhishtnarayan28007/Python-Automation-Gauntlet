import requests
def create_post(title, body, user_id):
    try:
        url = "https://jsonplaceholder.typicode.com/posts"
        new_post_data = {'title':title,'body':body,'userId':user_id}
        response = requests.post(url,json=new_post_data,timeout=10)
        if response.status_code == 201:
            data = response.json()
            print(f"Post added successfully with id : {data.get('id')}")
        else:
            print(f"couldn't add the new post! , {response.status_code}")
    except requests.exceptions.RequestException as err:
        print(f"error occured due to : {err}")
title = input("enter the title of your post : ")
body = input("enter the body of your post : ")
user_id = int(input("enter your user id : "))
create_post(title,body,user_id)