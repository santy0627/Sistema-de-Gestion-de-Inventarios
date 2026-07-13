from dataclasses import dataclass, field
from datetime import datetime
import uuid

from app.domain.entities.product import Product
from app.domain.value_objects.quantity import Quantity
from app.domain.enums.MovementType import MovementType

@dataclass(frozen=True)
class InventoryMovement:
    product: Product
    quantity: Quantity
    movement_type: MovementType
    movement_date: datetime = field(default_factory=datetime.now)
    movement_id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __eq__(self, other):
        if not isinstance(other, InventoryMovement):
            return NotImplemented
        return self.movement_id == other.movement_id

    def __hash__(self):
        return hash(self.movement_id)

    def __post_init__(self):
        if self.quantity.value == 0:
            raise ValueError("La cantidad no puede ser cero")

    def signed_quantity(self) -> int:
        if self.movement_type == MovementType.PURCHASE:
            return self.quantity.value
        elif self.movement_type == MovementType.SALE:
            return -self.quantity.value
        raise ValueError("Tipo de movimiento no válido")