import os
from datetime import datetime

NOTES_FILE = "my_notes.txt"

def add_note():
    text = input("Enter note: ").strip()
    if text == "":
        print("Note cannot be empty!")
        return
        
    now = datetime.now()
    timestamp = now.strftime("[%Y-%m-%d %H:%M]")
    
    f = open(NOTES_FILE, "a")
    f.write(timestamp + " " + text + "\n")
    f.close()
    
    print("Note saved successfully!")

def view_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes found yet! Add one first.")
        return
        
    f = open(NOTES_FILE, "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        print("Notes file is empty!")
    else:
        print("\n--- Saved Notes ---")
        for line in lines:
            print(line.strip())

def search_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes file exists to search!")
        return
        
    query = input("Enter search keyword: ").strip().lower()
    if query == "":
        print("Keyword cannot be blank!")
        return
        
    f = open(NOTES_FILE, "r")
    lines = f.readlines()
    f.close()
    
    found = False
    print("\n--- Search Results for '" + query + "' ---")
    for line in lines:
        if query in line.lower():
            print(line.strip())
            found = True
            
    if not found:
        print("No matching notes found.")

# Main Program Loop
print("=== Student CLI Notepad ===")

run = True
while run:
    print("\n1. Add Note")
    print("2. View All Notes")
    print("3. Search Notes")
    print("4. Exit")
    
    opt = input("Choice (1-4): ").strip()
    
    if opt == "1":
        add_note()
    elif opt == "2":
        view_notes()
    elif opt == "3":
        search_notes()
    elif opt == "4":
        print("Closing notepad... Allah Hafiz!")
        run = False
    else:
        print("Invalid choice!")
