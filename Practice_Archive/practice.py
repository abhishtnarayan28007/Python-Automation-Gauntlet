
purchases = [120, "250 USD", 400, "1500 INR", 80, "300"]
cleaned_purchases = [] # A fresh, empty list to hold our clean numbers

for item in purchases:
    # Step 1: Check if the item is text (string)
    if type(item) == str:
        # Split the string by spaces. "250 USD" becomes a list: ["250", "USD"]
        parts = item.split() 
        numeric_part = parts[0] # Grab the first part: "250"
        
        # Convert the string "250" into a real mathematical integer and save it
        cleaned_purchases.append(int(numeric_part))
    else:
        # If it's already a number, just save it directly
        cleaned_purchases.append(item)

# Step 2: Use your brilliant sum trick on the clean list!
total_revenue = sum(cleaned_purchases)
print("Total Revenue Saved:", total_revenue)


#The Client Scenario: A local gym owner in Hardoi has a messy digital registration log.
#  When users signed up, some typed just their age, but some typed words like "21 years" or "35 years old".
member_ages = [22, "28 years", 31, "19 years old", 45]
cleanedages = []
for item in member_ages:
    if type(item)==str:
        parts=item.split()
        numericpart=parts[0]
        cleanedages.append(int(numericpart))

    else:
        cleanedages.append(item)

print('The sum of ages:',sum(cleanedages))





#Day 2 of python programming
#The Freelance Scenario: A digital marketing agency's webhook has sent a messy batch of lead data to your
#  Python backend script. The client wants to calculate the total budget available from their verified leads.
#  However, some leads typed their budget numbers as strings with text because humans are messy.
leads_data = [
    {"name": "Amit", "verified": True, "budget": 5000},
    {"name": "Spam_Bot", "verified": False, "budget": 100},
    {"name": "Rahul", "verified": True, "budget": "2500 INR"},
    {"name": "Tech_Corp", "verified": True, "budget": "12000 USD"}
]
validbudget=[]
for item in leads_data:
    if item["verified"]==True:
        a=item["budget"]
        if type(a)==str:
            b=a.split()
            c=b[0]
            validbudget.append(int(c))
        else:
            validbudget.append(item["budget"])
print('The total budget is = ',sum(validbudget))




#Day 3 
#The Freelance Scenario: Your client's webhook sent over a list of applicant data. 
#Some users typed real budgets, some typed text numbers, and some typed complete gibberish to bypass the form constraints. 
#You need to sum the total budget of only the valid entries without letting the script crash.
incoming_applications = [
    {"applicant": "User_1", "budget": 4000},
    {"applicant": "User_2", "budget": "1500 USD"},
    {"applicant": "User_3", "budget": "Negotiable"},
    {"applicant": "User_4", "budget": "FREE"},
    {"applicant": "User_5", "budget": "3000 INR"}]

budgetsum=[]
for i in incoming_applications:
    try:
        if type(i["budget"])==str:
            a=i["budget"].split()
            b=a[0]
            budgetsum.append(int(b))
        else:
            budgetsum.append(i["budget"])
        print("Total sum is:",sum(budgetsum))
    except:
        print("The entry is not valid,skipping gracefully!",i["applicant"])
              



