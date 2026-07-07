#A retail client has sent you a raw list of inventory items. Some are active, some are out of stock, 
#and some are broken entries. Your job is to parse this list, perform logic math,
#and structure it into an Audited Inventory Catalog (a list of dictionaries) so it can be exported cleanly.
raw_inventory = [
    "PROD001:Laptop:1200:5",       # Format ➜ ID:Name:Price:Stock
    "PROD002:Mouse:25:0",          # Out of stock item
    "MALFORMED_DATA_ROW_ERROR",     # Landmine 1
    "PROD003:Keyboard:80:12",      
    "PROD004:Monitor:300:INVALID"  # Landmine 2: Stock isn't an integer!
]
cleancatalog=[]
for a in raw_inventory:
    try:
        b=a.split(":")
        totcost=float(b[2])*int(b[3])
        product_dict = {
                        "id": b[0],
                        "name": (b[1]),
                        "price": float(b[2]),
                        "stock": int(b[3]),
                        "totalvalue":totcost }
        cleancatalog.append(product_dict)
    except Exception as e:
        print(f"invalid entry due to: {e}")
print(f"the final product summary is:{cleancatalog}")
outofstock=[]
highvaluepipeline=[]
for item in cleancatalog:
        if item["stock"]==0:
            outofstock.append(item["name"])
        if item["totalvalue"]> 1000.0:
            highvaluepipeline.append(item)
print(f"out of stock list: {outofstock}\n" f"high value pip list: {highvaluepipeline}")


