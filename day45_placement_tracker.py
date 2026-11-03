import os

PLACEMENT_FILE = "placement_records.txt"

def add_placement():
    record_id = input("Enter Record ID (e.g. PL-01): ").strip()
    roll = input("Enter Student Roll Number: ").strip()
    company = input("Enter Company / Organization Name: ").strip()
    role = input("Enter Internship Role (e.g. Python Dev Intern): ").strip()
    
    if record_id != "" and roll != "" and company != "" and role != "":
        f = open(PLACEMENT_FILE, "a")
        f.write(record_id + "," + roll + "," + company + "," + role + ",Applied\n")
        f.close()
        print("Internship application recorded successfully!")
    else:
        print("Fields cannot be empty!")

def view_placements():
    if not os.path.exists(PLACEMENT_FILE):
        print("No placement records found!")
        return
        
    f = open(PLACEMENT_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Placement register is empty!")
        return
        
    print("\n--- Student Career & Placement Register ---")
    print("ID\t\tRoll No\t\tCompany Name\t\tRole\t\t\tStatus")
    print("-" * 75)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5:
            r_id, roll, comp, role, status = parts
            print(r_id + "\t\t" + roll + "\t\t" + comp + "\t\t" + role + "\t" + status)

def update_status():
    if not os.path.exists(PLACEMENT_FILE):
        print("No placement records exist!")
        return
        
    target = input("Enter Record ID to update status (e.g. Offered / Accepted): ").strip()
    if target == "":
        print("Record ID cannot be blank!")
        return
        
    new_status = input("Enter new status (Offered / Accepted / Rejected): ").strip()
    if new_status == "":
        print("Status cannot be blank!")
        return
        
    f = open(PLACEMENT_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5 and parts[0] == target:
            parts[4] = new_status
            found = True
            print("Record ID " + target + " status updated to " + new_status + "!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(PLACEMENT_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Record ID not found in placement records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Student Internship & Placement Tracker ===")

while True:
    print("\n1. Add Internship Application")
    print("2. View All Placement Records")
    print("3. Update Placement Status")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        add_placement()
    elif opt == "2":
        view_placements()
    elif opt == "3":
        update_status()
    elif opt == "4":
        print("Closing placement tracker... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
