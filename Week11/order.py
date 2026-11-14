from orderline import OrderLine
from product import Product
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount: DiscountStrategy = discount if discount is not None else NoDiscount()

        # Order class already accepts any class that inherits from DiscountStrategy.
        # So no need to change anything after adding a new DicountStrategy class
        # This demonstrates the Open-Closed Principle:
        # - Open for extension: You can add new discount strategies.
        # - Closed for modification: You don't need to modify the existing Order class.

    @property
    def order_id(self) -> str:
        return self.__order_id

    @property
    def order_lines(self) -> list[OrderLine]:
        return self.__order_lines.copy()


    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, index: int) -> bool:
        if index < 0 or index >= len(self.__order_lines):
            return False
        self.__order_lines.pop(index)
        return True


    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.__order_lines)
        return self.__discount.apply(total)


    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

        
