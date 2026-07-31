import json
import csv
flattened_rows = []
with open('shipping_routes.json','r') as file:
    data = json.load(file)
for item in data['containers']:
    for item1 in item['packages']:
        for item2 in item1['checkpoint_logs']:
            metrics = item2['coordinate_metrics']
            flattened_rows.append({'shipment_batch_id':data['shipment_batch_id'],
                                    'logistics_provider':data['logistics_provider'],
                                    'container_id':item['container_id'],'origin_port':item['origin_port'],
                                    'destination_port':item['destination_port'],'package_id':item1['package_id'],
                                    'weight_kg':item1['weight_kg'],'declared_value_usd':item1['declared_value_usd'],
                                    'checkpoint_id':item2['checkpoint_id'],'timestamp':item2['timestamp'],
                                    'latitude': metrics['latitude'],
                'longitude': metrics['longitude'],
                'temp_celsius': metrics['temp_celsius'],
                'humidity_percent': metrics['humidity_percent']})
with open('unrolled_shipping_ledger.csv','w',newline='',encoding='utf-8') as file2:
    header = [
    'shipment_batch_id',
    'logistics_provider',
    'container_id',
    'origin_port',
    'destination_port',
    'package_id',
    'weight_kg',
    'declared_value_usd',
    'checkpoint_id',
    'timestamp',
    'latitude',
    'longitude',
    'temp_celsius',
    'humidity_percent'
]
    writer = csv.DictWriter(file2,fieldnames=header)
    writer.writeheader()
    writer.writerows(flattened_rows)