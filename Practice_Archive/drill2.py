import csv
orders = [
    {"invoice_no": "INV001", "item": "Mechanical Keyboard", "cost": 4500},
    {"invoice_no": "INV002", "item": "Ergonomic Mouse", "cost": 2200}
]
with open("invoice_report.csv","w",newline="") as file:
    header=["invoice_no","item","cost"]
    writer=csv.DictWriter(file,fieldnames=header)
    writer.writeheader()
    writer.writerows(orders)
