import json
with open("server_logs.json") as file:
    data= json.load(file)
    if data["status"] == "CRITICAL":
        print(f"WARNING!, {data["server_name"]}, {data["error_codes"][2]}")
