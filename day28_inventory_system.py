import os

INV_FILE = "inventory_data.txt"

def add_item():
    item_id = input("Enter Item ID (e.g. ITM-01): ").strip()
    name = input("Enter Item Name: ").strip()
    price_str = input("Enter Price (Rs): ").strip()
    qty_str = input("Enter Quantity in Stock: ").strip()
    
    if item_id != "" and name != "" and price_str.isdigit() and qty_str.isdigit():
        f = open(INV_FILE, "a")
        f.write(item_id + "," + name + "," + price_str + "," + qty_str + "\n")
        f.close()
        print("Item added to inventory successfully!")
    else:
        print("Invalid input! Check IDs, names, or numeric values.")

def view_inventory():
    if not os.path.exists(INV_FILE):
        print("Inventory file not found!")
        return
        
    f = open(INV_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Inventory is empty!")
        return
        
    print("\n--- Current Inventory Stock ---")
    print("ID\t\tItem Name\tPrice (Rs)\tQuantity")
    print("-" * 55)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            i_id, name, price, qty = parts
            print(i_id + "\t\t" + name + "\t\t" + price + "\t\t" + qty)

def update_stock():
    if not os.path.exists(INV_FILE):
        print("No inventory file found!")
        return
        
    target = input("Enter Item ID to update quantity: ").strip()
    new_qty_str = input("Enter new quantity: ").strip()
    
    if not new_qty_str.isdigit():
        print("Quantity must be a number!")
        return
        
    f = open(INV_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[0] == target:
            parts[3] = new_qty_str
            found = True
            print("Stock quantity updated successfully!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(INV_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Item ID not found.")

# Main Program Loop
print("=== Student Inventory Management System ===")

run = True
while run:
    print("\n1. Add New Item")
    print("2. View Inventory Stock")
    print("3. Update Item Quantity")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        add_item()
    elif opt == "2":
        view_inventory()
    elif opt == "3":
        update_stock()
    elif opt == "4":
        print("Closing inventory system... Allah Hafiz!")
        run = False
    else:
        print("Invalid choice!")
