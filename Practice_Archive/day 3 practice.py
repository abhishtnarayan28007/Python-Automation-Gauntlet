
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
    except:
        print("The entry is not valid,skipping gracefully!",i["applicant"],",",i["budget"])
print("Total sum is:",sum(budgetsum))