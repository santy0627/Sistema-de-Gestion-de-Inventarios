from dataclasses import dataclass, field
from app.domain.entities.inventoryItem import InventoryItem
from app.domain.entities.product import Product
from app.domain.value_objects.quantity import Quantity
from app.domain.exceptions.inventory_exceptions import ProductNotInInventoryError

@dataclass
class Inventory:
    items: list[InventoryItem] = field(default_factory=list)

    def search_product(self, product: Product):
        for item in self.items:
            if item.product == product:
                return item
        raise ProductNotInInventoryError("El producto no existe en el inventario")
    
    def stock(self, product: Product) -> Quantity:
        item = self.search_product(product)
        return item.quantity
    
    def add_stock(self, product: Product, quantity: Quantity): 
            item = self.search_product(product)
            newquantity = item.quantity.add(quantity)
            item.quantity = newquantity
