

def print_menu():
    print("=== General Knowledge Quiz ===")
    print("1. Start Quiz")
    print("2. View Rules")
    print("3. Exit")

# List of quiz questions
# Each item has: [Question, Option A, Option B, Option C, Correct Answer]
questions = [
    ["What is the capital of Pakistan?", "A. Lahore", "B. Islamabad", "C. Karachi", "B"],
    ["Which keyword defines a function in Python?", "A. func", "B. def", "C. function", "B"],
    ["What is the remainder of 10 % 3?", "A. 1", "B. 3", "C. 0", "A"],
    ["Which data type uses key-value pairs?", "A. List", "B. Tuple", "C. Dictionary", "C"]
]

is_running = True

while is_running:
    print_menu()
    user_choice = input("\nSelect an option (1-3): ").strip()
    print("\n----------------------------")

    # Start Quiz
    if user_choice == "1":
        marks = 0
        total_q = len(questions)
        
        print("Quiz Started! Enter A, B, or C.\n")
        
        for q in questions:
            print(q[0])
            print(q[1])
            print(q[2])
            print(q[3])
            
            ans = input("Your answer: ").strip().upper()
            
            if ans == q[4]:
                print("Correct answer!\n")
                marks = marks + 1
            else:
                print("Wrong! Correct answer was " + q[4] + "\n")
        
        # Calculate percentage
        percent = (marks / total_q) * 100
        
        print("--- Final Result ---")
        print("Total Marks: " + str(marks) + " out of " + str(total_q))
        print("Percentage: " + str(round(percent, 1)) + "%")
        
        if percent >= 70:
            print("Status: Passed!")
        else:
            print("Status: Needs Improvement")

    # View Rules
    elif user_choice == "2":
        print("Quiz Instructions:")
        print("- Choose A, B, or C for each question.")
        print("- You get 1 mark for every correct answer.")
        print("- Final score will show at the end.")

    # Exit
    elif user_choice == "3":
        print("Thanks for taking the quiz! Allah Hafiz.")
        is_running = False

    else:
        print("Invalid input! Please choose 1, 2, or 3.")

    print("----------------------------\n")
    
