import os

LOCKER_FILE = "locker_records.txt"

def allocate_locker():
    locker_no = input("Enter Locker Number (e.g. L-101): ").strip()
    roll = input("Enter Student Roll Number: ").strip()
    name = input("Enter Student Name: ").strip()
    
    if locker_no != "" and roll != "" and name != "":
        f = open(LOCKER_FILE, "a")
        f.write(locker_no + "," + roll + "," + name + ",Occupied\n")
        f.close()
        print("Locker allocated successfully!")
    else:
        print("Fields cannot be empty!")

def view_lockers():
    if not os.path.exists(LOCKER_FILE):
        print("No locker records found!")
        return
        
    f = open(LOCKER_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Locker register is empty!")
        return
        
    print("\n--- Campus Locker Status Register ---")
    print("Locker No\tRoll No\t\tStudent Name\t\tStatus")
    print("-" * 60)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            l_no, r_no, name, status = parts
            print(l_no + "\t\t" + r_no + "\t\t" + name + "\t\t" + status)

def vacate_locker():
    if not os.path.exists(LOCKER_FILE):
        print("No locker records exist!")
        return
        
    target = input("Enter Locker Number to vacate: ").strip()
    if target == "":
        print("Locker number cannot be blank!")
        return
        
    f = open(LOCKER_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[0] == target:
            parts[3] = "Available"
            found = True
            print("Locker " + target + " marked as Available!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(LOCKER_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Locker number not found in records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Student Locker Allocation System ===")

while True:
    print("\n1. Allocate Locker")
    print("2. View Locker Status Register")
    print("3. Vacate Locker")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        allocate_locker()
    elif opt == "2":
        view_lockers()
    elif opt == "3":
        vacate_locker()
    elif opt == "4":
        print("Closing locker system... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
