from discount_strategy import DiscountStrategy

class NoDiscount(DiscountStrategy):

    def apply(self, total: float) -> float:
        if total < 0:
            raise ValueError("Total cannot be less than 0.")
        return total