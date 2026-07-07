import json

# 1. Create a rich, nested dictionary profile in Python memory
freelance_deal = {
    "deal_id": "DEAL_2026_99",
    "payout_inr": 25000,
    "milestones": ["Web Scraper Built", "CSV Pipeline Fixed"],
    "client_verified": True
}

# 2. Open a BRAND NEW file called 'milestone_deal.json' in 'w' (Write) mode
with open("milestone_deal.json", "w") as file:
    
    # 3. Dump the dictionary into the file with a clean 4-space indent
    json.dump(freelance_deal, file, indent=4)

print("🚀 File written successfully! Look at your sidebar.")