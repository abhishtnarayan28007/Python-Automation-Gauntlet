import json 
import csv
top_tier_cstmr = []
with open("saas_ledger.json","r") as file:
    data = json.load(file)
for item in data:
    total_valuation = 0
    for sub in item["subscription_history"]:
        if sub["discount_coupon_code"] == "WELCOME10":
            m = (sub["base_rate"]*(1 - 0.1))*sub["months_active"]
            total_valuation+=m
        elif sub["discount_coupon_code"] == "LOYALTY20":
            m1 = (sub["base_rate"]*(1 - 0.2))*sub["months_active"]
            total_valuation+=m1
        elif sub["discount_coupon_code"] == "PRO50":
            m2 = (sub["base_rate"]*(1 - 0.5))*sub["months_active"]
            total_valuation+=m2
        elif sub["discount_coupon_code"] == "NO_COUPON":
            m3 = (sub["base_rate"])*sub["months_active"]
            total_valuation+=m3
    if total_valuation > 2500:
        top_tier_cstmr.append({"user_id":item["user_id"],"email":item["email"],"total_valuation":round(total_valuation,2)})
with open("actionable_marketing_dispatch.csv","w",newline="") as file2:
    header = ["user_id","email","total_valuation"]
    writer = csv.DictWriter(file2,fieldnames=header)
    writer.writeheader()
    writer.writerows(top_tier_cstmr)
print("success")

    
    
        

