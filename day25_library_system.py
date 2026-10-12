import os

BOOK_FILE = "library_books.txt"

def add_book():
    b_id = input("Enter Book ID (e.g. B-001): ").strip()
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    
    if b_id != "" and title != "" and author != "":
        f = open(BOOK_FILE, "a")
        f.write(b_id + "," + title + "," + author + ",Available\n")
        f.close()
        print("Book added to library successfully!")
    else:
        print("Fields cannot be empty!")

def view_books():
    if not os.path.exists(BOOK_FILE):
        print("No books found in library catalog!")
        return
        
    f = open(BOOK_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Catalog is empty!")
        return
        
    print("\n--- Library Book Catalog ---")
    print("ID\t\tTitle\t\tAuthor\t\tStatus")
    print("-" * 55)
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            b_id, title, author, status = parts
            print(b_id + "\t\t" + title + "\t\t" + author + "\t\t" + status)

def issue_book():
    if not os.path.exists(BOOK_FILE):
        print("No library file found!")
        return
        
    target = input("Enter Book ID to issue: ").strip()
    
    f = open(BOOK_FILE, "r")
    lines = f.readlines()
    f.close()
    
    updated_lines = []
    found = False
    
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4 and parts[0] == target:
            if parts[3] == "Available":
                parts[3] = "Issued"
                found = True
                print("Book issued successfully!")
            else:
                print("Book is already issued out!")
                found = True
        updated_lines.append(",".join(parts) + "\n")
        
    if found:
        f = open(BOOK_FILE, "w")
        f.writelines(updated_lines)
        f.close()
    else:
        print("Book ID not found.")

# Main Program Loop
print("=== ICS Library Management System ===")

run = True
while run:
    print("\n1. Add New Book")
    print("2. View All Books")
    print("3. Issue Book")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        add_book()
    elif opt == "2":
        view_books()
    elif opt == "3":
        issue_book()
    elif opt == "4":
        print("Closing library system... Allah Hafiz!")
        run = False
    else:
        print("Invalid choice!")
