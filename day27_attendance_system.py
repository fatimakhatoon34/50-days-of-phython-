import os
from datetime import datetime

ATTENDANCE_FILE = "attendance_log.txt"

def mark_attendance():
    roll = input("Enter Student Roll Number (e.g. ICS-101): ").strip()
    name = input("Enter Student Name: ").strip()
    status = input("Enter Status (P for Present / A for Absent): ").strip().upper()
    
    if roll != "" and name != "" and (status == "P" or status == "A"):
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        
        status_word = "Present" if status == "P" else "Absent"
        
        f = open(ATTENDANCE_FILE, "a")
        f.write(roll + "," + name + "," + status_word + "," + date_str + "\n")
        f.close()
        print("Attendance marked successfully for " + date_str + "!")
    else:
        print("Invalid input! Check roll number, name, or status (P/A).")

def view_attendance():
    if not os.path.exists(ATTENDANCE_FILE):
        print("No attendance records found!")
        return
        
    f = open(ATTENDANCE_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Attendance log is empty!")
        return
        
    print("\n--- Attendance Records ---")
    print("Roll No\t\tName\t\tStatus\t\tDate")
    print("-" * 55)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            roll, name, status, date = parts
            print(roll + "\t\t" + name + "\t\t" + status + "\t\t" + date)

def count_stats():
    if not os.path.exists(ATTENDANCE_FILE):
        print("No attendance records exist to analyze!")
        return
        
    f = open(ATTENDANCE_FILE, "r")
    lines = f.readlines()
    f.close()
    
    present_count = 0
    absent_count = 0
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            if parts[2] == "Present":
                present_count = present_count + 1
            elif parts[2] == "Absent":
                absent_count = absent_count + 1
                
    print("\n--- Attendance Summary Statistics ---")
    print("Total Records: " + str(len(lines)))
    print("Total Present: " + str(present_count))
    print("Total Absent: " + str(absent_count))

# Main Program Loop
print("=== Student Attendance Management System ===")

run = True
while run:
    print("\n1. Mark Attendance")
    print("2. View All Attendance Records")
    print("3. View Summary Statistics")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        mark_attendance()
    elif opt == "2":
        view_attendance()
    elif opt == "3":
        count_stats()
    elif opt == "4":
        print("Closing attendance system... Allah Hafiz!")
        run = False
    else:
        print("Invalid option!")
