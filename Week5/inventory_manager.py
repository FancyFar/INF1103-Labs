import json
import os

INVENTORY_FILE = 'inventory.json'

def display_all(inventory):
    print("\nCurrent Inventory")
    print('-' * 50)

    if len(inventory) == 0:
        print("Inventory is empty")
    else:
        for item in inventory:
            print(
                f"ID: {item["id"]} | Name: {item["name"]} | Price: ${item["price"]:.2f} | Stock: {item["stock"]}" 
            )
    print('-' * 50)

def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        print("\ninventory.json found.")

        try:
            with open(INVENTORY_FILE, "r") as file:
                inventory = json.load(file)

            print("Inventory loaded successfully.")
            return inventory #return dictionary

        except json.JSONDecodeError:
            print("Error: inventory.json is invalid")
            return []

    else:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")
        return []

def save_inventory(inventory):

    try:
        with open(INVENTORY_FILE, "w") as file:
            # write to file
            json.dump(inventory, file, indent=4)
            print("Inventory saved successfully to inventory.json.")

    except FileNotFoundError as e:
        print(f"inventory.json not found: {e}")



def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    inventory = load_inventory()

    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

    while True:

        option = input("\nEnter option: ")

        if option == "1":
            display_all(inventory)

        # elif option == "2":
        #     add_product(inventory)

        # elif option == "3":
        #     update_stock(inventory)

        # elif option == "4":
        #     search_product(inventory)

        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)

        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)

            print("\nThank you for using Inventory Management System. Program terminated. ")
            break

        else:
            print("Invalid option. Please try again.")


main()


