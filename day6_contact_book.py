

# Dictionary to keep all contacts
contacts = {}

def print_menu():
    print("=== Contact Book Menu ===")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. Show all contacts")
    print("4. Exit program")

# Main program loop
running = True

while running:
    print_menu()
    user_choice = input("\nChoose an option (1-4): ")
    print("\n----------------------------")

    # Option 1: Add contact
    if user_choice == "1":
        name = input("Enter contact name: ").strip().capitalize()
        phone = input("Enter phone number: ").strip()
        
        contacts[name] = phone
        print("\n" + name + " has been added to contacts!")

    # Option 2: Search contact
    elif user_choice == "2":
        search = input("Enter name to look up: ").strip().capitalize()
        
        if search in contacts:
            print("\nName:", search)
            print("Phone:", contacts[search])
        else:
            print("\nSorry, couldn't find " + search + " in contacts.")

    # Option 3: Display all
    elif user_choice == "3":
        if len(contacts) == 0:
            print("\nNo contacts saved yet.")
        else:
            print("\nSaved Contacts List:")
            for name, phone in contacts.items():
                print("- " + name + ": " + phone)

    # Option 4: Exit
    elif user_choice == "4":
        print("\nExiting program... Goodbye!")
        running = False

    else:
        print("\nInvalid choice, please enter 1, 2, 3, or 4.")

    print("----------------------------\n")
    
