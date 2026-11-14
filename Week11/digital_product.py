from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size:float, supplier: Supplier): # add download_size (MB)
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size

    @property
    def get_download_size(self) -> float:
        return self.__download_size 

    def display_information(self) -> None: # Method overriding 
        '''
        Display information of Digital Product
        ''' 
        super().display_information()
        print(f"Download Size: {self.__download_size: .2f} MB")


    def get_fulfilment_info(self) -> str:
        return "Digital product is delivered digitally."
    
