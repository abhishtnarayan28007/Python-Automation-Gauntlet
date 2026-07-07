import json
l = []
with open("products.json","r") as file:
    data=json.load(file)
    for item in data:
        a = item["item_id"]
        b = item["price_usd"]
        c = round(b * 83.5,2)
        amt = round(c+c*0.18,2)
        d = {"item_id":a,"price_usd":b,"price_inr":c,"tax_amount_inr":amt}
        l.append(d)
with open("products.json","w") as file2:
    json.dump(l,file2,indent=4)