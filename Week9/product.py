from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, product_type: str):
        self._product_id = product_id # double underscore __ is private
        self._name = name
        self._price = price
        self._stock = stock
        self._product_type = product_type

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    # getters
    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    @property
    def product_type(self):
        return self._product_type


    def update_stock(self, quantity: int) -> None:
        '''
        Update a product stock
        '''
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise ValueError("Stock must be a whole number.")

        if quantity < 0:
            raise ValueError("Stock cannot be negative.")

        self._stock = quantity

     
    def display_information(self) -> None:
        '''
        Display a product
        '''
        print(
            f"ID: {self._product_id} | "
            f"Name: {self._name} | "
            f"Price: ${self._price:.2f} | "
            f"Stock: {self._stock} ")


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
       pass
       
                   


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight: float): # add weight (kg)
        super().__init__(product_id, name, price, stock, "physical")
        self.__weight  = weight

    @property
    def get_weight(self):
        return self.__weight

    def display_information(self) -> None : # Method overriding 
        '''
        Display information of Physical Product
        ''' 
        super().display_information()
        print(f"Weight: {self.__weight:.2f} KG")
        # print(
        #             f"ID: {self._product_id} | "
        #             f"Name: {self._name} | "
        #             f"Price: ${self._price:.2f} | "
        #             f"Stock: {self._stock} | "
        #             f"Weight: {self.__weight}" )

    def get_fulfilment_info(self) -> str:
        return "Physical product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 2.00
       



class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size:float): # add download_size (MB)
        super().__init__(product_id, name, price, stock, "digital")
        self.__download_size = download_size

    @property
    def get_download_size(self):
        return self.__download_size 

    def display_information(self) -> None: # Method overriding 
        '''
            Display information of Digital Product
        ''' 
        super().display_information()
        print(f"Download Size: {self.__download_size: .2f} MB")
        # print(
        #                     f"ID: {self._product_id} | "
        #                     f"Name: {self._name} | "
        #                     f"Price: ${self._price:.2f} | "
        #                     f"Stock: {self._stock} | "
        #                     f"Dowbload Size: {self.__download_size}" )

    def get_fulfilment_info(self) -> str:
            return "Digital product is delivered digitally."



