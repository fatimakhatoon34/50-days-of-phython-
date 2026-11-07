import os

PORTAL_LOG = "master_portal_log.txt"

def log_system_access(module_name):
    f = open(PORTAL_LOG, "a")
    f.write("Accessed Module: " + module_name + "\n")
    f.close()

def display_portfolio_stats():
    print("\n==================================================")
    print("      ICS 50-DAY PYTHON PORTFOLIO STATS          ")
    print("==================================================")
    print(" Total CLI Modules Completed  : 50 / 50 (100%)")
    print(" Data Persistence Standard    : Custom CSV (.txt)")
    print(" Primary Language Standard    : Python 3 Standard Library")
    print(" Target Application           : ICS Scholarship Portfolio")
    print(" Status                       : COMPLETE & VERIFIED")
    print("==================================================")
    input("\nPress Enter to return to Master Menu...")

def launch_academics_subsystem():
    log_system_access("Academics & Evaluation Subsystem")
    print("\n--- [MODULE] Academics & Evaluation Subsystem ---")
    print("1. Course Evaluations (Day 46)")
    print("2. Central Clearance Verification (Day 47)")
    print("3. Capstone Thesis Portal (Day 48)")
    print("4. Return to Master Menu")
    
    choice = input("Select sub-option (1-4): ").strip()
    if choice in ["1", "2", "3"]:
        print("Launching selected academic module... [Simulated Active Integration]")
    else:
        print("Returning to main portal...")

def launch_services_subsystem():
    log_system_access("Student Services & Campus Life Subsystem")
    print("\n--- [MODULE] Student Services Subsystem ---")
    print("1. Security & Visitor Pass System (Day 43)")
    print("2. Sports Equipment & Field System (Day 44)")
    print("3. Career Placement Tracker (Day 45)")
    print("4. Health Center & Sick Bay (Day 49)")
    print("5. Return to Master Menu")
    
    choice = input("Select sub-option (1-5): ").strip()
    if choice in ["1", "2", "3", "4"]:
        print("Launching selected campus service module... [Simulated Active Integration]")
    else:
        print("Returning to main portal...")

def view_audit_log():
    if not os.path.exists(PORTAL_LOG):
        print("No master portal audit logs found!")
        return
        
    f = open(PORTAL_LOG, "r")
    lines = f.readlines()
    f.close()
    
    print("\n--- Master Administrative Access Audit Log ---")
    for idx, line in enumerate(lines, 1):
        print(str(idx) + ". " + line.strip())

# Main Program Loop (Infinite Loop with Break)
print("**************************************************")
print("  WELCOME TO THE CENTRAL CAMPUS MASTER PORTAL HUB ")
print("       FBISE ICS Computer Science Capstone        ")
print("**************************************************")

while True:
    print("\n=== MASTER PORTAL MAIN MENU ===")
    print("1. Academic & Student Clearance Subsystem")
    print("2. Campus Life & Student Services Subsystem")
    print("3. System Access Audit Logs")
    print("4. Display 50-Day Portfolio Milestone Summary")
    print("5. Exit Master Portal")
    
    opt = input("Choice (1-5): ").strip()
    
    if opt == "1":
        launch_academics_subsystem()
    elif opt == "2":
        launch_services_subsystem()
    elif opt == "3":
        view_audit_log()
    elif opt == "4":
        display_portfolio_stats()
    elif opt == "5":
        print("\n" + "="*50)
        print("   Congratulations on completing all 50 Days!")
        print("   Your CLI Python Portfolio is ready for review.")
        print("   Closing Master Portal Hub... Allah Hafiz!")
        print("="*50)
        break
    else:
        print("Invalid choice! Please select 1-5.")
