import os

def get_ext(fname):
    if "." in fname:
        p = fname.split(".")
        return "." + p[-1]
    return ""

def make_name(pfix, c, ext):
    if c < 10:
        return pfix + "_0" + str(c) + ext
    else:
        return pfix + "_" + str(c) + ext

print("=== Student File Renamer ===")

path = input("Enter folder path (. for current folder): ").strip()

try:
    files = os.listdir(path)
    
    if len(files) == 0:
        print("No files found!")
    else:
        print("Files in folder:")
        for f in files:
            print("- " + f)
            
        print("\n")
        prefix = input("Enter prefix for files (e.g. ICS_Notes): ").strip()
        ans = input("Confirm rename? (Yes/No): ").strip().capitalize()
        
        if ans == "Yes":
            count = 1
            renamed = 0
            
            for file in files:
                # Don't rename python code
                if file.endswith(".py"):
                    continue
                    
                old_p = os.path.join(path, file)
                
                if os.path.isfile(old_p):
                    ext = get_ext(file)
                    new_f = make_name(prefix, count, ext)
                    new_p = os.path.join(path, new_f)
                    
                    os.rename(old_p, new_p)
                    print("Renamed: " + file + " to " + new_f)
                    
                    count = count + 1
                    renamed = renamed + 1
                    
            print("\nDone! Total files renamed: " + str(renamed))
        else:
            print("Cancelled.")

except FileNotFoundError:
    print("Folder does not exist!")
