import os

def convert_line(line):
    # Headings
    if line.startswith("# "):
        return "<h1>" + line[2:].strip() + "</h1>"
    elif line.startswith("## "):
        return "<h2>" + line[3:].strip() + "</h2>"
    elif line.startswith("### "):
        return "<h3>" + line[4:].strip() + "</h3>"
    
    # Lists
    elif line.startswith("- ") or line.startswith("* "):
        return "<li>" + line[2:].strip() + "</li>"
    
    # Blank lines
    elif line.strip() == "":
        return ""
    
    # Normal text
    else:
        text = line.strip()
        if "**" in text:
            p = text.split("**")
            if len(p) >= 3:
                text = p[0] + "<b>" + p[1] + "</b>" + p[2]
        return "<p>" + text + "</p>"

def parse_md_file(in_f, out_f):
    if not os.path.exists(in_f):
        print("File not found!")
        return False
        
    f_in = open(in_f, "r")
    lines = f_in.readlines()
    f_in.close()
    
    html = []
    html.append("<html>")
    html.append("<body>")
    
    for line in lines:
        c = convert_line(line)
        if c != "":
            html.append("  " + c)
            
    html.append("</body>")
    html.append("</html>")
    
    f_out = open(out_f, "w")
    for h in html:
        f_out.write(h + "\n")
    f_out.close()
    
    return True

# Main Code
print("=== Markdown to HTML Tool ===")

run = True
while run:
    print("\n1. Convert File")
    print("2. Exit")
    
    opt = input("Choice (1-2): ").strip()
    
    if opt == "1":
        file_in = input("Enter markdown file name (e.g. notes.md): ").strip()
        file_out = input("Enter output html name (e.g. notes.html): ").strip()
        
        if file_in != "" and file_out != "":
            done = parse_md_file(file_in, file_out)
            if done:
                print("Converted successfully to " + file_out)
        else:
            print("File names can't be empty!")

    elif opt == "2":
        print("Closing... Allah Hafiz!")
        run = False

    else:
        print("Invalid choice!")
