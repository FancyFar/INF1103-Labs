import json
from pathlib import Path

from product import Product, PhysicalProduct, DigitalProduct, CanBeShipped
from inventory import Inventory

INVENTORY_FILE = Path("Week9/inventory.json")

def load_inventory() -> Inventory:
    inventory = Inventory()

    if not INVENTORY_FILE.exists():
        print("\nInventory file not found. Starting with empty inventory.")
        return inventory

    try:
        with INVENTORY_FILE.open("r") as file:
            data = json.load(file)

        print("inventory.json found.")

        if not isinstance(data, list):
            print("Error: Inventory JSON must contain a list,")
            print("Starting with empty inventory.")
            return inventory

        for item in data:
            if not isinstance(item, dict):
                print("Warning: Skipping an invalid record.")
                continue

            try:
                product_id = item["id"]
                name = item["name"]
                price = item["price"]
                stock = item["stock"]
                product_type = item["type"]

                # Validate values before creating the object.
                if not isinstance(product_id, str) or not product_id.strip():
                    raise ValueError("Invalid product ID.") 

                if not isinstance(name, str) or not name.strip():
                    raise ValueError("Invalid product name.")

                if (
                    not isinstance(price, (int, float))
                    or isinstance(price, bool)
                    or price < 0
                ):
                    raise ValueError("Invalid product price.")

                if (
                    not isinstance(stock, int)
                    or isinstance(stock, bool)
                    or stock < 0
                ):
                    raise ValueError("Invalid stock quantity.")

                if not isinstance(product_type, str) or not name.strip():
                    raise ValueError("Invalid product type.")

                # product = Product(product_id, name, price, stock)

                if product_type == "physical":
                    weight = item["weight"]

                    if (
                        not isinstance(weight, (int, float))
                        or isinstance(weight, bool)
                        or weight < 0
                    ):
                        raise ValueError("Invalid product weight.")
                    
                    product = PhysicalProduct(product_id, name, price, stock , weight)

                elif product_type == "digital":
                    download_size = item["download_size"]
                    if (
                        not isinstance(download_size, (int, float))
                        or isinstance(download_size, bool)
                        or download_size < 0
                    ):
                        raise ValueError("Invalid download size.")
                    
                    product = DigitalProduct(product_id, name, price, stock, download_size)

                else:
                    print(f"Warning: Invalid product type '{product_type}'. Skipping.")
                    continue

                if not inventory.add_product(product):
                    print(f"Warning: Duplicate ID {product_id} skipped.")

            except (KeyError, TypeError, ValueError) as e:
                print(f"Warning: Skipping invalid product: {e}")

        print("Inventory loaded successfully.")

    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        print("Starting with empty inventory.")

    except OSError as e:
        print(f"File error: {e}")
        print("Starting with empty inventory.")

    return inventory


def save_inventory(inventory: Inventory) -> None:
    try:
        #Convert Product obj to dictionaries for JSON
        data = []

        for product in inventory.get_products():
            # Common attributes shared by all products
                product_data = {
                    "id": product.product_id,
                    "name": product.name,
                    "price": product.price,
                    "stock": product.stock,
                    "type": product.product_type
                }

                # Save subclass-specific attributes
                if isinstance(product, PhysicalProduct):
                    product_data["weight"] = product.get_weight

                elif isinstance(product, DigitalProduct):
                    product_data["download_size"] = product.get_download_size

                data.append(product_data)

        with INVENTORY_FILE.open("w") as file:
            json.dump(data, file, indent=4)


        print("Inventory saved successfully.")

    except (OSError, TypeError, ValueError) as e:
        print(f"Error saving inventory: {e}")


def add_product(inventory: Inventory) -> None:
    print("\nAdd New Product")

    while True:
        product_choice = input("Choose product type (1 for physical / 2 for digital): ").strip()

        if product_choice in ("1", "2"):
            break

        print("Invalid choice. Please enter 1 or 2.")

    while True:    
        product_id = input("Product ID: ").strip()

        if not product_id:
            print("Product ID cannot be empty.")
        elif inventory.search_product(product_id):
            print("Product ID already exists.")
        else:
            break

    while True:
        name = input("Name: ").strip()

        if name: 
            break

        print("Product Name cannot be empty,")

    while True:
        try:
            price = float(input("Price: "))

            if price < 0:
                print("Price cannot be negative.")
                continue
            break

        except ValueError:
            print("Error: Please enter a valid number.")


    while True:
        try:
            stock = int(input("Stock Quantity: "))

            if stock < 0:
                print("Stock cannot be negative.")
                continue
            break

        except ValueError:
            print("Error: Please enter a whole number.")

    # product = Product(product_id, name, price, stock)
    if product_choice == "1":
        while True:
            try:
                weight = float(input("Weight (kg): "))

                if weight < 0:
                    print("Weight cannot be negative.")
                    continue
                product = PhysicalProduct(product_id, name, price, stock, weight)
                break
            except ValueError:
                print("Error: Please enter a valid weight")
    else:
        while True:
            try:
                download_size = float(input("Download Size (MB): "))

                if download_size < 0:
                    print("Download size cannot be negative.")
                    continue
                product = DigitalProduct(product_id, name, price, stock, download_size)
                break

            except ValueError:
                print("Error: Please enter a valid download size.")

    if inventory.add_product(product):
        return True
    return False

def update_stock(inventory: Inventory) -> None:
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print(f"Product with ID {product_id} does not exist in the database.")
        return

    print("\nProduct Found:")
    print(f"Name: {product.name}")
    print(f"Current Stock: {product.stock}")


    while True:
        try:
            new_stock = int(input("New Stock Quantity: "))

            product.update_stock(new_stock)

            print("Stock updated successfully!")
            return

        except ValueError as e:
            print(f"Error: {e}")

def search_product(inventory: Inventory) -> None:
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("\nProduct Found\n" + "-" * 50)
    product.display_information()
    print(product.get_fulfilment_info())
    if isinstance(product, CanBeShipped):
        print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
    print("-" * 50)

def main() -> None:
    print("=" * 50 +  "\nINVENTORY MANAGEMENT SYSTEM\n" + "=" * 50)

    inventory = load_inventory()

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products\n2. Add product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit ")
        print("-" * 28)

        option = input("Enter option: ").strip()

        if option == "1":
            inventory.display_all()

        elif option == "2":
            if add_product(inventory):
                 print("Product added successfully!")

        elif option == "3":
            update_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            save_inventory(inventory)

        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)

            print(
                "\nThank you for using Inventory Management System."
                "\nProgram terminated."
            )
            break

        else:
            print("Invalid option. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()






