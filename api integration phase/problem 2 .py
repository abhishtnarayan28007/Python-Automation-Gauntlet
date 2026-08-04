import requests
url = "https://bored-api.appbrewery.com/filter"
query_params = {"type":"diy","participants":2}
response = requests.get(url,params=query_params)
print(f"Status Code = {response.status_code}")
print(f"Full URL = {response.url}")
data = response.json()
if response.status_code == 200:
    for items in data:
        print(f"Activity_name = {items.get('activity','__')}")
        print(f"Price = {items.get('price',0)}") 
else:
    print(f"error fetching data due to : {data.get('error','unknown error')}")

