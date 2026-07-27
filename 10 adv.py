#isinstance(variable, data_type)
import json

a = []

with open("inventory_manifest.json", "r") as file:
    data = json.load(file)

for item in data:
    # 1. If it's a nested list, unpack it into individual items first!
    if type(item) == list:
        for sub_item in item:
            # Safely process each unnested dictionary
            if "sku_id" not in sub_item:
                sub_item["sku_id"] = "SKU-UNKNOWN"
            if "quantity_in_stock" not in sub_item:
                sub_item["quantity_in_stock"] = 0
            sub_item["quantity_in_stock"] = int(sub_item["quantity_in_stock"])
            sub_item["unit_price"] = float(sub_item["unit_price"])
            a.append(sub_item)

    # 2. If it's a standard dictionary, clean and append it!
    elif type(item) == dict:
        if "sku_id" not in item:
            item["sku_id"] = "SKU-UNKNOWN"
        if "quantity_in_stock" not in item:
            item["quantity_in_stock"] = 0
        item["quantity_in_stock"] = int(item["quantity_in_stock"])
        item["unit_price"] = float(item["unit_price"])
        a.append(item)
 # 3. If it's a string or anything else (corrupted line), it simply gets ignored!
with open("healed_inventory.json","w") as file2:
    json.dump(a,file2,indent=4)