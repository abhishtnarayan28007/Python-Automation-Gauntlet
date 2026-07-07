import csv
l=[]
with open("signups.txt","r") as file:
    data=file.read()
    data1=data.split(",")
    for item in data1:    
        data2=item.strip()
        l.append(data2)    
    new=l[0].upper()
    a=l[1]
    b=l[2]
info={"Name":new,"DOB":a,"Location":b}
with open("clean_signups.csv","w",newline="") as file2:
    header=["Name","DOB","Location"]
    writer=csv.DictWriter(file2,fieldnames=header)
    writer.writeheader()
    writer.writerow(info)
print("success")

