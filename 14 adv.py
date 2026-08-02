import json
import csv
transaction_log = []
tot_transaction = 0

with open("defi_tx.csv", "r", encoding="utf-8") as file:
    data = file.readlines()

for item in data:
    item = item.strip() # Remove newline characters (\n)
    
    # 1. Skip the header row cleanly
    if "raw" in item or not item:
        continue
    
    # 2. Split the raw line by underscore "_"
    # Example string: TXNID_98231__VAL_4500_USD__STATUS_SUCCESS
    # b becomes: ['TXNID', '98231', '', 'VAL', '4500', 'USD', '', 'STATUS', 'SUCCESS']
    b = item.split("_")
    
    # Grab values directly based on positions:
    status = b[-1]          # 'SUCCESS' is always the last element
    amount = float(b[4])    # '4500' is at index 4
    trans_id = int(b[1])    # '98231' is at index 1
    
    # 3. Check status and calculate
    if status == "SUCCESS":
        tot_transaction += amount
        d = {
            "trans_id": trans_id,
            "amount": amount,
            "status": status
        }
        transaction_log.append(d)

# 4. Save into JSON (Wrap the log & total in a dictionary)
output_data = {
    "total_transaction_volume": tot_transaction,
    "transactions": transaction_log
}

with open("dashboard_log.json", "w", encoding="utf-8") as file2:
    json.dump(output_data, file2, indent=4)



        

