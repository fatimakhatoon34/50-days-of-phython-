# Day 44: Campus Sports Equipment & Field System
# ICS Computer Science Lab Practice - FBISE

import os

SPORTS_FILE = "sports_records.txt"

def issue_equipment():
    issue_id = input("Enter Issue ID (e.g. SP-01): ").strip()
    roll = input("Enter Student Roll Number: ").strip()
    item_name = input("Enter Item / Field (e.g. Cricket Kit / Football Ground): ").strip()
    
    if issue_id != "" and roll != "" and item_name != "":
        f = open(SPORTS_FILE, "a")
        f.write(issue_id + "," + roll + "," + item_name + ",Issued\n")
        f.close()
        print("Sports gear / field reservation recorded successfully!")
    else:
        print("Fields cannot be empty!")

def view_records():
    if not os.path.exists(SPORTS_FILE):
        print("No sports records found!")
        return
        
    f = open(SPORTS_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Sports register is empty!")
        return
        
    print("\n--- Campus Sports Equipment & Field Register ---")
    print("Issue ID\tRoll No\t\tItem / Field\t\tStatus")
    print("-" * 65)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            i_id, roll, item, status = parts
            print(i_id + "\t\t" + roll + "\t\t" + item + "\t\t" + status)

def return_equipment():
    if not os.path.exists(SPORTS_FILE):
        print("No sports records exist!")
        return
        
    target = input("Enter Issue ID to mark as Returned: ").strip()
    if target == "":
        print("Issue ID cannot be blank!")
        return
        
    f = open(SPORTS_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[0] == target:
            parts[3] = "Returned"
            found = True
            print("Issue ID " + target + " marked as Returned!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(SPORTS_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Issue ID not found in sports records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Campus Sports Equipment & Field System ===")

while True:
    print("\n1. Issue Equipment / Reserve Field")
    print("2. View All Sports Records")
    print("3. Return Equipment / Release Field")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        issue_equipment()
    elif opt == "2":
        view_records()
    elif opt == "3":
        return_equipment()
    elif opt == "4":
        print("Closing sports management system... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
