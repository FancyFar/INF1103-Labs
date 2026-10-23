from product import Product


class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> bool: 
        # Prevent duplicate product IDs
        if self.search_product(product.product_id) is not None:
            print("Error: Product ID already exists.")
            return False

        self.__products.append(product)
        return True

    def search_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def display_all(self) -> None:
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

    