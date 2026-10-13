import os

ACCOUNT_FILE = "bank_account.txt"

def setup_account():
    if os.path.exists(ACCOUNT_FILE):
        return
        
    print("\n--- First Time Setup ---")
    pin = input("Set a 4-digit PIN: ").strip()
    balance_str = input("Enter initial deposit amount (Rs): ").strip()
    
    if pin.isdigit() and len(pin) == 4 and balance_str.isdigit():
        f = open(ACCOUNT_FILE, "w")
        f.write(pin + "," + balance_str + "\n")
        f.close()
        print("Account created successfully!")
    else:
        print("Invalid setup values! Defaulting PIN to 1234 and balance to 1000.")
        f = open(ACCOUNT_FILE, "w")
        f.write("1234,1000\n")
        f.close()

def verify_pin():
    setup_account()
    
    f = open(ACCOUNT_FILE, "r")
    line = f.readline().strip()
    f.close()
    
    parts = line.split(",")
    saved_pin = parts[0]
    
    entered_pin = input("Enter your 4-digit PIN: ").strip()
    if entered_pin == saved_pin:
        return True
    else:
        print("Incorrect PIN!")
        return False

def check_balance():
    f = open(ACCOUNT_FILE, "r")
    line = f.readline().strip()
    f.close()
    
    parts = line.split(",")
    print("\nCurrent Account Balance: Rs. " + parts[1])

def deposit_money():
    f = open(ACCOUNT_FILE, "r")
    line = f.readline().strip()
    f.close()
    
    parts = line.split(",")
    pin = parts[0]
    balance = int(parts[1])
    
    amount_str = input("Enter amount to deposit: ").strip()
    if amount_str.isdigit():
        amount = int(amount_str)
        balance = balance + amount
        
        f = open(ACCOUNT_FILE, "w")
        f.write(pin + "," + str(balance) + "\n")
        f.close()
        print("Successfully deposited Rs. " + str(amount))
        print("Updated Balance: Rs. " + str(balance))
    else:
        print("Invalid amount entered!")

def withdraw_money():
    f = open(ACCOUNT_FILE, "r")
    line = f.readline().strip()
    f.close()
    
    parts = line.split(",")
    pin = parts[0]
    balance = int(parts[1])
    
    amount_str = input("Enter amount to withdraw: ").strip()
    if amount_str.isdigit():
        amount = int(amount_str)
        if amount <= balance:
            balance = balance - amount
            
            f = open(ACCOUNT_FILE, "w")
            f.write(pin + "," + str(balance) + "\n")
            f.close()
            print("Successfully withdrew Rs. " + str(amount))
            print("Remaining Balance: Rs. " + str(balance))
        else:
            print("Insufficient balance!")
    else:
            print("Invalid amount entered!")

# Main Program Loop
print("=== Student ATM Simulation ===")

if verify_pin():
    run = True
    while run:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        opt = input("Choice (1-4): ").strip()
        
        if opt == "1":
            check_balance()
        elif opt == "2":
            deposit_money()
        elif opt == "3":
            withdraw_money()
        elif opt == "4":
            print("Thank you for banking with us. Allah Hafiz!")
            run = False
        else:
            print("Invalid choice!")
