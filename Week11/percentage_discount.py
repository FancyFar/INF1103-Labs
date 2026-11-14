from discount_strategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.__percentage: float = percentage


    def apply(self, total: float) -> float:
        if total < 0:
            raise ValueError("Total must be more than 0.")

        discount = total * (self.__percentage/100)
        return total - discount