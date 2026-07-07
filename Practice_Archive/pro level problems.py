#💼 Brief 1: The Corporate HR Attendance Sanitizer
#Client Scenario: A startup's biometric attendance machine outputted a raw, messy array of string logs.
#Several rows are corrupt or have missing metrics.
#You need to parse the dataset, isolate valid profiles, and compute dynamic statistics.

#💼 Brief 2: The E-Commerce Tax & Duty Ledger
#Client Scenario: A global drop-shipping merchant wants to audit an array of
#product transactions processed in US Dollars ($). 
#The regional regulatory warehouse needs the final calculations structured in 
#Indian Rupees (₹) with local GST applied.

#💼 Brief 3: The Automated Web Scraping Lead Classifier
#Client Scenario: A marketing manager extracted business traffic data from a scraping script. 
#The raw fields are completely unstructured, and some records don't even have numerical data.

raw_logs = [
    "EMP101:Aman Sharma:22:0.95",   # ID:Name:Days_Worked:Attendance_Percentage
    "EMP102:Priya Rai:20:0.88",
    "SYSTEM_ERROR_TIMEOUT_REFRESH",  # Landmine 1
    "EMP103:Vikram Malhotra:INVALID_DAYS:0.91", # Landmine 2
    "EMP104:Rohan Verma:15:0.65"
]
sanitized_employees=[]
attendance_probation=[]
for item in raw_logs:
    try:
        a=item.strip()
        b=a.split(":")
        total_effective_days=int(b[2])*float(b[3])
        att_val=float(b[3])
        dict={"id":b[0],"name":b[1],"effective_days":total_effective_days,"attendance_rate":att_val}
        sanitized_employees.append(dict)
    except Exception as e:
        print(f"cannot evaluate, cause:{e}")
# Outside and below Loop 1 (Independent Evaluation Loop)
for employee in sanitized_employees:
    if employee["attendance_rate"] < 0.75:  # Clean, readable, fast!
        attendance_probation.append(employee["name"])
print(f"List 1 : {sanitized_employees}")
print(f"List 2 : {attendance_probation}")

#2
raw_txns = [
    "TXN_9901:GadgetBox:40:3",    # TransactionID:ItemName:USD_Price:Quantity
    "CRITICAL_NETWORK_DROP_404",   # Landmine 1
    "TXN_9902:LeatherWallet:25:0", # Out of stock item
    "TXN_9903:SmartWatch:120:ERROR_QTY", # Landmine 2
    "TXN_9904:WirelessBuds:50:5"
]
master_financial_ledger = []
restock_alerts=[]
def apply_indian_market_metrics(usd_price):
    p1=usd_price*85
    p1+=p1*(0.18)
    return p1
for item in raw_txns:
    p2=item.strip()
    p3=p2.split(":")
    try:
        p4=apply_indian_market_metrics(float(p3[2]))
        total_order_valuation=p4*int(p3[3])
        dict={"txn_id":p3[0],"item":p3[1],"inr_price_with_tax":p4,"quantity":p3[3],
              "order_total":total_order_valuation}
        master_financial_ledger.append(dict)
        if int(p3[3])==0:
            restock_alerts.append(p3[1])
    except Exception as e:
        print(f"skipping gracefully, cause: {e}")
print(f"{master_financial_ledger}")
print(f"{restock_alerts}")


#3
raw_scraped_leads = [
    "LEAD_A:TechCorp Solutions:4500:85",  # LeadID:CompanyName:MonthlyViews:ClickCount
    "LEAD_B:Alpha Logistics:1200:12",
    "PAGE_NOT_FOUND_404_SKIP",            # Landmine 1
    "LEAD_C:Beta FinTech:900:0",          # Zero clicks
    "LEAD_D:Gama Retail:UNAVAILABLE:15"   # Landmine 2
]
validated_leads=[]
hot_leads=[]
for item in raw_scraped_leads:
    a=item.strip()
    b=a.split(":")
    try:
        click_through_rate=int(b[3])/int(b[2])
        dict={"lead_id":b[0],"company":b[1],"ctr":round(click_through_rate,2)}
        validated_leads.append(dict)
        if click_through_rate >= 0.01:
            hot_leads.append(b[0])
    except Exception as e:
        print(f"cause of error:{e}")
print(f"{validated_leads}")
print(f"{hot_leads}")



