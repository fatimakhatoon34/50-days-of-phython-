import os

ALUMNI_FILE = "alumni_records.txt"

def add_alumni():
    name = input("Enter Alumni Name: ").strip()
    year_str = input("Enter Passing Year (e.g. 2024): ").strip()
    degree = input("Enter Degree Program (e.g. ICS / FSC): ").strip()
    current_status = input("Enter Current Status / University: ").strip()
    
    if name != "" and year_str.isdigit() and degree != "" and current_status != "":
        f = open(ALUMNI_FILE, "a")
        f.write(name + "," + year_str + "," + degree + "," + current_status + "\n")
        f.close()
        print("Alumni record added successfully!")
    else:
        print("Invalid input! Check fields or numeric passing year.")

def view_alumni():
    if not os.path.exists(ALUMNI_FILE):
        print("No alumni records found!")
        return
        
    f = open(ALUMNI_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Alumni directory is empty!")
        return
        
    print("\n--- College Alumni Directory ---")
    print("Name\t\tPassing Year\tProgram\t\tCurrent Status / University")
    print("-" * 70)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            name, year, degree, status = parts
            print(name + "\t\t" + year + "\t\t" + degree + "\t\t" + status)

def search_alumni():
    if not os.path.exists(ALUMNI_FILE):
        print("No alumni records exist!")
        return
        
    target_year = input("Enter Passing Year to filter (e.g. 2024): ").strip()
    if not target_year.isdigit():
        print("Passing year must be numeric!")
        return
        
    f = open(ALUMNI_FILE, "r")
    lines = f.readlines()
    f.close()
    
    print("\n--- Alumni from Year " + target_year + " ---")
    found = False
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[1] == target_year:
            print("Name: " + parts[0] + " | Program: " + parts[2] + " | Status: " + parts[3])
            found = True
            
    if not found:
        print("No alumni found for the year " + target_year + ".")

# Main Program Loop (Infinite Loop with Break)
print("=== College Alumni Directory System ===")

while True:
    print("\n1. Add Alumni Record")
    print("2. View All Alumni Directory")
    print("3. Search Alumni by Passing Year")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        add_alumni()
    elif opt == "2":
        view_alumni()
    elif opt == "3":
        search_alumni()
    elif opt == "4":
        print("Closing alumni directory... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
