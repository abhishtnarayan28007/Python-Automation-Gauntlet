# Conversion rate: 1 Euro = 90 Rupees
raw_euro_inventory = [
    "PROD_A:Keyboard:45:10",  # Price is 45 Euros
    "PROD_B:Monitor:200:2",   # Price is 200 Euros
    "CORRUPT_ROW",
    "PROD_C:Mouse:15:INVALID"
]
def convertcurrency(europrice):
    a=float(europrice)*90
    return a
cleancatalog=[]
    
for item in raw_euro_inventory:
    try:   
       a=item.split(":")
       b=convertcurrency(float(a[2]))
       totalvaluation=b*int(a[3])
       dict={"Rupee price":totalvaluation}
       cleancatalog.append(dict)
    except Exception as e:
       print(f"skipping gracefully beacause of: {e}")

print(cleancatalog)
