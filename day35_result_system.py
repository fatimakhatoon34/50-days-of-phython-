import os

RESULT_FILE = "exam_results.txt"

def add_result():
    roll = input("Enter Roll Number (e.g. ICS-101): ").strip()
    name = input("Enter Student Name: ").strip()
    eng_str = input("Enter English Marks (out of 100): ").strip()
    math_str = input("Enter Math Marks (out of 100): ").strip()
    comp_str = input("Enter Computer Marks (out of 100): ").strip()
    
    if roll != "" and name != "" and eng_str.isdigit() and math_str.isdigit() and comp_str.isdigit():
        eng = int(eng_str)
        math = int(math_str)
        comp = int(comp_str)
        
        total = eng + math + comp
        percentage = (total / 300) * 100
        
        # Simple grading logic
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
            
        f = open(RESULT_FILE, "a")
        f.write(roll + "," + name + "," + str(total) + "," + str(round(percentage, 2)) + "," + grade + "\n")
        f.close()
        print("Exam result recorded successfully! Total: " + str(total) + "/300 (" + str(round(percentage, 2)) + "%) Grade: " + grade)
    else:
        print("Invalid input! Check roll number, name, or numeric marks.")

def view_results():
    if not os.path.exists(RESULT_FILE):
        print("No exam results found!")
        return
        
    f = open(RESULT_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Result record file is empty!")
        return
        
    print("\n--- Student Exam Results Catalog ---")
    print("Roll No\t\tName\t\tTotal\t\tPercentage\tGrade")
    print("-" * 60)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5:
            roll, name, total, pct, grade = parts
            print(roll + "\t\t" + name + "\t\t" + total + "/300\t\t" + pct + "%\t\t" + grade)

def search_result():
    if not os.path.exists(RESULT_FILE):
        print("No exam results exist!")
        return
        
    target = input("Enter Roll Number to search report card: ").strip()
    if target == "":
        print("Roll number cannot be blank!")
        return
        
    f = open(RESULT_FILE, "r")
    lines = f.readlines()
    f.close()
    
    found = False
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5 and parts[0] == target:
            print("\n--- Student Report Card ---")
            print("Roll Number : " + parts[0])
            print("Student Name: " + parts[1])
            print("Total Marks : " + parts[2] + "/300")
            print("Percentage  : " + parts[3] + "%")
            print("Grade       : " + parts[4])
            found = True
            break
            
    if not found:
        print("Student roll number not found in result records.")

# Main Program Loop (Infinite Loop with Break)
print("=== Student Exam Result System ===")

while True:
    print("\n1. Add Student Exam Result")
    print("2. View All Results Catalog")
    print("3. Search Report Card by Roll No")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        add_result()
    elif opt == "2":
        view_results()
    elif opt == "3":
        search_result()
    elif opt == "4":
        print("Closing exam result system... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
