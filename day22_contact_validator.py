def validate_email(email):
email = email.strip()

if "@" not in email:
return False, "Missing '@' symbol"

parts = email.split("@")
if len(parts) != 2:
return False, "Email must have exactly one '@' symbol"

username, domain = parts[0], parts[1]

if username == "" or domain == "":
return False, "Username or domain cannot be empty"

if "." not in domain:
return False, "Domain missing '.' suffix"

if domain.startswith(".") or domain.endswith("."):
return False, "Invalid domain dot placement"

return True, "Valid Email"

def validate_phone(phone):
phone = phone.strip().replace("-", "").replace(" ", "")

if not phone.isdigit():
return False, "Phone number must contain digits only"

# Standard Pakistani mobile format check (e.g. 03001234567 -> 11 digits)
if len(phone) == 11 and phone.startswith("03"):
return True, "Valid Phone Number (Local Format)"
else:
return False, "Invalid length or network prefix (Must start with 03 and be 11 digits)"

# Main Program Loop
print("=== Student Contact Info Validator ===")

run = True
while run:
print("\n1. Validate Email Address")
print("2. Validate Pakistani Phone Number")
print("3. Exit")

opt = input("Choice (1-3): ").strip()

if opt == "1":
user_email = input("Enter email address: ")
is_valid, msg = validate_email(user_email)
print("Result: " + ("VALID" if is_valid else "INVALID") + " (" + msg + ")")

elif opt == "2":
user_phone = input("Enter mobile number (e.g. 0300-1234567): ")
is_valid, msg = validate_phone(user_phone)
print("Result: " + ("VALID" if is_valid else "INVALID") + " (" + msg + ")")

elif opt == "3":
print("Closing validator... Allah Hafiz!")
run = False

else:
print("Invalid choice!")
