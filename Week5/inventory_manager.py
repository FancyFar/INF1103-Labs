import json
import os

INVENTORY_FILE = 'Week5/inventory.json'

def add_product(inventory):

    print("\nAdd New Product")
    while True:
        user_input_ID = input("Product ID: ").strip() #method removes leading and trailing characters from a string

        if user_input_ID:
            break
        
        print("Product ID cannot be empty.")

        
    while True:
        user_input_Name = input("Name: ").strip()

        if user_input_Name:
            break
        print("Product Name cannot be empty.")

    while True:
        try:
            user_input_Price = float(input("Price: "))
            if user_input_Price < 0:
                print("Price cannot be negative.")
                continue
            break

        except ValueError:
            print("Error: Invalid input. Please enter a number.")

    while True:
        try:
            user_input_Stock = int(input("Stock Quantity: "))
            if user_input_Stock < 0:
                print("Stock cannot be negative.")
                continue
            break

        except ValueError:
                    print("Error: Invalid input. Please enter a number.")

    new_item = {"id": user_input_ID, "name": user_input_Name, "price": user_input_Price, "stock": user_input_Stock}

    inventory.append(new_item)
    print("Product added successfully!")
    return inventory

    # try:
    #     with open(INVENTORY_FILE, "w") as file: #creates a new file if file doesn't exist
    #         json.dump(new_item, file, indent=4)
    #         print("\nProduct added successfully!")

    # except TypeError as e:
    #     print(f"Serialization Error: Your data contains a non-JSON object. Details: {e}")

    # except OSError as e:
    #     print(f"System Error: A file system error occurred. Details: {e}")


def update_stock(inventory):
    print("\nUpdate Stock")

    while True:
        to_find_id = input("Enter Product ID: ").strip()

        if to_find_id:
            break
        print("Please enter a valid Product ID.")

    for item in inventory:
        if item["id"] == to_find_id:
            print("\nProduct Found:")
            print(f"Name: {item["name"]}\nCurrent Stock: {item["stock"]}\n")

            while True:
                try:
                    new_stock = int(input("New Stock Quantity: "))
                    if new_stock < 0:
                        print("Stock cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Error: Invalid input. Please enter a number.")

            item["stock"] = new_stock
            print("Stock updated successfully!")
            return
    print(f"Product with ID {to_find_id} does not exists in the inventory.")


def search_product(inventory):
    print("\nSearch Product")

    while True:
        search_id = input("Enter Product ID: ").strip()

        if search_id:
            break
        print("Product ID cannot be empty.")

    for item in inventory:
        if item["id"] == search_id:
            print("\nProduct Found\n" + "-" * 50)
            print(f"ID: {item["id"]}\nName: {item["name"]}\nPrice: ${item["price"]:.2f}\nStock: {item["stock"]}")
            print("-" * 50)
            return
        
    print("Product not found.")


def display_all(inventory):

    if len(inventory) > 0 :
        print("\nCurrent Inventory\n" + "-" * 50)
        for item in inventory:
            print(f"ID: {item.get("id")} | Name: {item["name"]} | Price: ${item.get("price"):.2f} | Stock: {item["stock"]}")
        print("-" * 50)
    else:
        print("\nInventory is empty.")

    return 0

def load_inventory():
    # if no inventory file, begin with empty inventory
    if os.path.exists(INVENTORY_FILE):
        print("\ninventory.json found.")

        try:
            with open(INVENTORY_FILE, "r") as file:
                # json.load() returns a Python list of dictionaries
                inventory = json.load(file)
                print("Inventory loaded successfully.")
                return inventory
            
        except json.JSONDecodeError as e:
            print(f"Error reading from JSON file: {e}")
            return [] #empty list if no inventory file

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    else:
        print("\ninventory is not found.")
        print("Starting with empty inventory.")
        return [] #empty list if no inventory file

def save_inventory(inventory, exit):
    try:
        with open(INVENTORY_FILE, "w") as file: #creates a new file if file doesn't exist
            json.dump(inventory, file, indent=4)
            if exit:
                print("Inventory saved successfully.")
            else:
                print("Inventory saved successfully to inventory.json.")
    
    except TypeError as e:
        print(f"Serialization Error: Your data contains a non-JSON object. Details: {e}")

    except OSError as e:
        print(f"System Error: A file system error occurred. Details: {e}")


def main():
    print("=" * 50 + "\nINVENTORY MANAGEMENT SYSTEM\n" + "=" * 50)

    inventory = load_inventory()

    print("\n----------- MENU -----------")
    print("1. Display All Products\n2. Add product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit ")
    print("-" * 28)

    exit = True

    while True:
        option = input("\nEnter option: ")

        if option == "1":
            display_all(inventory)
            

        elif option == "2":
            add_product(inventory)

        elif option == "3":
            update_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory, exit=False)

        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory, exit)

            print("\nThank you for using Inventory Management System.\nProgram terminated.")
            break
            

if __name__ == "__main__":
    main()