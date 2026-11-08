from product import Product

class Inventory:
    def __init__(self):
        # Inventory class manages Product objects. 
        # This is an example of aggregation: an Inventory groups Product objects, 
        # but the products can exist independently of the inventory.
        
        self.__products: list[Product] = []

    @property
    def products(self) -> list[Product]:
        return self.__products

    def add_product(self, product: Product) -> bool: 
        # Prevent duplicate product IDs
        if self.find_product(product.product_id) is not None:
            print("Error: Product ID already exists.")
            return False

        self.__products.append(product)
        return True

    def remove_product(self, product_id: str) -> bool:
        # Check if item exists first
        product = self.find_product(product_id)

        if product is None:
            print("Error: Product ID does not exists.")
            return False

        self.__products.remove(product)
        return True

    def find_product(self, product_id: str) -> Product | None: # find product
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def display_all_products(self) -> None:
        if not self.__products:
            print("\nInventory is empty.")
            return

        print("\nCurrent Inventory\n" + "-" * 60 )

        for product in self.__products:
            product.display_information()

        print("-" * 60)

    def get_products(self) -> list[Product]:
        # return copy of the list 
        return self.__products.copy()

    