from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product import Product
from inventory import Inventory
from order import Order
from orderline import OrderLine

#========================================================
# Step 2: Implement association: Supplier and Product
#========================================================
# After deleting the supplier1 variable, the Product object can still display the supplier's information. This is because the Product object stores a reference to the Supplier object through self.__supplier = supplier in its constructor. 
# Deleting supplier1 only removes the external reference, but the Supplier object still exists because the Product object holds another reference to it.
# The key concept to remember:
# Deleting a variable is not the same as deleting the object it references.
# This is why object association works: a Product can maintain access to its Supplier even when the original Supplier variable is deleted.
# Association - No ownership just referencing
# A Product is not a whole that contains a Supplier as one of its parts. The objects are collaborating through a reference.

supplier1 = Supplier(101, "ABC Electronics", "abc@gmail.com")
product1 = PhysicalProduct("P001", "Keyboard", 50, 10, 0.5, supplier1)
product1.supplier.display_information()

product2 = DigitalProduct("P002", "Mouse", 40, 20, 0.1, supplier1)
product2.supplier.display_information()

# Confirm both products reference the same Supplier object
print("Same Supplier:", product1.supplier is product2.supplier) #True

supplier2 = Supplier(102, "Independent Supplier", "test@gmail.com")

print("\nSupplier exists independently:")
supplier2.display_information()

del supplier1

print("AFTER DELETING SUPPLIER1")
product1.supplier.display_information()

#========================================================
# Step 3: Implement aggregation: Inventory and Product
#========================================================
# the Product object can still work after being removed from Inventory A. 
# This is because removing the product only removes its reference from Inventory A's collection. 
# The Product object still exists because the external variable product1 holds a reference to it. 
# Therefore, it can still be used independently and added to another inventory, such as Inventory B.

supplier1 = Supplier(101, "ABC Electronics", "abc@gmail.com")
product1 = PhysicalProduct("P001", "Keyboard", 50, 10, 0.5, supplier1)

inventoryA = Inventory()

print("Add product1 to Inventory A")
inventoryA.add_product(product1)

print("Remove product1 from Inventory A")
inventoryA.remove_product(product1.product_id)

print("Inventory A")
# Confirm Inventory A is empty
inventoryA.display_all_products()

print("\nProduct1 Info")
# Product still exists independently
product1.display_information()

inventoryB = Inventory()

# Add the same Product to Inventory B
inventoryB.add_product(product1)

print("\nInventory B")
# Confirm Inventory B contains the Product
inventoryB.display_all_products()

# Confirm Inventory B contains the original Product object
print(
    "Same Product object:",
    inventoryB.get_products()[0] is product1
) # True

#========================================================
# Step 4: Implement composition: Order and OrderLine
#========================================================
supplier1 = Supplier(101, "ABC Electronics", "abc@gmail.com")

product1 = PhysicalProduct(
    "P001", "Keyboard", 50, 10, 0.5, supplier1
)

product2 = DigitalProduct(
    "P002", "Software", 100, 20, 500, supplier1
)

# Create first order
order1 = Order("O001")

order1.add_order_line(product1, 2)
order1.add_order_line(product2, 1)

# Display first order
for line in order1.order_lines:
    print(
        f"Product: {line.product.name} | "
        f"Quantity: {line.quantity} | "
        f"Subtotal: ${line.calculate_subtotal():.2f}"
    )

print(f"Order Total: ${order1.calculate_total():.2f}")

# Create second order using the same Product
order2 = Order("O002")
order2.add_order_line(product1, 3)

# Compare objects
line1 = order1.order_lines[0] # product1, 2
line2 = order2.order_lines[0] # product1, 3

print("\nObject Comparison")
print("Same OrderLine:", line1 is line2) # False
print("Same Product:", line1.product is line2.product) # True

# Confirm OrderLine references the original Product
print("OrderLine references original Product:", line1.product is product1) #True

# Remove an OrderLine from Order 1
order1.remove_order_line(0)

print("\nAfter removing OrderLine from Order 1:")
print("Order 1 total:", order1.calculate_total()) # 1 * 100 = 100
print("Order 2 total:", order2.calculate_total()) # 3 * 50 = 150

# Product still exists independently
product1.display_information()

print("Order 2 still references Product:", line2.product is product1) #True

#========================================================
# Apply the Liskov Substitution Principle (LSP)
#========================================================
# main idea of the Liskov Substitution Principle (LSP): 
# it stores Product objects and calls methods such as display_information() 
# without checking whether each object is a PhysicalProduct or DigitalProduct.
# Subclasses must still behave correctly wherever the parent class is expected.

# LSP means that if a function is written to work with a Product, it should continue working regardless of whether it 
# receives a PhysicalProduct or DigitalProduct. 
# You should fix a subclass that breaks this expectation rather than adding special-case checks to Inventory.

# a function that accepts any Product
def show_product_detail(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())
    print("-" * 60)

# Create a supplier
supplier1 = Supplier(101, "ABC Electronics", "abc@gmail.com")

product1 = PhysicalProduct(
    "P001", "Keyboard", 50, 10, 0.5, supplier1
)

product2 = DigitalProduct(
    "P002", "Software", 100, 20, 500, supplier1
)

# 1. Test substitutability
print("Testing Physical Product:")
show_product_detail(product1)

print("\nTesting Digital Product:")
show_product_detail(product2)

# 2. Test in Inventory
inventory = Inventory()

print("Adding products to Inventory...")
print(inventory.add_product(product1))
print(inventory.add_product(product2))

print("\nDisplaying all products:")
inventory.display_all_products()

# 3. Test inherited Product behaviour
print("\nTesting update_stock():")

product1.update_stock(15)
product2.update_stock(30)

print("Physical Product stock (product1)", product1.stock)
print("Digital Product stock (product2)", product2.stock)


# # 4. Test invalid input for update_stock()
# print("\nTesting invalid inputs:")
# # product1.update_stock("test") # should raise  ValueError
# #product1.update_stock(1.1) # should raise ValueError
# #product1.update_stock(-1) # should raise ValueError

#========================================================
# Polymorphism: work with different Product types
#========================================================
# Different subclasses respond differently to the same method call.

supplier1 = Supplier(101, "ABC Electronics", "abc@gmail.com")

product1 = PhysicalProduct(
    "P001", "Keyboard", 50, 10, 0.5, supplier1
)

product2 = DigitalProduct(
    "P002", "Software", 100, 20, 500, supplier1
)


inventory = Inventory()

print("Adding products to Inventory...")
print(inventory.add_product(product1))
print(inventory.add_product(product2))

print("\nDisplaying products and fulfilment information:")
print("-" * 60)
for product in inventory.products:
    product.display_information()
    print(product.get_fulfilment_info())
    print("-" * 60)
