import json
with open("app_config.json","r") as file:
    data = json.load(file)
flat_strings = []
for main_item , main_val in data.items():
    if type(main_val) == dict:
        for inner_item , inner_val in main_val.items():
            print(f"")


