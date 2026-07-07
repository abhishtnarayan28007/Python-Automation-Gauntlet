with open("serverstatus.txt", "r") as file_variable:
    # Your code goes here to read from file_variable!
    content=file_variable.readlines()

cleanedstatues=[]
for item in content:
    cleanedstatues.append(item.strip())
for item in cleanedstatues:
    if item=="Offline":
        with open("alerts.txt","a") as alertfile:
            alertfile.write("CRITICAL ALERT, Server is down!\n")
