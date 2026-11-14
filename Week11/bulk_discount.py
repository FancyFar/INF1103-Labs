from discount_strategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: int, amount: float):
        self.__threshold: int = threshold
        self.__amount: float = amount

    def apply(self, total: float) -> float:
        if total < 0:
            raise ValueError("Total cannot be less than 0.")
        if total >= self.__threshold:
            return total - self.__amount
        return total 

