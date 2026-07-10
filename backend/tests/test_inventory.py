from app.domain.entities.inventoryItem import InventoryItem
from app.domain.entities.product import Product
from app.domain.value_objects.money import Money
from app.domain.value_objects.quantity import Quantity
from app.domain.enums.currency import Currency
from decimal import Decimal
from app.domain.entities.inventory import Inventory
from app.domain.exceptions.inventory_exceptions import ProductNotInInventoryError

product1 = Product("RTX 5070", "GPU-5070", "Nvidia", "GPU", Money(Decimal(5000000), Currency.COP), True)
product2 = Product("RTX 4070", "GPU-4070", "Nvidia", "GPU", Money(Decimal(4000000), Currency.COP), True)
product3 = Product("RTX 3050", "GPU-3050", "Nvidia", "GPU", Money(Decimal(3500000), Currency.COP), True)

item1 = InventoryItem(product1, Quantity(10))
item2 = InventoryItem(product2, Quantity(20))
item3 = InventoryItem(product3, Quantity(30))

def test_search_product():
    inventory = Inventory(items=[item1,item2,item3])
    product = Product("RTX 4070", "GPU-4070", "Nvidia", "GPU", Money(Decimal(8000000), Currency.COP), True)
    result = inventory.search_product(product)
    assert result.product.sku == product.sku and result.quantity == item2.quantity

def test_add_stock():
    inventory = Inventory(items=[item1,item2,item3])
    inventory.add_stock(product2, Quantity(5))
    assert inventory.stock(product2) == Quantity(25)

def test_search_product_error():
    inventory = Inventory(items=[item1,item2,item3])
    product = Product("RTX 4070Ti", "GPU-4070Ti", "Nvidia", "GPU", Money(Decimal(8000000), Currency.COP), True)
    try:
        result = inventory.search_product(product)
    except ProductNotInInventoryError as e:
        assert str(e) == "El producto no existe en el inventario"
