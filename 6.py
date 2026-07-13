from datetime import datetime
import os
a = datetime.now()
current_date = a.strftime('%Y-%m-%d')
file_size = os.path.getsize("activity_log.txt")
with open("activity_log.txt","r") as file:
    data = file.readlines()
    data1 = len(data)
with open("backup_activity_log.txt","w",newline="") as file2:
    file2.write("# BACKUP METADATA #\n")
    file2.write(f"# Execution Date: {current_date}\n")
    file2.write(f"# File Size: {file_size} bytes\n")
    file2.write(f"# Total Lines: {data1}\n")
    file2.write("###################\n\n")
    for item in data:
        file2.write(item)




