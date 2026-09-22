

def show_menu():
    print("=== Shopping Cart Manager ===")
    print("1. Add item to cart")
    print("2. View cart items")
    print("3. Edit an item price")
    print("4. Calculate total bill")
    print("5. Exit")

# Lists to store cart items and prices
items = []
prices = []

keep_running = True

while keep_running:
    show_menu()
    choice = input("\nSelect an option (1-5): ").strip()
    print("\n----------------------------")

    # Option 1: Add item
    if choice == "1":
        item_name = input("Enter item name: ").strip().capitalize()
        item_price = float(input("Enter price in Rs: "))
        
        items.append(item_name)
        prices.append(item_price)
        print("\n" + item_name + " added to your cart!")

    # Option 2: View items
    elif choice == "2":
        if len(items) == 0:
            print("\nYour cart is empty right now.")
        else:
            print("\nItems in your cart:")
            for i in range(len(items)):
                print(str(i + 1) + ". " + items[i] + " - Rs. " + str(prices[i]))

    # Option 3: Edit item price
    elif choice == "3":
        if len(items) == 0:
            print("\nCart is empty! Nothing to edit.")
        else:
            print("\nSelect item to edit:")
            for i in range(len(items)):
                print(str(i + 1) + ". " + items[i] + " (Rs. " + str(prices[i]) + ")")
            
            item_num = int(input("\nEnter item number to change price: "))
            index = item_num - 1  # Adjust for 0-based index
            
            if index >= 0 and index < len(items):
                new_price = float(input("Enter new price in Rs: "))
                prices[index] = new_price
                print("\nPrice for " + items[index] + " updated to Rs. " + str(new_price))
            else:
                print("\nInvalid item number!")

    # Option 4: Calculate total
    elif choice == "4":
        if len(items) == 0:
            print("\nYour cart is empty. Please add items first!")
        else:
            subtotal = sum(prices)
            print("\nSubtotal: Rs. " + str(round(subtotal, 2)))
            
            # Apply 10% discount if bill is over Rs. 5000
            if subtotal > 5000:
                discount = subtotal * 0.10
                final_total = subtotal - discount
                print("Discount (10% off for bill over Rs. 5000): -Rs. " + str(round(discount, 2)))
                print("Final Total: Rs. " + str(round(final_total, 2)))
            else:
                print("Final Total: Rs. " + str(round(subtotal, 2)))

    # Option 5: Exit
    elif choice == "5":
        print("\nThank you for shopping! Allah Hafiz.")
        keep_running = False

    else:
        print("\nInvalid option! Please enter a number from 1 to 5.")

    print("----------------------------\n")
    
