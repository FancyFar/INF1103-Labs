from supplier import Supplier
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):

        if price <= 0:
            raise ValueError("Product price must be greater than 0.")
        if not isinstance(stock, int) or isinstance(stock, bool):
            raise ValueError("Stock must be a whole number.")

        if stock < 0:
            raise ValueError("Stock cannot be negative.")


        self.__product_id: str = product_id # double underscore __ is private
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier

    # getters
    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    @property
    def supplier(self) -> Supplier:
        return self.__supplier

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass


    def update_stock(self, quantity: int) -> None:
        '''
        Update a product stock
        '''
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise ValueError("Stock must be a whole number.")

        if quantity < 0:
            raise ValueError("Stock cannot be negative.")

        self.__stock = quantity

     
    def display_information(self) -> None:
        '''
        Display a product
        '''
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}")
                   

        