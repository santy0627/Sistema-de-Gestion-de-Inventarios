from dataclasses import dataclass
from app.domain.value_objects.money import Money

@dataclass
class Product:
    name:str 
    sku:str
    brand:str
    category:str
    suggested_price: Money
    serial_control:bool
    status:bool = True

    def __post_init__(self):
        empty_field_error = "El campo no puede estar vacio"

        if not self.name:
            raise ValueError(empty_field_error)
        if not self.category:
            raise ValueError(empty_field_error)
        if not self.sku:
            raise ValueError(empty_field_error)
        if not self.brand:
            raise ValueError(empty_field_error)
        

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.sku == other.sku
    
    def __hash__(self):
        return hash(self.sku)

    def _ensure_active(self) -> None:
        if not self.status:
            raise ValueError("No puedes hacer cambios de un objeto descontinuado")

    def change_name (self, newname:str) -> None:
        self._ensure_active()
        if not newname:
            raise ValueError("El nombre no puede estar vacio")
        self.name = newname

    def change_price(self, newprice: "Money") -> "Money":
        self._ensure_active()
        if not isinstance(newprice, Money):
            raise TypeError("El valor no es compatible")
        self.suggested_price = newprice

    def change_brand(self, newbrand:str) -> None:
        self._ensure_active()
        if not newbrand:
            raise ValueError("El objeto debe tener alguna marca")
        self.brand = newbrand

    def change_category(self, newcategory:str) -> None:
        self._ensure_active()
        if not newcategory:
            raise ValueError("Debes incluir el producto en una categoria")
        self.category = newcategory

    def activate(self) -> None:
        self.status = True

    def deactivate(self) -> None:
        self.status = False 