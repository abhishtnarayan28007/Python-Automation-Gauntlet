import json
import csv
b=[]
num=0
with open("billing_registry.json","r") as file:
    data = json.load(file)

for row in data["dispute_log"]:
    if row["status"] == "completed":  
        num+=1
        bfee = int(row["metrics"]["base_fee"])
        tax_amt = bfee*row["metrics"]["tax_rate"]
        total_payout = float(bfee + tax_amt)
        c = {"client":row["client"],"base_fee":row["metrics"]["base_fee"],"total_payout":total_payout}
        b.append(c)

with open("verified_payouts.csv","w",newline="") as file2:
    header=["client","base_fee","total_payout"]
    writer=csv.DictWriter(file2,fieldnames=header)
    writer.writeheader()
    writer.writerows(b)
num2=0
with open("verified_payouts.csv","r") as file3:
    data2 = csv.DictReader(file3)
    for row2 in data2:
        num2+=float(row2["total_payout"])
print(f"Total completed orders and total amount respectively is : {num} , {num2}")




