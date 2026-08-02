import json
import csv
with open('supplier_costs.json','r',encoding='utf-8') as file:
    data = json.load(file)
shipping_fees = {}
with open('shipping_invoices.csv','r',encoding='utf-8') as file3:
    data3 = csv.DictReader(file3)
    for item in data3:
        shipping_fees[item['order_id']] = float(item['shipping_fee'])
with open('sales_register.json','r',encoding='utf-8') as file2:
    data2 = json.load(file2)
reconciled_orders = []
total_revenue = 0.0
total_profit = 0.0
for order in data2:
    order_id = order["order_id"]
    product_id = order["product_id"]
    quantity = order["quantity"]
    total_charged = float(order["total_charged"])
    unit_cost = data.get(product_id, 0.0)
    shipping_fee = shipping_fees.get(order_id, 0.0)
    wholesale_cost = unit_cost * quantity
    total_expenses = wholesale_cost + shipping_fee
    net_profit = total_charged - total_expenses
    total_revenue += total_charged
    total_profit += net_profit
    reconciled_orders.append({
            "order_id": order_id,
            "product_id": product_id,
            "total_charged": round(total_charged, 2),
            "wholesale_cost": round(wholesale_cost, 2),
            "shipping_fee": round(shipping_fee, 2),
            "net_profit": round(net_profit, 2)
     })    
summary_report = {
    "overall_revenue": round(total_revenue, 2),
    "overall_profit": round(total_profit, 2),
    "orders": reconciled_orders
}

with open("reconciled_report.json", "w") as f:
    json.dump(summary_report, f, indent=4)

