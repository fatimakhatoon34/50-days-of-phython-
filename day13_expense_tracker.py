import datetime
import math
import random

# Function with return value to generate a random receipt code
def generate_receipt_id():
    num = random.randint(1000, 9999)
    code = "EXP-" + str(num)
    return code

# Function to get formatted current date
def get_current_date():
    now = datetime.datetime.now()
    date_str = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    return date_str

# Function returning multiple values for financial summary
def calculate_summary(pocket_money, total_spent):
    remaining = pocket_money - total_spent
    # Using math module to round off percentage
    spent_percentage = math.floor((total_spent / pocket_money) * 100)
    return remaining, spent_percentage

# Main Program
print("=== Student Daily Expense Tracker ===")

allowance = float(input("Enter total monthly pocket money (Rs): "))
expenses = []

flag = True

while flag:
    print("\n1. Add Expense")
    print("2. View Expense Summary")
    print("3. Exit")
    
    choice = input("Select option (1-3): ").strip()
    
    if choice == "1":
        item_name = input("Enter expense name: ").strip().capitalize()
        cost = float(input("Enter cost in Rs: "))
        
        # Calling functions with return values
        receipt_no = generate_receipt_id()
        entry_date = get_current_date()
        
        # Dictionary record
        record = {
            "id": receipt_no,
            "date": entry_date,
            "item": item_name,
            "cost": cost
        }
        
        expenses.append(record)
        print("\nExpense recorded! ID: " + receipt_no + " | Date: " + entry_date)

    elif choice == "2":
        if len(expenses) == 0:
            print("\nNo expenses added yet.")
        else:
            total_spent = 0.0
            print("\n--- Expense List ---")
            for e in expenses:
                print("[" + e["id"] + "] " + e["date"] + " - " + e["item"] + ": Rs. " + str(e["cost"]))
                total_spent = total_spent + e["cost"]
            
            # Unpacking multiple return values from function
            rem_balance, percent_used = calculate_summary(allowance, total_spent)
            
            print("\n--- Summary ---")
            print("Total Pocket Money: Rs. " + str(allowance))
            print("Total Spent: Rs. " + str(total_spent))
            print("Remaining Balance: Rs. " + str(rem_balance))
            print("Allowance Used: " + str(percent_used) + "%")

    elif choice == "3":
        print("\nExiting tracker... Allah Hafiz!")
        flag = False

    else:
        print("\nInvalid choice!")

