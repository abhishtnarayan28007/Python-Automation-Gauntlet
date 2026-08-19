import os 
import requests
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")
if not api_key:
    print("KEY NOT FOUND")
def news_fetcher(topic):
    count = 1
    try:
        my_params = {"q":topic,"apiKey":api_key,"pageSize":3}
        response = requests.get("https://newsapi.org/v2/everything",params=my_params,timeout=5)
        if response.status_code == 200:
            print("data received successfully")
            for item in response.json()["articles"]:
                print("------",count,",","------")
                print(f"Source Name : {item["source"]["name"]}")
                print(f"Title Name : {item["title"]}")
                print(f"URL : {item["url"]}")
                count+=1
                
        else:
            print(f"couldn't load data due to : {response.status_code}")
    except requests.exceptions.RequestException as err:
        print(f"error due to : {err}")
topic = input("Enter the topic you want updates of : ")
news_fetcher(topic)