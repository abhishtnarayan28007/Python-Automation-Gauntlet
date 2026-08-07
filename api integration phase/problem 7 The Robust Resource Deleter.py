import requests
def delete_post(post_id):
    try:
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        response = requests.delete(url,timeout=5)
        a = response.status_code
        if a == 200 or a == 204:
            print(f"✅ Post {post_id} deleted successfully!")
        elif response.status_code == 404:
            print(f"⚠️ Error: Post {post_id} not found on server.")
        else:
            print(f"❌ Failed with status code: {a}")
    except requests.exceptions.RequestException as err:
        print(f"error generated due to : {err}")
post_id = int(input("Enter post id :"))
delete_post(post_id)
