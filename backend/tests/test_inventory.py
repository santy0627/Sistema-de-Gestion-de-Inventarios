from app.domain.entities.inventoryItem import InventoryItem
from app.domain.entities.product import Product
from app.domain.value_objects.money import Money
from app.domain.value_objects.quantity import Quantity
from app.domain.enums.currency import Currency
from decimal import Decimal
from app.domain.entities.inventory import Inventory

producto1 = Product("RTX 5070", "GPU-5070", "Nvidia", "GPU", Money(Decimal(5000000), Currency.COP), True)
producto2 = Product("RTX 4070", "GPU-4070", "Nvidia", "GPU", Money(Decimal(4000000), Currency.COP), True)
producto3 = Product("RTX 3050", "GPU-3050", "Nvidia", "GPU", Money(Decimal(3500000), Currency.COP), True)

producto4 = Product("RTX 4070", "GPU-4070", "Nvidia", "GPU", Money(Decimal(8000000), Currency.COP), True)

item1 = InventoryItem(producto1, Quantity(10))
item2 = InventoryItem(producto2, Quantity(20))
item3 = InventoryItem(producto3, Quantity(30))

inventory = Inventory(items=[item1,item2,item3])

def test_search_product():
    result = inventory.search_product(producto4)
    assert result.product.sku == producto4.sku and result.quantity == item2.quantity