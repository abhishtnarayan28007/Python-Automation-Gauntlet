#USD to INR: 83.50
#EUR to INR: 90.20
#GBP to INR: 106.10
import json
import csv
a = []
with open("global_tx.json","r") as file:
    data = json.load(file)
for item in data:
    if item["status"] == "Success":
        if item["pricing_metrics"]["base_currency"] == "USD":
              INR_amount = item["pricing_metrics"]["original_amount"]*83.5
              final_payment = round((INR_amount*item["pricing_metrics"]["local_tax_rate"]) + INR_amount,2)
              a.append({"order_id": item["order_id"], "client_name": item["client_name"], "tax_payout": final_payment})
              item["system_reconciled"] = True

        if item["pricing_metrics"]["base_currency"] == "EUR":
             INR_amount1 = item["pricing_metrics"]["original_amount"]*90.20
             final_payment1 = round((INR_amount1*item["pricing_metrics"]["local_tax_rate"]) + INR_amount1,2)
             a.append({"order_id": item["order_id"], "client_name": item["client_name"], "tax_payout": final_payment1})
             item["system_reconciled"] = True
             
        if item["pricing_metrics"]["base_currency"] == "GBP":
             INR_amount2 = item["pricing_metrics"]["original_amount"]*106.20
             final_payment2 = round((INR_amount1*item["pricing_metrics"]["local_tax_rate"]) + INR_amount2,2)
             a.append({"order_id": item["order_id"], "client_name": item["client_name"], "tax_payout": final_payment2})
             item["system_reconciled"] = True

with open("reconciled_payouts.csv","w",newline="") as file2:
     header = ["order_id","client_name","tax_payout"]
     writer = csv.DictWriter(file2,fieldnames=header)
     writer.writeheader()
     writer.writerows(a)
with open("global_tx.json","w") as file3:
     json.dump(data,file3,indent=4)
     
     
     



             

