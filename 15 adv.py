import json
import csv
user_data = []
with open("user_sessions.json","r",encoding="utf-8") as file:
    data = json.load(file)
for item in data:
    try:
        tot_duration = 0
        b = 0
        if "subscription_tier" not in item:
            item["subscription_tier"] = "Basic"
        if "support_tickets" not in item:
            item["support_tickets"] = 0
        if "weekly_durations" not in item:
            item["weekly_durations"] = [0.0]
        for durations in item["weekly_durations"]:
                b += 1
                tot_duration += durations
        a = tot_duration/b     
        user_data.append({"user_id":item["user_id"],"subscription_tier":item["subscription_tier"],
                            "avg_weekly_duration":round(a,2)})
    except Exception as e:           
            print(f"skipping the average math for user :{item["user_id"]} because : {e}")    
with open("churn_features.csv","w",newline="",encoding="utf-8") as file2:
     header = ["user_id","subscription_tier","avg_weekly_duration"]
     writer = csv.DictWriter(file2,fieldnames=header)
     writer.writeheader()
     writer.writerows(user_data)    