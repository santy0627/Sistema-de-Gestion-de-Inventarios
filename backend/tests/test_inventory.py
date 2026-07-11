from app.domain.entities.inventoryItem import InventoryItem
from app.domain.entities.product import Product
from app.domain.value_objects.money import Money
from app.domain.value_objects.quantity import Quantity
from app.domain.enums.currency import Currency
from decimal import Decimal
from app.domain.entities.inventory import Inventory
from app.domain.exceptions.inventory_exceptions import ProductNotInInventoryError
import pytest

@pytest.fixture
def inventory():
    item1 = InventoryItem(Product("RTX 3080", "GPU-3080", "Nvidia", "GPU", Money(Decimal(5000000), Currency.COP), True), Quantity(10))
    item2 = InventoryItem(Product("RTX 4070", "GPU-4070", "Nvidia", "GPU", Money(Decimal(8000000), Currency.COP), True), Quantity(20))
    item3 = InventoryItem(Product("RTX 4090", "GPU-4090", "Nvidia", "GPU", Money(Decimal(15000000), Currency.COP), True), Quantity(5))
    return Inventory(items=[item1, item2, item3])

def test_search_product(inventory):
    product = Product("RTX 4070", "GPU-4070", "Nvidia", "GPU", Money(Decimal(8000000), Currency.COP), True)
    result = inventory.search_product(product)
    assert result.product.sku == product.sku and result.quantity == Quantity(20)

def test_add_stock(inventory):
    product2 = Product("RTX 4070", "GPU-4070", "Nvidia", "GPU", Money(Decimal(8000000), Currency.COP), True)
    inventory.add_stock(product2, Quantity(5))
    assert inventory.stock(product2) == Quantity(25)

def test_search_product_error(inventory):
    product_fantasma = Product("RTX 4070Ti", "GPU-4070Ti", "Nvidia", "GPU", Money(Decimal(8000000), Currency.COP), True)
   
    with pytest.raises(ProductNotInInventoryError) as exc_info:
        inventory.search_product(product_fantasma)

    assert str(exc_info.value) == "El producto no existe en el inventario"