import os

DB_FILE = "student_grades.txt"

def add_student():
    roll = input("Enter Roll Number (e.g. ICS-101): ").strip()
    name = input("Enter Student Name: ").strip()
    marks_str = input("Enter Total Marks (out of 500): ").strip()
    
    if roll != "" and name != "" and marks_str.isdigit():
        marks = int(marks_str)
        percentage = (marks / 500) * 100
        
        # Calculate grade
        if percentage >= 80:
            grade = "A+"
        elif percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "F"
            
        f = open(DB_FILE, "a")
        f.write(roll + "," + name + "," + str(marks) + "," + str(round(percentage, 2)) + "," + grade + "\n")
        f.close()
        print("Student record added successfully!")
    else:
        print("Invalid input! Check roll number, name, or numeric marks.")

def view_records():
    if not os.path.exists(DB_FILE):
        print("No student records found!")
        return
        
    f = open(DB_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Record file is empty!")
        return
        
    print("\n--- Student Grade Records ---")
    print("Roll No\t\tName\t\tMarks\t%age\tGrade")
    print("-" * 55)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5:
            roll, name, marks, perc, grade = parts
            print(roll + "\t\t" + name + "\t\t" + marks + "\t" + perc + "%\t" + grade)

def search_student():
    if not os.path.exists(DB_FILE):
        print("Record file does not exist!")
        return
        
    target = input("Enter Roll Number to search: ").strip()
    if target == "":
        print("Roll number cannot be empty!")
        return
        
    f = open(DB_FILE, "r")
    lines = f.readlines()
    f.close()
    
    found = False
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5 and parts[0] == target:
            print("\nRecord Found:")
            print("Roll Number: " + parts[0])
            print("Name: " + parts[1])
            print("Marks: " + parts[2] + "/500")
            print("Percentage: " + parts[3] + "%")
            print("Grade: " + parts[4])
            found = True
            break
            
    if not found:
        print("Student with roll number " + target + " not found.")

# Main Program Loop
print("=== Student Grade Management System ===")

run = True
while run:
    print("\n1. Add Student Record")
    print("\n2. View All Records")
    print("3. Search Student by Roll No")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        add_student()
    elif opt == "2":
        view_records()
    elif opt == "3":
        search_student()
    elif opt == "4":
        print("Closing grade manager... Allah Hafiz!")
        run = False
    else:
        print("Invalid option!")
