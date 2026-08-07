import requests
def full_update_post(post_id, title, body, user_id):
    try:
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        payload = {"title":title,"body":body,"userId":user_id}
        response = requests.put(url,json=payload)
        if response.status_code == 200:
            data = response.json()
            print(f"data updated successfully using PUT with id : {data.get('id')}")
            print(f"the updated data is {data}")
    except requests.exceptions.RequestException as err:
        print(f"error occured due to {err}")
post_id = int(input("enter post id : "))
title = input("enter the title : ")
body = input("enter the body : ")
user_id = int(input("enter the user id : "))
full_update_post(post_id,title,body,user_id)

def partial_update_title(post_id, new_title):
    try:
        new_payload = {"title":new_title} 
        response = requests.patch(f"https://jsonplaceholder.typicode.com/posts/){post_id}",json=new_payload)
        if response.status_code == 200:
            data = response.json()
            print(f"data updated successfully using PATCH , the updated data is : {data}")
    except requests.exceptions.RequestException as err:
        print(f"error occured due to : {err}")
post_id = int(input("enter id : "))
new_title = input("enter title here : ")
partial_update_title(post_id,new_title)