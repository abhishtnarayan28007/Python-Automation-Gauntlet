import csv
l = []
with open("sensor_logs.csv","r") as file:
    data = csv.DictReader(file)
    for row in data:
        try:
            val = float(row["reading"])
            a = row["timestamp"]
            b = row["sensor_id"]
            lst = {"timestamp" : a, "sensor_id" : b, "reading" : val}
            l.append(lst)
        except Exception as e:
            print(f"skipping  {row['sensor_id']} , cause: {e}")

with open("filtered_sensors.csv","w",newline="") as file2:
    header=["timestamp","sensor_id","reading"]
    writer=csv.DictWriter(file2,fieldnames=header)
    writer.writeheader()
    writer.writerows(l)