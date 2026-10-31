import os

VISITOR_FILE = "visitor_records.txt"

def issue_pass():
    pass_id = input("Enter Pass ID (e.g. VST-101): ").strip()
    visitor_name = input("Enter Visitor Name: ").strip()
    cnic = input("Enter Visitor CNIC / ID Number: ").strip()
    purpose = input("Enter Purpose of Visit (e.g. Admissions / Meeting): ").strip()
    
    if pass_id != "" and visitor_name != "" and cnic != "" and purpose != "":
        f = open(VISITOR_FILE, "a")
        f.write(pass_id + "," + visitor_name + "," + cnic + "," + purpose + ",Inside\n")
        f.close()
        print("Visitor pass issued successfully!")
    else:
        print("Fields cannot be empty!")

def view_visitors():
    if not os.path.exists(VISITOR_FILE):
        print("No visitor records found!")
        return
        
    f = open(VISITOR_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Visitor log is empty!")
        return
        
    print("\n--- Campus Visitor Log ---")
    print("Pass ID\t\tVisitor Name\t\tCNIC/ID\t\t\tPurpose\t\tStatus")
    print("-" * 75)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5:
            p_id, name, cnic_no, purpose, status = parts
            print(p_id + "\t\t" + name + "\t\t" + cnic_no + "\t\t" + purpose + "\t" + status)

def checkout_visitor():
    if not os.path.exists(VISITOR_FILE):
        print("No visitor records exist!")
        return
        
    target = input("Enter Pass ID to mark visitor exit: ").strip()
    if target == "":
        print("Pass ID cannot be blank!")
        return
        
    f = open(VISITOR_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5 and parts[0] == target:
            parts[4] = "Exited"
            found = True
            print("Visitor with Pass ID " + target + " marked as Exited!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(VISITOR_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Pass ID not found in visitor records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Campus Security & Visitor Pass System ===")

while True:
    print("\n1. Issue Visitor Pass")
    print("2. View All Campus Visitors")
    print("3. Mark Visitor Exit / Checkout")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        issue_pass()
    elif opt == "2":
        view_visitors()
    elif opt == "3":
        checkout_visitor()
    elif opt == "4":
        print("Closing visitor pass system... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
