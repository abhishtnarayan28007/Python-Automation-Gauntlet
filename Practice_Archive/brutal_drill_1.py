import json
import csv
num=0
restock_list=[]
with open("inventory_status.json","r") as file:
    data = json.load(file)
a = data["exchange_rate_usd_to_inr"]
b = data["critical_threshold"]

with open("raw_stock_manifest.csv","r") as file2:
    reader = csv.DictReader(file2)
    for row1 in reader:
        c = int(row1["quantity"])
        INR_price = round(float(row1["price_usd"])*a,2)
        if c < b:
            num+=1
            dict={"item_name":row1["item_name"],"current_stock":c,"cost_per_unit_inr":INR_price}
            restock_list.append(dict)
with open("restock_order.csv","a",newline="") as file3:
    header=["item_name","current_stock","cost_per_unit_inr"]
    writer=csv.DictWriter(file3,fieldnames=header)
    writer.writeheader()
    writer.writerows(restock_list)
data["last_inspected"] = "2026-06-25"
data["items_to_restock"] = num
with open("inventory_status.json","w") as file4:
    json.dump(data,file4,indent=4)
    