import json
flattened_data = []
with open("app_config.json","r") as file:
    data = json.load(file)
for main_item , main_val in data.items():
    if type(main_val) == dict:
        for inner_item , inner_val in main_val.items():
             a= main_item +'.'+ inner_item +'='+ str(inner_val)
             flattened_data.append(a)
    else:
        b = main_item +'='+ str(main_val)
        flattened_data.append(b)
with open("config.properties","a",newline="") as file2:
    for item in flattened_data:
        file2.write(item + "\n")
print("success")



            


