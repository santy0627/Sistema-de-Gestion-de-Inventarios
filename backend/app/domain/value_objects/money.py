from dataclasses import dataclass
from app.domain.enums.currency import Currency
from decimal import Decimal

@dataclass (frozen=True)
class Money:
    amount: Decimal
    currency: Currency

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("No puedes tener una cantidad negativa")
        
        if not self.currency:
            raise ValueError("Necesitas tener una moneda")
        

    def _ensure_compatible(self, other:"Money"):
        if not isinstance(other, Money):
            raise TypeError("El valor no es compatible")

        if other.currency != self.currency:
            raise ValueError("No puedes operar con monedas distintas")

    def add(self, other: "Money") -> "Money":
        self._ensure_compatible(other)
        
        return  Money(
            self.amount + other.amount,
            self.currency
        )
        
    def subtract(self, other: "Money") -> "Money":
        self._ensure_compatible(other)

        if self.amount - other.amount >= 0:
            return Money(self.amount - other.amount, self.currency)
        else:
            raise ValueError("No puedes quedar con un valor negativo")
        
    def multiply(self, value: int) -> "Money":   
        if value < 0:
            raise ValueError("No puedes multiplicar por un valor negativo")

        return Money(self.amount * value, self.currency)
   