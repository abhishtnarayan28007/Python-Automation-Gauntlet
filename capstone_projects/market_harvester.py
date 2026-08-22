import json
import requests
import time
import os 
import sys
from datetime import datetime
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[logging.FileHandler("pipeline.log"),logging.StreamHandler()])
logging.info("Starting Market Harvester Pipeline...")
load_dotenv()
api_key = os.getenv("API_TOKEN")
if not api_key:
    logging.error("couldn't access the key,terminating the program right here....")
    sys.exit(1)
logging.info("API_TOKEN verified successfully. Proceeding to extraction...")
header = {"Authorization":f"Bearer {api_key}","Accept":"application/json"}
all_posts = []
cleaned_posts = []
page = 1
base_delay = 2
max_retries = 3
while True:
    page_success = False
    for attempt in range(1,max_retries + 1):
        try:
            my_params = {"_page":page,"_limit":10}
            response = requests.get("https://jsonplaceholder.typicode.com/posts",timeout=5,headers=header
                                    ,params=my_params)
            if response.status_code == 200:
                logging.info(f"Successfully retrieved response for page no. {page}!")
                data = response.json()
                page_success = True
                break
            else:
                delay = base_delay ** attempt
                logging.warning(f"couldn't load data in attempt {attempt} for page no.{page} due to error : {response.status_code}")
                logging.warning(f"Attempt failed. Retrying in {delay} seconds...")
                time.sleep(delay)
        except requests.exceptions.RequestException as err:
            delay = base_delay ** attempt
            logging.warning(f"error occured in attempt {attempt} while retrieving page no. {page} : {err}")
            logging.warning(f"Attempt failed. Retrying in {delay} seconds...")
            time.sleep(delay)
    else: 
        logging.error("Pipeline failed: Maximum retry limit reached.")
        sys.exit(1)
    all_posts.extend(data)
    logging.info(f"Harvested {len(data)} records from page {page}")
    time.sleep(1)
    if not data:
            logging.info(f"Finished harvesting ! , total pages crawled : {page - 1}")
            break
    page += 1
total_body_length = 0
for raw_posts in all_posts:
    if len(raw_posts.get("body","")) >= 20:
        total_body_length += len(raw_posts["body"])
        cleaned_posts.append({"id":raw_posts["id"],"user_id":raw_posts["userId"],
                              "title":raw_posts["title"],"body_length":len(raw_posts.get("body",""))})
logging.info("successfully created list of cleaned posts")
totaL_raw = len(all_posts)
totaL_cleaned = len(cleaned_posts)
try:
    avg_body_length = total_body_length / totaL_cleaned
    logging.info(f"The average body length for each of the post is : {round(avg_body_length,2)}")
except Exception as e:
    logging.error(f"{e}\n")
    logging.error(f"error due to no post present with body length equal to greater than 20")
try:   
    with open("actionable_market_data.json","w",encoding="utf-8") as file:
        json.dump(cleaned_posts,file,indent=4)
    logging.info("successfully saved the processed data in a json file")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("harvest_summary.txt","w",encoding="utf-8") as file2:
        file2.write("====================================\n")
        file2.write("FINAL REPORT\n")
        file2.write("------------------------------------\n")
        file2.write(f"DATE/TIME : {current_time}\n")
        file2.write(f"Total raw posts harvested : {totaL_raw}\n")
        file2.write(f"Total clean posts retained : {totaL_cleaned}\n")
        file2.write(f"Average Content Length : {avg_body_length}\n")
        file2.write("Pipeline Status : SUCCESS\n")
        file2.write("=========================================\n")
    logging.info("successfully generated the summary text file")
except Exception as e : 
    logging.error(f"error occured while working with final data files, reason : {e}")
logging.info("Market Harvester Pipeline completed successfully!")

