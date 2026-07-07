import json

# PHASE 1: Read the existing data into memory
with open("milestone_deal.json", "r") as file:
    deal_data = json.load(file)

# PHASE 2: Modify the dictionary using your Phase 2 skills!
# Let's add a 3rd milestone to the nested list
deal_data["milestones"].append("Code Base Fully Optimized")

# Let's increase the payout because we added a milestone
deal_data["payout_inr"] += 5000 

# PHASE 3: Write the updated dictionary back down to the exact same file
with open("milestone_deal.json", "w") as file:
    json.dump(deal_data, file, indent=4)

print("🔄 Milestone file successfully read, modified, and saved!")