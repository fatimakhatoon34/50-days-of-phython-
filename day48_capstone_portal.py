import os

CAPSTONE_FILE = "capstone_records.txt"

def register_project():
    project_id = input("Enter Project ID (e.g. PRJ-01): ").strip()
    title = input("Enter Project Title / Topic: ").strip()
    domain = input("Enter Domain (e.g. AI / Web / CLI Tool): ").strip()
    supervisor = input("Enter Supervisor Name: ").strip()
    
    if project_id != "" and title != "" and domain != "" and supervisor != "":
        f = open(CAPSTONE_FILE, "a")
        f.write(project_id + "," + title + "," + domain + "," + supervisor + ",In Progress\n")
        f.close()
        print("Capstone project registered successfully!")
    else:
        print("Fields cannot be empty!")

def view_projects():
    if not os.path.exists(CAPSTONE_FILE):
        print("No capstone project records found!")
        return
        
    f = open(CAPSTONE_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Capstone project register is empty!")
        return
        
    print("\n--- Student Capstone Project Register ---")
    print("Project ID\tTitle\t\t\tDomain\t\tSupervisor\tStatus")
    print("-" * 75)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5:
            p_id, title, domain, supervisor, status = parts
            print(p_id + "\t\t" + title + "\t\t" + domain + "\t\t" + supervisor + "\t" + status)

def complete_project():
    if not os.path.exists(CAPSTONE_FILE):
        print("No project records exist!")
        return
        
    target = input("Enter Project ID to mark as Completed: ").strip()
    if target == "":
        print("Project ID cannot be blank!")
        return
        
    f = open(CAPSTONE_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5 and parts[0] == target:
            parts[4] = "Completed"
            found = True
            print("Project ID " + target + " marked as Completed!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(CAPSTONE_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Project ID not found in capstone records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Student Capstone Project Portal ===")

while True:
    print("\n1. Register New Capstone Project")
    print("2. View All Capstone Projects")
    print("3. Mark Project as Completed")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        register_project()
    elif opt == "2":
        view_projects()
    elif opt == "3":
        complete_project()
    elif opt == "4":
        print("Closing capstone portal... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
