#A local tech startup's server was hit with a burst of heavy automated traffic. 
#They exported a raw network log list for you. They need you to build an isolated, reusable Log Analyzer Function that
#scans every network request, filters out high-risk flags, extracts port numbers, and returns a safety score.

def extractport(logentry):
    try:
        if logentry["status"]=="MALICIOUS":
            return -1
        elif type(logentry["details"])==str:
            a=logentry["details"].split()
            b=a[1]
            return int(b)        
        else:
            return int(logentry["details"])
    except:
        return 0
    
criticalports=[]
network_logs = [
    {"ip": "192.168.1.1", "status": "SUCCESS", "details": "Port 8080"},
    {"ip": "10.0.0.5", "status": "FAILED", "details": "Port 22"},
    {"ip": "unknown_source", "status": "MALICIOUS", "details": "ATTACK_BLOCKED"}, 
    {"ip": "172.16.0.22", "status": "SUCCESS", "details": 443},                   
    {"ip": "192.168.1.99", "status": "CRITICAL", "details": "Port 80"}
]
for item in network_logs:
    portresult=extractport(item)
    if portresult== -1:
        print("THREAT DETECTED, IMMEDIATE ACTION REQUIRED, from IP",item["ip"])
    elif portresult > 0:
        criticalports.append(portresult)
print("Scanned secured ports:",criticalports)