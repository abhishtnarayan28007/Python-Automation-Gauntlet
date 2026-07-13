import json
count = 0
count1 = 0
with open("server_status.json","r") as file:
    data = json.load(file)
    for item in data:
        if item["is_up"] == True:
            count+=1
        count1+=1
eval = (count/count1)*100
with open("summary.txt","w",newline="") as file2:
    file2.write(f"SUMMARY\n###########\nTotal upbeats detected : {count}\nTotal Evaluated Beats : {count1}\nUpbeat Percentage : {eval}\n###########")