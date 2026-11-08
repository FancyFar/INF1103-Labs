class Supplier:
    def __init__(self, supplier_id: int, name: str, contact_email: str):
        self.__supplier_id: int = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    @property
    def supplier_id(self) -> int:
        return self.__supplier_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def contact_email(self) -> str:
        return self.__contact_email

    def display_information(self) -> None:
        print(f"Supplier id: {self.__supplier_id} | "
              f"Name: {self.__name} | "
              f"Email: {self.__contact_email}" )
