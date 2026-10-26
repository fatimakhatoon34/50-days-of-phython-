import os

PARKING_FILE = "parking_records.txt"

def allocate_slot():
    slot_no = input("Enter Parking Slot Number (e.g. P-05): ").strip()
    vehicle_no = input("Enter Vehicle Number (e.g. LE-1234): ").strip()
    owner_name = input("Enter Owner Name: ").strip()
    
    if slot_no != "" and vehicle_no != "" and owner_name != "":
        f = open(PARKING_FILE, "a")
        f.write(slot_no + "," + vehicle_no + "," + owner_name + ",Parked\n")
        f.close()
        print("Parking slot allocated successfully!")
    else:
        print("Fields cannot be empty!")

def view_slots():
    if not os.path.exists(PARKING_FILE):
        print("No parking records found!")
        return
        
    f = open(PARKING_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Parking register is empty!")
        return
        
    print("\n--- Campus Parking Lot Status ---")
    print("Slot No\t\tVehicle No\t\tOwner Name\t\tStatus")
    print("-" * 60)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            slot, veh, owner, status = parts
            print(slot + "\t\t" + veh + "\t\t" + owner + "\t\t" + status)

def release_slot():
    if not os.path.exists(PARKING_FILE):
        print("No parking records exist!")
        return
        
    target = input("Enter Parking Slot Number to release: ").strip()
    if target == "":
        print("Slot number cannot be blank!")
        return
        
    f = open(PARKING_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[0] == target:
            parts[3] = "Available"
            found = True
            print("Slot " + target + " marked as Available!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(PARKING_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Parking slot not found in records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Campus Parking Management System ===")

while True:
    print("\n1. Allocate Parking Slot")
    print("2. View Parking Status List")
    print("3. Release Parking Slot")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        allocate_slot()
    elif opt == "2":
        view_slots()
    elif opt == "3":
        release_slot()
    elif opt == "4":
        print("Closing parking system... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
