import requests
import time
attempts = 0
max_retries = 3
while attempts < max_retries:
    try:
        response = requests.get("https://httpbin.org/status/429",timeout=5)
        if response.status_code == 200:
            print(f"data received successfully for attempt {attempts}")
            data = response.json()
            break
        elif response.status_code == 429:
            wait_time = response.headers.get("Retry-After",2) 
            print(f"Rate limited! Cooling down for {int(wait_time)} seconds...")
            time.sleep(int(wait_time))
        else:
            print(f"couldn't load data due to error : {response.status_code}")
    except requests.exceptions.RequestException as err: 
        print(f"error due to : {err}")
    attempts += 1
if attempts == max_retries:
    print("Failed after maximum retry attempts.")
