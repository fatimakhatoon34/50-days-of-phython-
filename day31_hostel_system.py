import os

HOSTEL_FILE = "hostel_records.txt"

def allocate_room():
    room_no = input("Enter Room Number (e.g. R-102): ").strip()
    student_name = input("Enter Student Name: ").strip()
    department = input("Enter Department/Program (e.g. ICS): ").strip()
    
    if room_no != "" and student_name != "" and department != "":
        f = open(HOSTEL_FILE, "a")
        f.write(room_no + "," + student_name + "," + department + ",Allocated\n")
        f.close()
        print("Room allocated successfully!")
    else:
        print("Fields cannot be empty!")

def view_allocations():
    if not os.path.exists(HOSTEL_FILE):
        print("No hostel records found!")
        return
        
    f = open(HOSTEL_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Hostel record file is empty!")
        return
        
    print("\n--- Hostel Room Allocation List ---")
    print("Room No\t\tStudent Name\t\tDepartment\tStatus")
    print("-" * 60)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            r_no, name, dept, status = parts
            print(r_no + "\t\t" + name + "\t\t" + dept + "\t" + status)

def vacate_room():
    if not os.path.exists(HOSTEL_FILE):
        print("No hostel records exist!")
        return
        
    target = input("Enter Room Number to vacate: ").strip()
    if target == "":
        print("Room number cannot be blank!")
        return
        
    f = open(HOSTEL_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[0] == target:
            parts[3] = "Vacant"
            found = True
            print("Room " + target + " marked as Vacant!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(HOSTEL_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Room number not found in records.")

# Main Program Loop
print("=== Student Hostel Management System ==pss")

run = True
while run:
    print("\n1. Allocate Room")
    print("\n2. View Room Allocations")
    print("3. Vacate Room")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        allocate_room()
    elif opt == "2":
        view_allocations()
    elif opt == "3":
        vacate_room()
    elif opt == "4":
        print("Closing hostel system... Allah Hafiz!")
        run = False
    else:
        print("Invalid option!")
