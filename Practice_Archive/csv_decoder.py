import csv
total_earnings=0
with open("freelance_ledger.csv","r") as file:
    reader=csv.DictReader(file)
    print("─── READING LIVE LEDGER ───")
    for row in reader:
        print(f"Client: {row['client']} | Project: {row['project']}")
        total_earnings += int(row["payout"])
print("───────────────────────────")
print(f"💰 Total Revenue Secured: INR {total_earnings:,}")
