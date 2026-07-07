#Ingestion: Create a raw list of dirty string logs representing transaction data
#Sanitization: Loop through the list, strip the hidden spacing, and isolate the Transaction ID and the
#Amount dynamically (Hint: use .index(":") and slicing!).
#Processing: Convert the isolated amount to a float. 
#If the amount is over $500$, apply a flat $5\%$ processing discount. 
#Format the final output cleanly using an f-string so it looks exactly
#like this: [VALID TRANSACTION] ID: TXN1001 | Final Amount: $450.50.
#Persistence: Append these clean, beautifully formatted strings directly into a new file called processed_payments.txt.

raw_transactions = [
    "  TXN1001:450.50  \n", 
    "  TXN1002:1200.00  \n", 
    "  CORRUPT_LINE_NO_DATA\n",  
    "  TXN1003:75.25  \n",
    "  TXN1004:REFUND_ERROR  \n" 
]    
for item in raw_transactions:
    try:    
        a=item.strip()
        b=a.index(":")
        c=a[:b]
        d=float(a[b+1:])
        if d > 500:
            d-=d*(5/100)
        with open("processedpayments.txt","a") as var2:
            var2.write(f"[VALID TRANSACTION] ID: {c}  //  Final amount: {d:.2f}\n")
       
    except Exception as e:
        print(f"❌ Alert: Skipping corrupted row due to: {e}")
