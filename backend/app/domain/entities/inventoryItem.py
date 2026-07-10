from dataclasses import dataclass
from app.domain.value_objects.quantity import Quantity
from app.domain.entities.product import Product

@dataclass
class InventoryItem:
    product: Product
    quantity: Quantity

    def __post_init__(self):
        if not self.product:
            raise ValueError("Necesitas añadir un producto")
        
    def __eq__(self, other):
        if not isinstance(other, InventoryItem):
            return NotImplemented
        return self.product == other.product
    
    def __hash__(self):
        return hash(self.product)
    