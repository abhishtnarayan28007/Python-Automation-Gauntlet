import csv

# 1. Our clean, flat data payload (a list of identical dictionaries)
freelance_leads = [
    {"client": "Moti Mahal Delux", "project": "Menu Automation", "payout": 15000},
    {"client": "TechCorp India", "project": "Web Scraper", "payout": 22000},
    {"client": "Alpha Logistics", "project": "Data Cleaning", "payout": 18000}
]

# 2. Open the file gate in "w" (Write) mode.
# newline="" is a critical Windows trick that prevents blank empty rows!
with open("freelance_ledger.csv", "w", newline="") as file:
    
    # 3. Define the exact column titles for our spreadsheet
    headers = ["client", "project", "payout"]
    
    # 4. Initialize the specialized CSV writer machine mapped to our headers
    writer = csv.DictWriter(file, fieldnames=headers)
    
    # 5. Stamp the very first row (The Column Headers)
    writer.writeheader()
    
    # 6. Dump all our dictionaries as flat rows in one shot!
    writer.writerows(freelance_leads)

print("🚀 Spreadsheet generated successfully! Check your sidebar.")