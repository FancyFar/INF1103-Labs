from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product import Product
from inventory import Inventory
from order import Order
from orderline import OrderLine
from discount_strategy import DiscountStrategy
from bulk_discount import BulkDiscount
from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from product_factory import ProductFactory

import csv


#========================================================
# 2.3	Use a strategy in Order 
#========================================================

supplier1 = Supplier(101, "ABC Electronics", "abc@gmail.com")
product1 = PhysicalProduct(
    "P001", "Keyboard", 250, 10, 0.5, supplier1
)

# Section 2.3 Predict First
order1 = Order("ORD001", BulkDiscount(200, 20))
order1.add_order_line(product1, 1)

print(f"Bulk Discount: ${order1.calculate_total():.2f}")

order2 = Order("ORD002")
order2.set_discount(PercentageDiscount(10))
order2.add_order_line(product1, 1)

print(f"Percentage Discount: ${order2.calculate_total():.2f}")

#========================================================
# 3.	Implement the Factory pattern: creating products 
#========================================================

def add_product(inventory: Inventory) -> None:
    print("\nAdd New Product")

    while True:
        product_choice = input("Choose product type (1 for physical / 2 for digital): ").strip()

        if product_choice in ("1", "2"):
            break

        print("Invalid choice. Please enter 1 or 2.")

    while True:
        supplier_sid = int(input("Supplier id: "))

        if not supplier_sid:
            print("Supplier ID cannot be empty.")
        else:
            break

    while True:
        supplier_name = input("Supplier name: ").strip()

        if not supplier_name:
            print("Supplier name cannot be empty.")
        else:
            break

    while True:
        supplier_contact = input("Supplier contact email: ").strip()

        if not supplier_contact:
            print("Supplier contact email cannot be empty.")
        else:
            break

    supplier = Supplier(supplier_id=supplier_sid, name=supplier_name, contact_email=supplier_contact)

    while True:    
        product_id = input("Product ID: ").strip()

        if not product_id:
            print("Product ID cannot be empty.")
        elif inventory.find_product(product_id):
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

            if price <= 0:
                print("Price must be greater than zero.")
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
                product = ProductFactory.create("physical", product_id, name, price, stock, supplier,  weight=weight)
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
                product = ProductFactory.create("digital", product_id, name, price, stock, supplier, download_size=download_size)
                break

            except ValueError:
                print("Error: Please enter a valid download size.")

    if inventory.add_product(product):
        return True
    return False

inventory = Inventory()


inventory.display_all_products()

while True:
    user_input = input("Add Product? y/n: ")
    if user_input == "y":
        add_product(inventory)

    elif user_input == "n":
        break

    else:
        print("Invalid command.")
        continue

inventory.display_all_products()

# supplier1 = Supplier(101, "ABC Electronics", "abc@gmail.com")
# try:
#     product = ProductFactory.create(
#         "service", "S001", "Cleaning", 50.00, 10, supplier1
#     )

# except ValueError as e:
#     print(e)
# Output: Unknown product type: service

#========================================================
# 5.	Handle exceptions gracefully 
#========================================================

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50") 



def add_product(inventory: Inventory) -> None:
    print("\nAdd New Product")

    while True:
        product_choice = input("Choose product type (1 for physical / 2 for digital): ").strip()

        if product_choice in ("1", "2"):
            break

        print("Invalid choice. Please enter 1 or 2.")

    while True:
        supplier_sid = int(input("Supplier id: "))

        if not supplier_sid:
            print("Supplier ID cannot be empty.")
        else:
            break

    while True:
        supplier_name = input("Supplier name: ").strip()

        if not supplier_name:
            print("Supplier name cannot be empty.")
        else:
            break

    while True:
        supplier_contact = input("Supplier contact email: ").strip()

        if not supplier_contact:
            print("Supplier contact email cannot be empty.")
        else:
            break

    supplier = Supplier(supplier_id=supplier_sid, name=supplier_name, contact_email=supplier_contact)

    while True:    
        product_id = input("Product ID: ").strip()

        if not product_id:
            print("Product ID cannot be empty.")
        elif inventory.find_product(product_id):
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

            if price <= 0:
                print("Price must be greater than zero.")
                continue
            break

        except ValueError:
            print("Error: Please enter a valid number.")

    price = get_positive_float("Price: ")



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

        weight = get_positive_float("Weight (kg): ")

        product = ProductFactory.create("physical", product_id, name, price, stock, supplier,  weight=weight)
    else:

        download_size = get_positive_float("Download Size (MB): ")

        product = ProductFactory.create("digital", product_id, name, price, stock, supplier, download_size=download_size)




    if inventory.add_product(product):
        return True
    return False

inventory = Inventory()


inventory.display_all_products()

while True:
    user_input = input("Add Product? y/n: ")
    if user_input == "y":
        add_product(inventory)

    elif user_input == "n":
        break

    else:
        print("Invalid command.")
        continue

inventory.display_all_products()

prompt = "Enter input: "

print(get_positive_float(prompt=prompt))

#========================================================
# 5.2	Loading products from a file 
#========================================================

FILE_PATH = "Week11/products.csv"
inventory = Inventory()
supplier1 = Supplier(101, "ABC Electronics", "abc@gmail.com")

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0

    try:
        file = open(path, newline="")

    except FileNotFoundError:
        print(f"Products file not found {path}")

    else:
        with file:
            # read rows with csv.reader
            data = csv.reader(file)
            next(data, None) # skip the header row

            # for each row: try to create and add the product
           
            for row in data:
                try:
                    # Extract and convert common product information
                    product_type = row[0]
                    product_id = row[1]
                    name = row[2]
                    price = float(row[3])
                    stock = int(row[4])

                    # Create product
                    if product_type == "physical":
                        weight = float(row[5])

                        product = ProductFactory.create(
                            "physical",
                            product_id,
                            name,
                            price,
                            stock,
                            supplier,
                            weight=weight
                        )
                    elif product_type == "digital":
                        download_size = float(row[6])
                        product = ProductFactory.create(
                            "digital",
                            product_id,
                            name,
                            price,
                            stock,
                            supplier,
                            download_size=download_size
                        )
                    else:
                        raise ValueError(f"Unknown product type: {product_type}")

                    # Add product to inventory
                    if inventory.add_product(product):
                        loaded += 1

                except ValueError as e: # except ValueError: report the row and continue
                    print(f"Invalid data in row {row}: {e}")

            print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished")

load_products(FILE_PATH, inventory, supplier1)
inventory.display_all_products()
