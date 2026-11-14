from abc import ABC, abstractmethod

class DiscountStrategy(ABC):

    @abstractmethod
    def apply(self, total: float) -> float:
        pass
# Child classes: NoDiscount, PercentageDiscount, BulkDiscount
# Strategy Design Pattern and polymorphism (def apply())
# advantage is that you can use any discount strategy through the same apply() method.

# You don't need to know which specific discount class is being used. You just call apply().
# Key takeaway: Inheritance ensures all discount classes follow the same interface, while polymorphism allows each class to implement apply() differently.