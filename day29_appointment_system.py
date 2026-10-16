import os

APP_FILE = "appointments.txt"

def book_appointment():
    p_name = input("Enter Patient Name: ").strip()
    doctor = input("Enter Doctor Name (e.g. Dr. Ahmed): ").strip()
    time_slot = input("Enter Time Slot (e.g. 05:00 PM): ").strip()
    
    if p_name != "" and doctor != "" and time_slot != "":
        f = open(APP_FILE, "a")
        f.write(p_name + "," + doctor + "," + time_slot + ",Scheduled\n")
        f.close()
        print("Appointment booked successfully!")
    else:
        print("Fields cannot be empty!")

def view_appointments():
    if not os.path.exists(APP_FILE):
        print("No appointments recorded yet!")
        return
        
    f = open(APP_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("No scheduled appointments found!")
        return
        
    print("\n--- Scheduled Clinic Appointments ---")
    print("Patient Name\t\tDoctor\t\t\tTime Slot\tStatus")
    print("-" * 65)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            p_name, doc, time_s, status = parts
            print(p_name + "\t\t" + doc + "\t\t" + time_s + "\t" + status)

def cancel_appointment():
    if not os.path.exists(APP_FILE):
        print("No appointment records exist!")
        return
        
    target_name = input("Enter Patient Name to cancel appointment: ").strip()
    if target_name == "":
        print("Patient name cannot be blank!")
        return
        
    f = open(APP_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[0].lower() == target_name.lower():
            parts[3] = "Cancelled"
            found = True
            print("Appointment for " + parts[0] + " cancelled successfully!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(APP_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Patient record not found.")

# Main Program Loop
print("=== Student Clinic Appointment System ===")

run = True
while run:
    print("\n1. Book New Appointment")
    print("2. View All Appointments")
    print("3. Cancel Appointment")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        book_appointment()
    elif opt == "2":
        view_appointments()
    elif opt == "3":
        cancel_appointment()
    elif opt == "4":
        print("Closing appointment system... Allah Hafiz!")
        run = False
    else:
        print("Invalid choice!")
