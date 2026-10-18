import os

TRANSPORT_FILE = "transport_records.txt"

def issue_pass():
    roll = input("Enter Student Roll Number (e.g. ICS-101): ").strip()
    name = input("Enter Student Name: ").strip()
    route = input("Enter Bus Route / Area (e.g. Route 4 - G-9): ").strip()
    fee_str = input("Enter Monthly Transport Fee (Rs): ").strip()
    
    if roll != "" and name != "" and route != "" and fee_str.isdigit():
        f = open(TRANSPORT_FILE, "a")
        f.write(roll + "," + name + "," + route + "," + fee_str + ",Active\n")
        f.close()
        print("Bus pass issued successfully!")
    else:
        print("Invalid input! Check fields or numeric transport fee.")

def view_passes():
    if not os.path.exists(TRANSPORT_FILE):
        print("No transport records found!")
        return
        
    f = open(TRANSPORT_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Transport record file is empty!")
        return
        
    print("\n--- Student Bus Pass Records ---")
    print("Roll No\t\tName\t\tRoute\t\tFee (Rs)\tStatus")
    print("-" * 65)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5:
            roll, name, route, fee, status = parts
            print(roll + "\t\t" + name + "\t\t" + route + "\t" + fee + "\t\t" + status)

def cancel_pass():
    if not os.path.exists(TRANSPORT_FILE):
        print("No transport records exist!")
        return
        
    target = input("Enter Roll Number to cancel bus pass: ").strip()
    if target == "":
        print("Roll number cannot be blank!")
        return
        
    f = open(TRANSPORT_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5 and parts[0] == target:
            parts[4] = "Cancelled"
            found = True
            print("Bus pass for Roll No " + target + " marked as Cancelled!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(TRANSPORT_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Student roll number not found.")

# Main Program Loop
print("=== Student Transport Management System ===")

run = True
while run:
    print("\n1. Issue Bus Pass")
    print("2. View All Bus Passes")
    print("3. Cancel Bus Pass")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        issue_pass()
    elif opt == "2":
        view_passes()
    elif opt == "3":
        cancel_pass()
    elif opt == "4":
        print("Closing transport system... Allah Hafiz!")
        run = False
    else:
        print("Invalid option!")
