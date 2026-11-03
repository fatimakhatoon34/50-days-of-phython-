import os

EVAL_FILE = "evaluation_records.txt"

def submit_evaluation():
    eval_id = input("Enter Eval ID (e.g. EV-01): ").strip()
    course_name = input("Enter Course Name (e.g. CS-101): ").strip()
    faculty_name = input("Enter Faculty / Teacher Name: ").strip()
    rating_str = input("Enter Rating (1 to 5): ").strip()
    
    if eval_id != "" and course_name != "" and faculty_name != "" and rating_str.isdigit():
        rating = int(rating_str)
        if 1 <= rating <= 5:
            f = open(EVAL_FILE, "a")
            f.write(eval_id + "," + course_name + "," + faculty_name + "," + str(rating) + "\n")
            f.close()
            print("Evaluation submitted successfully!")
        else:
            print("Rating must be between 1 and 5!")
    else:
        print("Invalid input! Fields cannot be empty and rating must be numeric.")

def view_evaluations():
    if not os.path.exists(EVAL_FILE):
        print("No evaluation records found!")
        return
        
    f = open(EVAL_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Evaluation register is empty!")
        return
        
    print("\n--- Faculty & Course Evaluation Register ---")
    print("Eval ID\t\tCourse\t\tFaculty Name\t\tRating (out of 5)")
    print("-" * 65)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            e_id, course, teacher, rating = parts
            print(e_id + "\t\t" + course + "\t\t" + teacher + "\t\t" + rating + " / 5")

def calculate_summary():
    if not os.path.exists(EVAL_FILE):
        print("No evaluation records exist to summarize!")
        return
        
    f = open(EVAL_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("No data available for calculation!")
        return
        
    total_rating = 0
    count = 0
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[3].isdigit():
            total_rating += int(parts[3])
            count += 1
            
    if count > 0:
        avg_score = total_rating / count
        print("\n--- Evaluation Summary Report ---")
        print("Total Evaluations Recorded: " + str(count))
        print("Average Course Rating: " + str(round(avg_score, 2)) + " / 5.0")
    else:
        print("No valid rating data found.")

# Main Program Loop (Infinite Loop with Break)
print("=== Faculty & Course Evaluation System ===")

while True:
    print("\n1. Submit Course & Faculty Evaluation")
    print("2. View All Evaluation Records")
    print("3. Generate Summary & Average Rating")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        submit_evaluation()
    elif opt == "2":
        view_evaluations()
    elif opt == "3":
        calculate_summary()
    elif opt == "4":
        print("Closing evaluation system... Allah Hafiz!")
        break
    else:
        print("Invalid option!")
