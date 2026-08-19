import requests
repo = []
def currency_converter(amount):
    try:
        my_params = {"from":"USD"}
        response = requests.get("https://api.frankfurter.app/latest",params=my_params,timeout=5)
        if response.status_code == 200:
            print("data received successfully")
            data = response.json()
            data2 = {"INR":round(amount*data["rates"]["INR"],2),"GBP":round(amount*data["rates"]["GBP"],2),
                     "AUD":round(amount*data["rates"]["AUD"],2)
                     ,"JPY":round(amount*data["rates"]["JPY"],2),
                     "CAD":round(amount*data["rates"]["CAD"],2),"EUR":round(amount*data["rates"]["EUR"],2)}
            repo.append(data2)
        else:
            print(f"couldn't load data due to : {response.status_code}")
    except requests.exceptions.RequestException as err:
        print(f"error due to : {err}")
amount = float(input("Enter the amount here : $"))
currency_converter(amount)
with open("exchange_report.txt","w",encoding="utf-8") as file:
    file.write("=====DAILY EXCHANGE REPORT====\n")
    file.write(f"Base amount : ${amount}\n")
    file.write("----------------------------\n")
    item = repo[0]
    for key, val in item.items():
        file.write(f"{key} : {val}\n")
    file.write("================================\n")
    file.write("REPORT GENERATED SUCCESSFULLY\n")
