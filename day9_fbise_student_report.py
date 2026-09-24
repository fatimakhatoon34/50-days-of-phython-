

def display_menu():
    print("=== FBISE Student Record System ===")
    print("1. Add new student")
    print("2. Show all student records")
    print("3. Search by roll number")
    print("4. Exit")

# List to keep student records
students = []

flag = True

while flag:
    display_menu()
    user_input = input("\nEnter choice (1-4): ").strip()
    print("\n-----------------------------------")

    # Add student
    if user_input == "1":
        roll_no = input("Enter roll number: ").strip()
        name = input("Enter student name: ").strip().capitalize()
        marks = float(input("Enter total marks (out of 1200): "))
        attended = int(input("Enter attended classes: "))
        total_classes = int(input("Enter total classes held: "))
        
        # Percentage math
        m_percentage = (marks / 1100) * 100
        a_percentage = (attended / total_classes) * 100
        
        # Board grading logic
        if m_percentage >= 80:
            board_grade = "A-1"
        elif m_percentage >= 70:
            board_grade = "A"
        elif m_percentage >= 60:
            board_grade = "B"
        elif m_percentage >= 50:
            board_grade = "C"
        elif m_percentage >= 40:
            board_grade = "D"
        elif m_percentage >= 33:
            board_grade = "E"
        else:
            board_grade = "F"

        # Make dictionary for single student
        st_dict = {
            "roll": roll_no,
            "name": name,
            "marks": marks,
            "pct": round(m_percentage, 1),
            "att": round(a_percentage, 1),
            "grade": board_grade
        }
        
        students.append(st_dict)
        print("\nStudent " + name + " saved!")

    # View all
    elif user_input == "2":
        if len(students) == 0:
            print("\nList is empty, add students first.")
        else:
            print("\nSaved Student Records:")
            for s in students:
                print("Roll No: " + s["roll"])
                print("Name: " + s["name"])
                print("Marks: " + str(s["marks"]) + "/1100 (" + str(s["pct"]) + "%)")
                print("Attendance: " + str(s["att"]) + "%")
                print("Grade: " + s["grade"])
                
                # Eligibility checks
                if s["att"] < 75:
                    print("Status: Shortage of attendance (Detained)")
                elif s["pct"] < 33:
                    print("Status: Failed (Supply exam required)")
                else:
                    print("Status: Eligible for Board Exams")
                print("-----------------------------------")

    # Search
    elif user_input == "3":
        if len(students) == 0:
            print("\nNo records available.")
        else:
            s_roll = input("Enter roll number to search: ").strip()
            found = False
            
            for s in students:
                if s["roll"] == s_roll:
                    print("\nStudent Found:")
                    print("Roll No: " + s["roll"])
                    print("Name: " + s["name"])
                    print("Marks: " + str(s["marks"]) + "/1100 (" + str(s["pct"]) + "%)")
                    print("Attendance: " + str(s["att"]) + "%")
                    print("Grade: " + s["grade"])
                    found = True
                    break
            
            if not found:
                print("\nRoll number " + s_roll + " not found.")

    # Exit
    elif user_input == "4":
        print("\nClosing program. Good luck for FBISE board exams!")
        flag = False

    else:
        print("\nWrong choice! Select 1 to 4 only.")

    print("-----------------------------------\n")
