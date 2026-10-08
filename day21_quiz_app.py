questions = [
    ("What is the primary function of the CPU?", "a"),
    ("Which module is used for delays in Python?", "b"),
    ("What data type is returned by input()?", "c")
]

options = [
    ["a) Processing data", "b) Storing files permanently", "c) Displaying graphics"],
    ["a) os", "b) time", "c) random"],
    ["a) Integer", "b) Boolean", "c) String"]
]

score = 0

print("=== Quick ICS CS Quiz ===")

for i in range(len(questions)):
    print("\nQ" + str(i + 1) + ": " + questions[i][0])
    for opt in options[i]:
        print("  " + opt)
        
    ans = input("Your answer (a/b/c): ").strip().lower()
    
    if ans == questions[i][1]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! Correct answer was: " + questions[i][1])

print("\n--- Final Result ---")
print("Score: " + str(score) + "/" + str(len(questions)))
