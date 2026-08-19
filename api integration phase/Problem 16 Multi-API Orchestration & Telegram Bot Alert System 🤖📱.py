import os
import requests
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("MY_TELEGRAM_BOT")
id = os.getenv("chat_id")
if not api_key:
  print("key not found")
if not id:
  print("id not found")
try:
   my_params = {"from":"USD"}
   response = requests.get("https://api.frankfurter.app/latest",params=my_params,timeout=5)
   if response.status_code == 200:
      print("data received successfully from frankfurter")
      data = response.json()["rates"]["INR"]
      payload = {"chat_id": id,"text": f"🚨 ALERT: High exchange rate detected! USD to INR is now {data}"}
      response2 = requests.post(f"https://api.telegram.org/bot{api_key}/sendMessage",json=payload,timeout=5)
      if response2.status_code == 200:
        print("message sent successfully , kindly check your telegram app")
      else:
        print(f"telegram request not responding due to : {response2.status_code}")    
   else:
    print(f"frankfurter server not working due to : {response.status.code}")
except requests.exceptions.RequestException as err:
    print(f"error due to : {err}")
   

