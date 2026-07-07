#The Freelance Scenario: An international travel agency captures custom trip costs from users globally.
#Some are numbers, some are string formats, and some are junk text. 
#They want you to build an isolated data cleaner function, then use that function to process a raw webhook response.

# ==========================================
# STEP 1: DEFINE THE ISOLATED MACHINE (At the top)
# ==========================================
def parse_amount(val):
    """
    This machine takes ONE value (val), cleans it, 
    and RETURNS a clean integer or 0 if it's junk.
    """
    try:
        if type(val) == str:
            parts = val.split()
            return int(parts[0])  # Returns clean number from string
        else:
            return int(val)       # Returns clean number directly
    except:
        # If it's "Unknown" or "TBD", int() fails, jumping here!
        return 0                  # Returns 0 as a safe placeholder

# ==========================================
# STEP 2: YOUR RAW DATASET
# ==========================================
trip_expenses = [
    {"destination": "Paris", "cost": "2500 EUR"},
    {"destination": "Tokyo", "cost": 4000},
    {"destination": "Mumbai", "cost": "Unknown"},  
    {"destination": "New York", "cost": "3500 USD"},
    {"destination": "Goa", "cost": "TBD"}          
]

# ==========================================
# STEP 3: RUN THE PIPELINE (At the bottom)
# ==========================================
cleaned_cost = []

for item in trip_expenses:
    # 1. Extract the raw value
    raw_val = item["cost"]
    
    # 2. Feed it into our machine and CATCH the returned output
    clean_num = parse_amount(raw_val)
    
    # 3. Save the caught output into our tracking list
    cleaned_cost.append(clean_num)

# Print the final calculated result!
print("The total cleaned budget is =", sum(cleaned_cost))


#new problem
def cleanscore(score):
    try:
        if score=="ABSENT":
            return 0
        else:
            return int(score)
    except:
        return 0

finalmarks=[]
raw_scores = [85, 92, "ABSENT", 78, "ABSENT"]
for i in raw_scores:
    a=cleanscore(i)
    finalmarks.append(a)
print('total marks',sum(finalmarks))