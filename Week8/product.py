class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__product_id = product_id # double underscore __ is private
        self.__name = name
        self.__price = price
        self.__stock = stock

    # getters
    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock


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
                   

        