from discount_strategy import DiscountStrategy

class StudentDiscount(DiscountStrategy):
    # Make student Discount to be 5%
    def apply(self, total):
        if total < 0:
            raise ValueError("Total cannot be less than 0.")
        return 0.95 * total