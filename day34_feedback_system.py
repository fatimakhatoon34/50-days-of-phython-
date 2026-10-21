
import os

FEEDBACK_FILE = "feedback_records.txt"

def submit_feedback():
    roll = input("Enter Student Roll Number (e.g. ICS-101): ").strip()
    category = input("Enter Category (e.g. IT Lab / Library / Canteen): ").strip()
    message = input("Enter Complaint / Feedback Message: ").strip()
    
    if roll != "" and category != "" and message != "":
        f = open(FEEDBACK_FILE, "a")
        f.write(roll + "," + category + "," + message + ",Pending\n")
        f.close()
        print("Feedback submitted successfully!")
    else:
        print("Fields cannot be empty!")

def view_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        print("No feedback records found!")
        return
        
    f = open(FEEDBACK_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Feedback record file is empty!")
        return
        
    print("\n--- Student Feedback & Complaints ---")
    print("Roll No\t\tCategory\t\tMessage\t\t\tStatus")
    print("-" * 65)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            roll, cat, msg, status = parts
            print(roll + "\t\t" + cat + "\t\t" + msg + "\t\t" + status)

def resolve_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        print("No feedback records exist!")
        return
        
    target = input("Enter Roll Number to resolve feedback: ").strip()
    if target == "":
        print("Roll number cannot be blank!")
        return
        
    f = open(FEEDBACK_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[0] == target:
            parts[3] = "Resolved"
            found = True
            print("Feedback for Roll No " + target + " marked as Resolved!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(FEEDBACK_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Student roll number not found in feedback records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Student Feedback & Complaint System ===")

while True:
    print("\n1. Submit Feedback / Complaint")
    print("2. View All Feedback Records")
    print("3. Resolve Feedback Item")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        submit_feedback()
    elif opt == "2":
        view_feedback()
    elif opt == "3":
        resolve_feedback()
    elif opt == "4":
        print("Closing feedback system... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
