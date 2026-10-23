import os

SCHOLARSHIP_FILE = "scholarship_records.txt"

def add_application():
    app_id = input("Enter Application ID (e.g. SCH-01): ").strip()
    name = input("Enter Scholarship Name (e.g. Merit Scholarship): ").strip()
    provider = input("Enter Provider / Organization: ").strip()
    
    if app_id != "" and name != "" and provider != "":
        f = open(SCHOLARSHIP_FILE, "a")
        f.write(app_id + "," + name + "," + provider + ",Applied\n")
        f.close()
        print("Scholarship application recorded successfully!")
    else:
        print("Fields cannot be empty!")

def view_applications():
    if not os.path.exists(SCHOLARSHIP_FILE):
        print("No scholarship records found!")
        return
        
    f = open(SCHOLARSHIP_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Scholarship records file is empty!")
        return
        
    print("\n--- Scholarship Applications Catalog ---")
    print("App ID\t\tScholarship Name\tProvider\t\tStatus")
    print("-" * 65)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            app_id, name, provider, status = parts
            print(app_id + "\t\t" + name + "\t\t" + provider + "\t\t" + status)

def update_status():
    if not os.path.exists(SCHOLARSHIP_FILE):
        print("No scholarship records exist!")
        return
        
    target = input("Enter Application ID to update status: ").strip()
    if target == "":
        print("Application ID cannot be blank!")
        return
        
    new_status = input("Enter new status (Shortlisted / Awarded / Rejected): ").strip()
    if new_status == "":
        print("Status cannot be blank!")
        return
        
    f = open(SCHOLARSHIP_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[0] == target:
            parts[3] = new_status
            found = True
            print("Application status updated to " + new_status + "!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(SCHOLARSHIP_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Application ID not found.")

# Main Program Loop (Infinite Loop with Break)
print("=== Student Scholarship Application Tracker ===")

while True:
    print("\n1. Add Scholarship Application")
    print("2. View All Applications")
    print("3. Update Application Status")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        add_application()
    elif opt == "2":
        view_applications()
    elif opt == "3":
        update_status()
    elif opt == "4":
        print("Closing scholarship tracker... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
