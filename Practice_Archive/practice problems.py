#1. The Automated IP Whitelister 🌐
#The Scenario: You are setting up a secure network for a local client's office. 
# You have a list of raw server access logs, but some unauthorized IP addresses are trying to slip through.

#Your Task: Create a list containing 5 random string IP addresses 
# (e.g., ["192.168.1.1", "10.0.0.5", "172.16.0.1", "192.168.1.99", "10.0.0.25"]). 
# Loop through the list. If an IP starts with "192.168.", print "ACCESS GRANTED".
#  Otherwise, print "ACCESS DENIED: FLAG UNTRUSTED SOURCE".

#2. The Customer Review Sentiment Clean-up 🧹
#The Scenario: You scraped 4 product reviews for an e-commerce business. 
# The raw text dataset is messy, full of accidental trailing whitespaces, and mixed casing.

#Your Task: Given this raw list:
#reviews = ["  EXCELLENT Product!  \n", " terrible service \n", "  Good value for money   ", "BAD EXPERIENCE\n"]
#Create a script that cleans every string using .strip(), converts them entirely to lowercase,
#  and appends them into a new list called cleaned_reviews. Print the final clean list.


#3. The Enterprise Database Backup Simulator 💾
#The Scenario: You need to automate a daily check to see if a database backup script ran successfully.

#Your Task: Create a text file manually named backup_log.txt and write a single line inside it: SUCCESS.
#  Then, write a Python script that opens that file in read mode ("r"). Use an if statement to check if the text 
# inside the file is exactly "SUCCESS". If it is, print "Database system is healthy!".

#4. The Suspicious Activity Ledger 🪵
#The Scenario: You are building a security tool that flags failed login attempts.
#  You don't want to wipe out old security logs; you want to continuously build a historical timeline ledger.

#Your Task: Write a script that opens a file named security_alerts.txt in Append Mode ("a"). 
# Every time you run the script, it should append a new line: "WARNING: Failed login attempt detected at timestamp
#  22:00!\n". Run it 3 times consecutively and check your file to ensure it has 3 distinct rows.

#5. The Local AI Chatbot Budget Checker 🪙
#The Scenario: You are planning a freelance project where a client wants to run text tokens through an AI API model. 
# You need to calculate the total operational cost.

#Your Task: Create a list containing 4 integers representing token counts used per API call: 
# [1500, 4200, 800, 2300]. Loop through the list to calculate the total sum of tokens. 
# If a single call exceeds 3000 tokens, print a warning: "High-cost threshold crossed!". 
# At the very end of your script, print the total sum.


#6. The Freelance Invoice Calculator 💸
# The Scenario: You are building a automated invoicing tool 
# for your freelance coding business. You need a reusable tool that takes a developer's hourly rate 
# and hours worked, calculates the total, and applies a platform tax.
# 
# Your Task: Write a function named calculate_invoice that
#  accepts two parameters (arguments): hours_worked and hourly_rate.Inside the function,
#  calculate the total price: $\text{total} = \text{hours\_worked} \times \text{hourly\_rate}$.
# Deduct a $10\%$ platform fee from that total.
# Return the final earnings amount.
# Test your function outside the block by calling it with 50 hours and a rate of 30,
#  and print the returned value!
# 
# 7. The System Log Anonymizer 🕵️‍♂️
# The Scenario: You are working with a company's internal server logs. 
# For security reasons, you cannot let raw employee email addresses sit in plain text files.
#  You need a function to clean them.
# 
# Your Task: Write a function named anonymize_email that takes a single string parameter called email.
# Inside the function, use Python string slicing or split methods to extract just the 
# domain part (everything after the @ symbol).
# Make the function return a hidden version 
# string like: "HIDDEN_USER@" + domain.Test it by passing "abhisht@google.com" into the function and printing the result!


#01
iplist=["192.168.1.1", "10.0.0.5", "172.16.0.1", "192.168.1.99", "10.0.0.25"]
for item in iplist:
    #if item.startswith("192.168"):
    if "192.168" in item:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED: FLAG UNTRUSTED SOURCE")

#iplist = ["192.168.1.1", "10.0.0.5", "172.16.0.1", "192.168.1.99", "10.0.0.25"]

#for item in iplist:
    # We grab the first 7 characters manually using string slicing
    #if item[0:7] == "192.168":
        #print("ACCESS GRANTED")
    #else:
        #print("ACCESS DENIED: FLAG UNTRUSTED SOURCE")


#02
reviews=["  EXCELLENT Product!  \n", " terrible service \n", "  Good value for money   ", "BAD EXPERIENCE\n"]
cleanedreviews=[]
for item in reviews:
    a=item.lower()
    cleanedreviews.append(a.strip())
print(cleanedreviews)

#03
with open("backlog.txt","r") as b:
    c=b.readlines()
for item in c:
    if "SUCCESS" in item:
        print("database is healthy!")


