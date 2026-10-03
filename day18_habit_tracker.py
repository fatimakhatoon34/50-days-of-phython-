
import os

# Dictionary to store habits: {habit_name: streak_count}
habits = {}

def add_habit(name):
    if name in habits:
        print("Habit already exists!")
    else:
        habits[name] = 0
        print("Habit '" + name + "' added successfully.")

def mark_done(name):
    if name in habits:
        habits[name] = habits[name] + 1
        print("Completed! New streak for " + name + ": " + str(habits[name]) + " days")
    else:
        print("Habit not found!")

def show_summary():
    if len(habits) == 0:
        print("No habits added yet!")
    else:
        print("\n--- Daily Habit Summary ---")
        for h, streak in habits.items():
            print("- " + h + ": " + str(streak) + " day streak")

# Main Program Loop
print("=== Student Daily Habit Tracker ===")

run = True
while run:
    print("\n1. Add New Habit")
    print("2. Mark Habit Completed Today")
    print("3. View Habit Streaks")
    print("4. Exit")
    
    choice = input("Select choice (1-4): ").strip()
    
    if choice == "1":
        h_name = input("Enter habit name (e.g. Revision 1hr): ").strip()
        if len(h_name) > 0:
            add_habit(h_name)
        else:
            print("Habit name cannot be blank!")

    elif choice == "2":
        if len(habits) == 0:
            print("No habits available to update!")
        else:
            show_summary()
            h_name = input("\nEnter completed habit name: ").strip()
            mark_done(h_name)

    elif choice == "3":
        show_summary()

    elif choice == "4":
        print("Closing tracker... Allah Hafiz!")
        run = False

    else:
        print("Invalid option! Pick 1 to 4.")
