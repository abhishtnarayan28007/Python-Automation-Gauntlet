import json

with open("test_profile.json", "r") as file:
    data = json.load(file)

# 1. Accessing a value inside the nested list
print(data["tech_stack"][0])       # Prints: Python

# 2. Accessing a value inside the nested dictionary!
print(data["project_leads"]["technical"])  # Prints: Abhisht