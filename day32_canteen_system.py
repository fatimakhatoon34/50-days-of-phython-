import os

MENU_FILE = "canteen_menu.txt"

def add_menu_item():
    item_code = input("Enter Item Code (e.g. F-01): ").strip()
    item_name = input("Enter Food Item Name (e.g. Burger): ").strip()
    price_str = input("Enter Price (Rs): ").strip()
    
    if item_code != "" and item_name != "" and price_str.isdigit():
        f = open(MENU_FILE, "a")
        f.write(item_code + "," + item_name + "," + price_str + "\n")
        f.close()
        print("Menu item added successfully!")
    else:
        print("Invalid input! Check codes, names, or numeric prices.")

def view_menu():
    if not os.path.exists(MENU_FILE):
        print("No menu items found! Please add items first.")
        return
        
    f = open(MENU_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Canteen menu is empty!")
        return
        
    print("\n--- College Canteen Menu ---")
    print("Code\t\tItem Name\t\tPrice (Rs)")
    print("-" * 45)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 3:
            code, name, price = parts
            print(code + "\t\t" + name + "\t\t" + price)

def place_order():
    if not os.path.exists(MENU_FILE):
        print("No menu available to order from!")
        return
        
    f = open(MENU_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Menu is empty!")
        return
        
    view_menu()
    
    total_bill = 0
    ordering = True
    
    print("\n--- Order Processing ---")
    while ordering:
        code_input = input("Enter item code to order (or type 'done' to finish): ").strip()
        
        if code_input.lower() == "done":
            break
            
        qty_str = input("Enter quantity: ").strip()
        if not qty_str.isdigit():
            print("Quantity must be a number!")
            continue
            
        qty = int(qty_str)
        found = False
        
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 3 and parts[0] == code_input:
                item_name = parts[1]
                item_price = int(parts[2])
                cost = item_price * qty
                total_bill = total_bill + cost
                print("Added " + str(qty) + " x " + item_name + " = Rs. " + str(cost))
                found = True
                break
                
        if not found:
            print("Invalid item code!")
            
    print("\n==============================")
    print("Total Bill Amount: Rs. " + str(total_bill))
    print("==============================")

# Main Program Loop
print("=== College Canteen Billing System ===")

run = True
while run:
    print("\n1. Add Menu Item")
    print("2. View Canteen Menu")
    print("3. Place Food Order & Bill")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        add_menu_item()
    elif opt == "2":
        view_menu()
    elif opt == "3":
        place_order()
    elif opt == "4":
        print("Closing canteen system... Allah Hafiz!")
        run = False
    else:
        print("Invalid option!")
