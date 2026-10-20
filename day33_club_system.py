import os

CLUB_FILE = "club_members.txt"

def register_member():
    roll = input("Enter Roll Number (e.g. ICS-101): ").strip()
    name = input("Enter Student Name: ").strip()
    club = input("Enter Club Name (e.g. Coding / Science / Sports): ").strip()
    
    if roll != "" and name != "" and club != "":
        f = open(CLUB_FILE, "a")
        f.write(roll + "," + name + "," + club + ",Active\n")
        f.close()
        print("Student registered for club successfully!")
    else:
        print("Fields cannot be empty!")

def view_members():
    if not os.path.exists(CLUB_FILE):
        print("No club records found!")
        return
        
    f = open(CLUB_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Club membership list is empty!")
        return
        
    print("\n--- Student Club Memberships ---")
    print("Roll No\t\tStudent Name\t\tClub Name\tStatus")
    print("-" * 60)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            roll, name, club, status = parts
            print(roll + "\t\t" + name + "\t\t" + club + "\t" + status)

def cancel_membership():
    if not os.path.exists(CLUB_FILE):
        print("No club records exist!")
        return
        
    target = input("Enter Roll Number to cancel membership: ").strip()
    if target == "":
        print("Roll number cannot be blank!")
        return
        
    f = open(CLUB_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[0] == target:
            parts[3] = "Inactive"
            found = True
            print("Membership for Roll No " + target + " marked as Inactive!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(CLUB_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Student roll number not found in club records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Student Club & Society System ===")

while True:
    print("\n1. Register Club Member")
    print("2. View All Memberships")
    print("3. Cancel Membership")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        register_member()
    elif opt == "2":
        view_members()
    elif opt == "3":
        cancel_membership()
    elif opt == "4":
        print("Closing club management system... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
