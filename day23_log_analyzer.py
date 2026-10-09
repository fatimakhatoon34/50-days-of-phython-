import os

def generate_sample_log(filename):
    # Helper to create a dummy log file if one doesn't exist
    content = """[2026-10-09 10:15:01] INFO - System booted successfully
[2026-10-09 10:15:12] WARNING - Low memory detected
[2026-10-09 10:16:05] ERROR - Failed to connect to database
[2026-10-09 10:17:22] INFO - User admin logged in
[2026-10-09 10:18:40] ERROR - File not found: dataset.csv
[2026-10-09 10:19:00] WARNING - High CPU usage detected
[2026-10-09 10:20:11] INFO - Backup completed
"""
    f = open(filename, "w")
    f.write(content)
    f.close()
    print("Sample log file created: " + filename)

def analyze_log(filename):
    if not os.path.exists(filename):
        print("Log file not found!")
        return

    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    info_count = 0
    warn_count = 0
    err_count = 0
    errors_list = []

    for line in lines:
        line_str = line.strip()
        if "INFO" in line_str:
            info_count = info_count + 1
        elif "WARNING" in line_str:
            warn_count = warn_count + 1
        elif "ERROR" in line_str:
            err_count = err_count + 1
            errors_list.append(line_str)

    print("\n--- Log Analysis Report ---")
    print("Total Lines Analyzed: " + str(len(lines)))
    print("INFO Entries: " + str(info_count))
    print("WARNING Entries: " + str(warn_count))
    print("ERROR Entries: " + str(err_count))

    if len(errors_list) > 0:
        print("\n--- Flagged Errors ---")
        for err in errors_list:
            print("- " + err)

# Main Program Loop
print("=== Student Log Analyzer Tool ===")

run = True
while run:
    print("\n1. Analyze Log File")
    print("2. Generate Sample Log File")
    print("3. Exit")
    
    opt = input("Choice (1-3): ").strip()

    if opt == "1":
        file_path = input("Enter log file path (e.g. app.log): ").strip()
        if file_path != "":
            analyze_log(file_path)
        else:
            print("File path cannot be blank!")

    elif opt == "2":
        generate_sample_log("app.log")

    elif opt == "3":
        print("Closing analyzer... Allah Hafiz!")
        run = False

    else:
        print("Invalid option!")