#04
with open("security.txt","a") as item:
    item.write("WARNING: Failed login attempt detected at timestamp 22:00!\n")

#05
tokenlist=[1500, 4200, 800, 2300]
for i in tokenlist:
    if i > 3000:
        print("High-cost threshold crossed!")
print("total sum is",sum(tokenlist))

#06
def calculateinvoice(hoursworked,hourlyrate):
    total=hoursworked*hourlyrate
    total1=total-total*0.1
    return total1
inputval=calculateinvoice(50,30)
print(inputval)

#07
def anonymizeemail(email):
    email1=email.split("@")
    email2=email1[1]
    email3="HIDDEN USER@  " "+" + email2
    return email3

b=anonymizeemail("abhisht@gmail.com")
print(b)
#OR
def anonymizeemail(email):
    atposition = email.index("@")
    a="HIDDEN USER " "+" +email[atposition::]
    return a

b=anonymizeemail("abhisht@gmail.com")
print(b)
    
#08
price=[12.50, 45.00, 50.00, 89.99, 24.95]
finalprice=[]
for item in price:
    if item >=50.00:
        item1=item+20
        a=round(item1,2)
        finalprice.append(a)
    elif item < 50.00:
        item2=item+item*(15/100)
        b=round(item2,2)
        finalprice.append(b)
print("final list",finalprice)

#import math

#value = 45.99

# Floor drops the decimal entirely (always rounds DOWN)
#print(math.floor(value))  # Output: 45

# Ceil pushes it up to the next integer (always rounds UP)
#print(math.ceil(45.01))   # Output: 46


#9. The Automated Lead Generator Filter 🕵️‍♂️
#The Scenario: You scraped a text file filled with potential corporate clients.
 #Some lines are empty, some are broken fragments, and some are valid target URLs.

#Your Task: Create a text file manually named scraped_leads.txt. 
#Paste these lines exactly inside it:
#Write a script to read this file line by line. Clean the lines using .strip(). 
#Your script must only capture lines that start with "https://" and write them into a
 #brand-new file called valid_leads.txt.



#10. The Production Error Counter 📊
#The Scenario: A DevOps client hands you a server log file. 
#They don't want to read thousands of lines; they just want to know exactly how many times the 
#word "CRITICAL" or "WARNING" appears.

#Your Task: Given this list of log lines:
#logs = ["INFO: System started", "WARNING: High memory usage", 
       # "INFO: Job completed", "CRITICAL: Database offline", "WARNING: Retry attempt 1"]
#Initialize two counter variables: critical_count = 0 and warning_count = 0. 
#Loop through the logs. Use conditional statements to increment the respective counters. 
#A#t the end, print a clean summary report showing both totals.

#11. The Multi-Currency Payroll Function 💱
#The Scenario: An international outsourcing agency needs a modular function to process payouts for remote builders.

#Your Task: Write a function named convert_and_format_payout that accepts 
#two parameters: usd_amount and exchange_rate.

#Inside the function, calculate the converted total.

#If the converted total is less than 1000, add a flat 50 processing bonus.

#Return a string formatted exactly like this: "Final Payout: X" (where X is the calculated total).

#Test it by passing 500 USD and an exchange rate of 83.5 (simulating INR conversion).

#12. The Database Dynamic Query Builder 🛠️
#The Scenario: You are writing a backend utility function that takes raw filter keywords
#from a web UI and formats them into clean query strings for a search database.

#Your Task: Write a function called build_search_tag that takes a string parameter keyword.

#Clean the keyword of any trailing spaces and force it to completely uppercase.

#Return the string wrapped in database brackets, like this: "[TAG: CLEAN_KEYWORD]".

#Test it with the input "  machine learning   " and print the output.


#09
with open("scrapedleads.txt","r") as new:
    a=new.readlines()
    for item in a:
        b=item.strip()
        if b.startswith("https://"):
            with open("validleads.txt","a") as new1:
                new1.write(b + "\n")

#10
CRITICAL=0
WARNING=0
logs = ["INFO: System started", "WARNING: High memory usage", "INFO: Job completed",
         "CRITICAL: Database offline", "WARNING: Retry attempt 1"]
for item in logs:
    if "CRITICAL" in item:
        CRITICAL+=1
    elif "WARNING" in item:
        WARNING+=1
print("no. of warings and criticals:", WARNING, "," , CRITICAL)


#11
def convertandformatpayout(usdamount,exrate):
    convertedtotal=usdamount*exrate
    if convertedtotal < 1000:
        c1=convertedtotal+50
        return c1
        
    else:
        return convertedtotal
f=convertandformatpayout(500,83.5)
print("final payout:",f)

#12
def buildsearchtag(keyword):
    e=keyword.strip()
    d=e.upper()
    return d
x=buildsearchtag("machine learning     ")
print(f"[TAG:{x}]")

