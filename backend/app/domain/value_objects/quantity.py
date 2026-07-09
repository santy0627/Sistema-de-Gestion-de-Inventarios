from dataclasses import dataclass

@dataclass (frozen=True)
class Quantity:
    value: int

    def __post_init__(self):
        if self.value < 0:
            raise ValueError("No puedes tener una cantidad negativa")
        
    def _ensure_compatible(self, other:"Quantity"):
        if not isinstance(other, Quantity):
            raise TypeError("El valor no es compatible")
    
    def add(self, value: "Quantity") -> "Quantity":
        return Quantity(self.value + value.value)

    def subtract(self, value: "Quantity") -> "Quantity":
        subtraction = self.value - value.value

        if subtraction < 0:
            raise ValueError("No puedes restar mas de lo que tienes")
        else:
            return Quantity(subtraction)