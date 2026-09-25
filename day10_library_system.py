

def show_menu():
    print("=== College Library Manager ===")
    print("1. Add a new book")
    print("2. Display all books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")

# List to keep all book records (dictionaries)
library_books = []

flag = True

while flag:
    show_menu()
    user_choice = input("\nEnter choice (1-5): ").strip()
    print("\n-----------------------------------")

    # Add Book
    if user_choice == "1":
        b_id = input("Enter Book ID: ").strip()
        title = input("Enter Book Title: ").strip().capitalize()
        author = input("Enter Author Name: ").strip().capitalize()
        
        # Book record dictionary
        book = {
            "id": b_id,
            "title": title,
            "author": author,
            "is_available": True
        }
        
        library_books.append(book)
        print("\nBook '" + title + "' added successfully!")

    # View Books
    elif user_choice == "2":
        if len(library_books) == 0:
            print("\nLibrary has no books right now.")
        else:
            print("\nAvailable & Borrowed Books:")
            for b in library_books:
                if b["is_available"] == True:
                    status = "Available"
                else:
                    status = "Borrowed"
                
                print("ID: " + b["id"] + " | Title: " + b["title"] + " | Author: " + b["author"] + " | Status: " + status)

    # Borrow Book
    elif user_choice == "3":
        if len(library_books) == 0:
            print("\nNo books available to borrow.")
        else:
            search_id = input("Enter Book ID to borrow: ").strip()
            found = False
            
            for b in library_books:
                if b["id"] == search_id:
                    found = True
                    if b["is_available"] == True:
                        b["is_available"] = False
                        print("\nYou borrowed '" + b["title"] + "'. Return it on time!")
                    else:
                        print("\nSorry! This book is already taken.")
                    break
            
            if not found:
                print("\nBook ID " + search_id + " not found.")

    # Return Book
    elif user_choice == "4":
        if len(library_books) == 0:
            print("\nLibrary list is empty.")
        else:
            search_id = input("Enter Book ID to return: ").strip()
            found = False
            
            for b in library_books:
                if b["id"] == search_id:
                    found = True
                    if b["is_available"] == False:
                        b["is_available"] = True
                        
                        # Fine calculation
                        late_days = int(input("Enter late days (0 if returned on time): "))
                        if late_days > 0:
                            fine = late_days * 50
                            print("Book returned! Late fine: Rs. " + str(fine))
                        else:
                            print("Book returned on time! No fine.")
                    else:
                        print("\nThis book was not borrowed.")
                    break
            
            if not found:
                print("\nBook ID " + search_id + " not found.")

    # Exit
    elif user_choice == "5":
        print("\nExiting library system. Allah Hafiz!")
        flag = False

    else:
        print("\nInvalid input! Choose 1 to 5 only.")

    print("-----------------------------------\n")
