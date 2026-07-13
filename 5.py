import csv
budget_categories = []
total = 0
count = 0
with open("expenses.csv","r") as file:
    data = csv.DictReader(file)
    for item in data:
        a = round(float(item["amount_usd"])*83.5,2)
        if a < 1000.00:
            count+=1
            budget_categories.append(item["category"])
        else:
            total+=a
print(f"Total number of categories under rupees 1000 is/are =  {count} , namely = {budget_categories}")
print(f"total sum is of premium expenses : {total}")
            



        
    

    