import csv
dict=[]
with open("invoice_report.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        shipping_cost=int(row["cost"]) + 500
        row["cost"]=shipping_cost
        dict.append(row)
    with open("final_shipping_report.csv","w",newline="") as file2:
        header1=["invoice_no","item","cost"]
        writer=csv.DictWriter(file2,fieldnames=header1)
        writer.writeheader()
        writer.writerows(dict)