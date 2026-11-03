import os

CLEARANCE_FILE = "clearance_records.txt"

def add_student_clearance():
    roll = input("Enter Student Roll Number: ").strip()
    name = input("Enter Student Name: ").strip()
    library_dues = input("Enter Library Dues (PKR): ").strip()
    fee_dues = input("Enter Tuition/Misc Dues (PKR): ").strip()
    
    if roll != "" and name != "" and library_dues.isdigit() and fee_dues.isdigit():
        lib_val = int(library_dues)
        fee_val = int(fee_dues)
        
        status = "Cleared"
        if lib_val > 0 or fee_val > 0:
            status = "Pending Dues"
            
        f = open(CLEARANCE_FILE, "a")
        f.write(roll + "," + name + "," + str(lib_val) + "," + str(fee_val) + "," + status + "\n")
        f.close()
        print("Clearance record added successfully!")
    else:
        print("Invalid input! Ensure dues amounts are numeric.")

def view_clearance_list():
    if not os.path.exists(CLEARANCE_FILE):
        print("No clearance records found!")
        return
        
    f = open(CLEARANCE_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Clearance register is empty!")
        return
        
    print("\n--- Central Clearance Register ---")
    print("Roll No\t\tStudent Name\t\tLib Fine\tMisc Dues\tClearance Status")
    print("-" * 75)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5:
            roll, name, lib, fee, status = parts
            print(roll + "\t\t" + name + "\t\tRs." + lib + "\t\tRs." + fee + "\t\t" + status)

def clear_dues():
    if not os.path.exists(CLEARANCE_FILE):
        print("No clearance records exist!")
        return
        
    target = input("Enter Roll Number to mark dues cleared: ").strip()
    if target == "":
        print("Roll number cannot be blank!")
        return
        
    f = open(CLEARANCE_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5 and parts[0] == target:
            parts[2] = "0"
            parts[3] = "0"
            parts[4] = "Cleared"
            found = True
            print("All dues for Roll No " + target + " cleared successfully!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(CLEARANCE_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Student roll number not found in clearance records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Central Clearance Management System ===")

while True:
    print("\n1. Add Student Clearance Record")
    print("2. View All Clearance Records")
    print("3. Settle / Clear Student Dues")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        add_student_clearance()
    elif opt == "2":
        view_clearance_list()
    elif opt == "3":
        clear_dues()
    elif opt == "4":
        print("Closing clearance management system... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
