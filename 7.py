import csv
new = []
with open("leads.txt","r") as file:
    data = file.readlines()
    for e in data:
        item = e.strip()
        if item.endswith("edu") or item.endswith("org"):
            new.append(item)
with open("enterprise_leads.csv","w",newline="") as file2:
    for item1 in new:
        file2.write(f"{item1}\n")
print('success') 

