import os

ASSIGNMENT_FILE = "assignment_records.txt"

def add_assignment():
    task_id = input("Enter Task ID (e.g. HW-01): ").strip()
    subject = input("Enter Subject Name (e.g. Computer Science): ").strip()
    title = input("Enter Assignment Title / Topic: ").strip()
    deadline = input("Enter Deadline Date (e.g. 15-Nov-2026): ").strip()
    
    if task_id != "" and subject != "" and title != "" and deadline != "":
        f = open(ASSIGNMENT_FILE, "a")
        f.write(task_id + "," + subject + "," + title + "," + deadline + ",Pending\n")
        f.close()
        print("Assignment recorded successfully!")
    else:
        print("Fields cannot be empty!")

def view_assignments():
    if not os.path.exists(ASSIGNMENT_FILE):
        print("No assignment records found!")
        return
        
    f = open(ASSIGNMENT_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Assignment register is empty!")
        return
        
    print("\n--- Student Assignment Register ---")
    print("ID\t\tSubject\t\tTitle\t\t\tDeadline\tStatus")
    print("-" * 70)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5:
            t_id, subj, title, deadline, status = parts
            print(t_id + "\t\t" + subj + "\t\t" + title + "\t\t" + deadline + "\t" + status)

def update_status():
    if not os.path.exists(ASSIGNMENT_FILE):
        print("No assignment records exist!")
        return
        
    target = input("Enter Task ID to mark as Submitted: ").strip()
    if target == "":
        print("Task ID cannot be blank!")
        return
        
    f = open(ASSIGNMENT_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5 and parts[0] == target:
            parts[4] = "Submitted"
            found = True
            print("Assignment " + target + " marked as Submitted!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(ASSIGNMENT_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Task ID not found in records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Student Assignment Tracker ===")

while True:
    print("\n1. Add New Assignment Task")
    print("2. View Assignment Register")
    print("3. Mark Task as Submitted")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        add_assignment()
    elif opt == "2":
        view_assignments()
    elif opt == "3":
        update_status()
    elif opt == "4":
        print("Closing assignment tracker... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
