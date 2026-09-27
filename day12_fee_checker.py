def show_menu():
    print("=== College Fee Checker ===")
    print("1. Add student fee record")
    print("2. Search fee status by roll no")
    print("3. View all fee records")
    print("4. Exit")

flag = True

while flag:
    show_menu()
    ch = input("\nEnter choice (1-4): ").strip()
    
    # Add record to file
    if ch == "1":
        roll = input("Enter Roll No: ").strip()
        name = input("Enter Name: ").strip().capitalize()
        amount = input("Enter Fee Amount (Rs): ").strip()
        status = input("Fee Status (Paid/Pending): ").strip().capitalize()
        
        # Saving comma separated string in text file
        f = open("fee_records.txt", "a")
        f.write(roll + "," + name + "," + amount + "," + status + "\n")
        f.close()
        
        print("Record saved in fee_records.txt!")

    # Search record in file
    elif ch == "2":
        search_roll = input("Enter Roll No to search: ").strip()
        found = False
        
        try:
            f = open("fee_records.txt", "r")
            data = f.readlines()
            f.close()
            
            for line in data:
                line = line.strip()
                if line != "":
                    # Splitting line by comma
                    parts = line.split(",")
                    if parts[0] == search_roll:
                        print("\nRecord Found:")
                        print("Roll No: " + parts[0])
                        print("Name: " + parts[1])
                        print("Amount Paid: Rs. " + parts[2])
                        print("Status: " + parts[3])
                        found = True
                        break
            
            if not found:
                print("Roll No " + search_roll + " not found!")

        except FileNotFoundError:
            print("No file exists yet! Add a record first.")

    # Show all records from file
    elif ch == "3":
        try:
            f = open("fee_records.txt", "r")
            data = f.readlines()
            f.close()
            
            if len(data) == 0:
                print("File is empty.")
            else:
                print("\nAll Student Fee Records:")
                for line in data:
                    line = line.strip()
                    if line != "":
                        parts = line.split(",")
                        print("Roll: " + parts[0] + " | Name: " + parts[1] + " | Paid: Rs. " + parts[2] + " | Status: " + parts[3])

        except FileNotFoundError:
            print("No file found! Add a record first.")

    # Exit
    elif ch == "4":
        print("Closing fee program. Allah Hafiz!")
        flag = False

    else:
        print("Wrong input! Select 1 to 4.")

    print("--------------------------------\n")

