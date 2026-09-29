import random

# Function with return value to sanitize and format raw strings
def format_topic_title(raw_title):
    # Removing extra spaces and converting to Title Case
    clean_title = raw_title.strip().title()
    return clean_title

# Function to extract key terms from raw text notes
def extract_keywords(raw_text):
    # Cleaning common punctuation manually
    text = raw_text.replace(".", "").replace(",", "").replace("-", " ")
    words = text.split()
    
    important_words = []
    for w in words:
        # Keep words longer than 3 letters to filter out small prepositions
        if len(w) > 3:
            important_words.append(w.capitalize())
            
    return important_words

# Function to auto-generate a study card code
def generate_card_code(category):
    prefix = category[:3].upper()
    random_num = random.randint(100, 999)
    card_id = prefix + "-" + str(random_num)
    return card_id

# Main Program
print("=== ICS Study Note & Quiz Card Automator ===")

subject = input("Enter Subject Name (e.g. Computer Science): ").strip()
clean_subject = format_topic_title(subject)
subject_code = generate_card_code(clean_subject)

print("\nProcessing session for subject: " + clean_subject + " [" + subject_code + "]")

study_cards = []

run = True

while run:
    print("\n1. Add Raw Note / Concept")
    print("2. View Cleaned Flashcards")
    print("3. Exit")
    
    choice = input("Select option (1-3): ").strip()
    
    if choice == "1":
        topic = input("Enter Topic Name: ")
        raw_note = input("Paste raw study note / definition: ")
        
        formatted_topic = format_topic_title(topic)
        keywords = extract_keywords(raw_note)
        
        card = {
            "id": generate_card_code("NOTE"),
            "topic": formatted_topic,
            "original_note": raw_note.strip(),
            "keywords": keywords
        }
        
        study_cards.append(card)
        print("\nNote refactored and added successfully!")

    elif choice == "2":
        if len(study_cards) == 0:
            print("\nNo flashcards generated yet.")
        else:
            print("\n================ CLEANED FLASHCARDS ================")
            for c in study_cards:
                print("Card ID: " + c["id"])
                print("Topic: " + c["topic"])
                print("Note: " + c["original_note"])
                
                # Joining extracted keywords manually
                key_str = ""
                for k in c["keywords"]:
                    key_str = key_str + k + " | "
                
                print("Key Terms: " + key_str)
                print("--------------------------------------------------")

    elif choice == "3":
        print("\nExiting automator... Allah Hafiz!")
        run = False

    else:
        print("\nInvalid choice! Select 1 to 3.")
