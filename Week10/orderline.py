from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.__product: Product  = product
        self.__quantity: int = quantity


    @property
    def product(self) -> Product:
        return self.__product

    @property
    def quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity