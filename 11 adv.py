import json
import csv
from datetime import datetime
cleanlist = []
with open("auth_logs.json","r") as file:
    data = json.load(file)
with open("payment_logs.csv","r") as file2:
    data2 = list(csv.DictReader(file2))
for item in data:
    for item2 in data2:        
        if item["correlation_id"] == item2["correlation_id"]:
            if item["auth_status"] == "SUCCESS":
                obj1 = datetime.fromisoformat(item["auth_timestamp"])
                obj2 = datetime.fromisoformat(item2["payment_timestamp"])
                latency_period = abs((obj2 - obj1).total_seconds())
                cleanlist.append({"correlation_id":item["correlation_id"],"user_id":item["user_id"],"pay_amount":item2["payment_amount"],"latency_period":latency_period})
        with open("transactions_logs.csv","w",newline="") as file2:
            header = ["correlation_id","user_id","pay_amount","latency_period"]
            writer = csv.DictWriter(file2,fieldnames=header)
            writer.writeheader()
            writer.writerows(cleanlist)






