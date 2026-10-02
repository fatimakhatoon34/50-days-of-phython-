import time

def format_time(seconds):
    mins = seconds // 60
    secs = seconds % 60
    
    if mins < 10:
        m_str = "0" + str(mins)
    else:
        m_str = str(mins)
        
    if secs < 10:
        s_str = "0" + str(secs)
    else:
        s_str = str(secs)
        
    return m_str + ":" + s_str

def start_timer(minutes, label):
    total_seconds = minutes * 60
    print("\nStarting " + label + " (" + str(minutes) + " mins)...")
    
    while total_seconds > 0:
        time_display = format_time(total_seconds)
        print("Time left: " + time_display, end="\r")
        time.sleep(1)
        total_seconds = total_seconds - 1
        
    print("\n" + label + " finished!")

# Main Loop
print("=== ICS Pomodoro Study Timer ===")

run = True
while run:
    print("\n1. Standard Study Session (25 min study / 5 min break)")
    print("2. Custom Countdown Timer")
    print("3. Exit")
    
    choice = input("Select option (1-3): ").strip()
    
    if choice == "1":
        print("\nGet ready to focus!")
        start_timer(25, "Study Session")
        print("\nTime for a short break!")
        start_timer(5, "Break Time")

    elif choice == "2":
        mins = int(input("Enter countdown time in minutes: "))
        if mins > 0:
            start_timer(mins, "Custom Timer")
        else:
            print("Please enter minutes greater than 0!")

    elif choice == "3":
        print("Exiting study timer... Allah Hafiz!")
        run = False

    else:
        print("Invalid choice! Pick 1 to 3.")
