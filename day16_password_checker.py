import random

def check_strength(pwd):
    length = len(pwd)
    has_up = False
    has_low = False
    has_num = False
    has_sym = False
    
    symbols = "!@#$%^&*"
    
    for c in pwd:
        if c.isupper():
            has_up = True
        elif c.islower():
            has_low = True
        elif c.isdigit():
            has_num = True
        elif c in symbols:
            has_sym = True
            
    score = 0
    if length >= 8:
        score = score + 1
    if has_up:
        score = score + 1
    if has_low:
        score = score + 1
    if has_num:
        score = score + 1
    if has_sym:
        score = score + 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

def make_password(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    p = ""
    for i in range(length):
        p = p + random.choice(chars)
    return p

# Main Code
print("=== Password Security Tool ===")

run = True
while run:
    print("\n1. Check Password Strength")
    print("2. Generate Random Password")
    print("3. Exit")
    
    opt = input("Choice (1-3): ").strip()
    
    if opt == "1":
        p_input = input("Enter password: ").strip()
        result = check_strength(p_input)
        print("Rating: " + result)

    elif opt == "2":
        l = int(input("Enter length: "))
        if l >= 4:
            new_p = make_password(l)
            rate = check_strength(new_p)
            print("Generated: " + new_p)
            print("Rating: " + rate)
        else:
            print("Too short! Minimum length is 4.")

    elif opt == "3":
        print("Closing program... Allah Hafiz")
        run = False

    else:
        print("Invalid option!")
