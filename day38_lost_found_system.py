import os

LOST_FOUND_FILE = "lost_found_records.txt"

def report_item():
    item_id = input("Enter Item ID (e.g. LF-01): ").strip()
    item_name = input("Enter Item Name (e.g. Calculator / USB Drive): ").strip()
    location = input("Enter Location Found/Lost (e.g. IT Lab 1): ").strip()
    status_type = input("Enter Type (Lost / Found): ").strip().capitalize()
    
    if item_id != "" and item_name != "" and location != "" and (status_type == "Lost" or status_type == "Found"):
        f = open(LOST_FOUND_FILE, "a")
        f.write(item_id + "," + item_name + "," + location + "," + status_type + ",Open\n")
        f.close()
        print("Item record added successfully!")
    else:
        print("Invalid input! Check fields or item type (Lost/Found).")

def view_items():
    if not os.path.exists(LOST_FOUND_FILE):
        print("No lost and found records found!")
        return
        
    f = open(LOST_FOUND_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Lost and found register is empty!")
        return
        
    print("\n--- Campus Lost & Found Register ---")
    print("ID\t\tItem Name\t\tLocation\t\tType\tStatus")
    print("-" * 65)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5:
            i_id, name, loc, i_type, status = parts
            print(i_id + "\t\t" + name + "\t\t" + loc + "\t\t" + i_type + "\t" + status)

def resolve_item():
    if not os.path.exists(LOST_FOUND_FILE):
        print("No records exist to update!")
        return
        
    target = input("Enter Item ID to mark as Claimed/Resolved: ").strip()
    if target == "":
        print("Item ID cannot be blank!")
        return
        
    f = open(LOST_FOUND_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5 and parts[0] == target:
            parts[4] = "Claimed"
            found = True
            print("Item ID " + target + " marked as Claimed!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(LOST_FOUND_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Item ID not found in records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Campus Lost & Found System ===")

while True:
    print("\n1. Report Lost or Found Item")
    print("\n2. View All Items Register")
    print("3. Mark Item as Claimed / Resolved")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        report_item()
    elif opt == "2":
        view_items()
    elif opt == "3":
        resolve_item()
    elif opt == "4":
        print("Closing lost and found system... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
