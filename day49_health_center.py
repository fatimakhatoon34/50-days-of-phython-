import os

HEALTH_FILE = "health_records.txt"

def log_visit():
    visit_id = input("Enter Visit ID (e.g. HC-01): ").strip()
    roll = input("Enter Student Roll Number: ").strip()
    symptoms = input("Enter Symptoms / Reason (e.g. Fever / Headache): ").strip()
    treatment = input("Enter Treatment / First Aid Provided: ").strip()
    
    if visit_id != "" and roll != "" and symptoms != "" and treatment != "":
        f = open(HEALTH_FILE, "a")
        f.write(visit_id + "," + roll + "," + symptoms + "," + treatment + ",Under Observation\n")
        f.close()
        print("Health record logged successfully!")
    else:
        print("Fields cannot be empty!")

def view_visits():
    if not os.path.exists(HEALTH_FILE):
        print("No health center records found!")
        return
        
    f = open(HEALTH_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Health center log is empty!")
        return
        
    print("\n--- Campus Health Center Log ---")
    print("Visit ID\tRoll No\t\tSymptoms\t\tTreatment\t\tStatus")
    print("-" * 75)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5:
            v_id, roll, symptoms, treatment, status = parts
            print(v_id + "\t\t" + roll + "\t\t" + symptoms + "\t\t" + treatment + "\t\t" + status)

def discharge_student():
    if not os.path.exists(HEALTH_FILE):
        print("No health records exist!")
        return
        
    target = input("Enter Visit ID to mark as Discharged: ").strip()
    if target == "":
        print("Visit ID cannot be blank!")
        return
        
    f = open(HEALTH_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5 and parts[0] == target:
            parts[4] = "Discharged"
            found = True
            print("Visit ID " + target + " marked as Discharged!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(HEALTH_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Visit ID not found in health records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Campus Health Center & Sick Bay Tracker ===")

while True:
    print("\n1. Log Student Health Center Visit")
    print("2. View All Health Records")
    print("3. Mark Student as Discharged")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        log_visit()
    elif opt == "2":
        view_visits()
    elif opt == "3":
        discharge_student()
    elif opt == "4":
        print("Closing health center tracker... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
