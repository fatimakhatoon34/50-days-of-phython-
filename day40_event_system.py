import os

EVENT_FILE = "event_records.txt"

def book_event():
    event_id = input("Enter Event ID (e.g. EVT-01): ").strip()
    title = input("Enter Event Title (e.g. Tech Symposium): ").strip()
    venue = input("Enter Venue (e.g. Main Auditorium): ").strip()
    organizer = input("Enter Organizer / Society Name: ").strip()
    
    if event_id != "" and title != "" and venue != "" and organizer != "":
        f = open(EVENT_FILE, "a")
        f.write(event_id + "," + title + "," + venue + "," + organizer + ",Scheduled\n")
        f.close()
        print("Event booked successfully!")
    else:
        print("Fields cannot be empty!")

def view_events():
    if not os.path.exists(EVENT_FILE):
        print("No event records found!")
        return
        
    f = open(EVENT_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Event register is empty!")
        return
        
    print("\n--- Scheduled Campus Events ---")
    print("ID\t\tEvent Title\t\tVenue\t\t\tOrganizer\tStatus")
    print("-" * 75)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5:
            e_id, title, venue, org, status = parts
            print(e_id + "\t\t" + title + "\t\t" + venue + "\t\t" + org + "\t" + status)

def cancel_event():
    if not os.path.exists(EVENT_FILE):
        print("No event records exist!")
        return
        
    target = input("Enter Event ID to cancel booking: ").strip()
    if target == "":
        print("Event ID cannot be blank!")
        return
        
    f = open(EVENT_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5 and parts[0] == target:
            parts[4] = "Cancelled"
            found = True
            print("Event ID " + target + " marked as Cancelled!")
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(EVENT_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Event ID not found in records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Campus Event & Seminar Booking System ===")

while True:
    print("\n1. Book Campus Event / Venue")
    print("2. View All Scheduled Events")
    print("3. Cancel Event Booking")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        book_event()
    elif opt == "2":
        view_events()
    elif opt == "3":
        cancel_event()
    elif opt == "4":
        print("Closing event booking system... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
