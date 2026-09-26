def show_menu():
    print("=== Habib Student Bank ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Save Statement File")
    print("5. Exit")

balance = 1000.0
trans_list = []

run = True

while run:
    show_menu()
    ch = input("\nEnter option (1-5): ").strip()
    
    if ch == "1":
        dep = float(input("Enter deposit amount Rs: "))
        if dep > 0:
            balance = balance + dep
            trans_list.append("Deposited: Rs. " + str(dep))
            print("Rs. " + str(dep) + " added. Current Balance: Rs. " + str(balance))
        else:
            print("Invalid amount!")

    elif ch == "2":
        w_draw = float(input("Enter withdrawal amount Rs: "))
        if w_draw > 0 and w_draw <= balance:
            balance = balance - w_draw
            trans_list.append("Withdrew: Rs. " + str(w_draw))
            print("Rs. " + str(w_draw) + " withdrawn. New Balance: Rs. " + str(balance))
        elif w_draw > balance:
            print("Low balance! Available balance is Rs. " + str(balance))
        else:
            print("Invalid amount!")

    elif ch == "3":
        print("Current Balance: Rs. " + str(balance))
        print("Total transactions: " + str(len(trans_list)))

    elif ch == "4":
        if len(trans_list) == 0:
            print("No transactions to save.")
        else:
            # File handling - writing statement
            f = open("statement.txt", "a")
            f.write("--- Statement ---\n")
            for item in trans_list:
                f.write(item + "\n")
            f.write("Final Balance: Rs. " + str(balance) + "\n")
            f.close()
            print("Saved to statement.txt!")

    elif ch == "5":
        print("Exiting... Allah Hafiz")
        run = False

    else:
        print("Wrong choice!")

    print("--------------------------------\n")
              
