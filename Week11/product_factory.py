from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

class ProductFactory():
    
    @staticmethod 
    #@staticmethod decorator transforms a method inside a class into a static method 
    # that does not receive an implicit first argument (self or cls). 
    # It behaves just like a regular standalone function, except that it lives inside a class's namespace.

    #Flexible calling. You can call a static method directly on the class (ClassName.method()) without creating an object, 
    # or on an instance (instance.method()) without triggering a TypeError
    def create(product_type: str, product_id:str, name:str, price:float, stock_quantity:int, supplier:Supplier, 
               download_size:float | None = None, weight:float | None = None) -> Product:
        # polymorphism: Even though the factory creates a PhysicalProduct, it returns it through the common Product type.
        if product_type == "physical":
            if weight is None:
                raise ValueError("Physical product requires a weight.")
            
            return PhysicalProduct(product_id, name, price, stock_quantity, weight, supplier)

        elif product_type == "digital":
            if download_size is None:
                raise ValueError("Digital product requires a download size.")
            
            return DigitalProduct(product_id, name, price, stock_quantity, download_size, supplier)
        
        else:
            raise ValueError(f"Unknown product type: {product_type}")