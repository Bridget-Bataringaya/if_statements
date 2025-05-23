# Sample inventory as a dictionary: item -> quantity
inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Oranges": 20
}

def display_inventory():
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def update_inventory():
    item = input("Enter the item name to update: ").title()
    if item in inventory:
        new_quantity = int(input(f"Enter new quantity for {item}: "))
        inventory[item] = new_quantity
        print(f"{item} updated to {new_quantity}.")
    else:
        print(f"{item} not found. Adding it to inventory.")
        new_quantity = int(input(f"Enter quantity for new item {item}: "))
        inventory[item] = new_quantity
        print(f"{item} added with quantity {new_quantity}.")

while True:
    print("\n--- Inventory Menu ---")
    print("1. Display Inventory")
    print("2. Update/Add Item")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        display_inventory()
    elif choice == "2":
        update_inventory()
    elif choice == "3":
        print("Exiting Inventory System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
