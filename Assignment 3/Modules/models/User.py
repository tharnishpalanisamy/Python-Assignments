from dataclasses import dataclass
from Modules.utilities import validate_email

@dataclass
class User:
    id: int 
    name: str 
    email: str 
    age: int 
    employed: int 
    income: float 
    credit_score: int 

    def __post_init__(self):
        self.id = int(self.id)
        self.age = int(self.age)
        self.employed = int(self.employed)
        self.income = float(self.income)
        self.credit_score = int(self.credit_score)

        if not str(self.name).strip():
            raise ValueError("User name cannot be empty.")
        if not validate_email(self.email):
            raise ValueError(f"Invalid email: {self.email}")
        if self.age <= 0 or self.age > 120:
            raise ValueError("Age must be between 1 and 120.")
        if self.employed not in (0, 1):
            raise ValueError("Employed status must be 0 or 1.")
        if self.income < 0:
            raise ValueError("Income cannot be negative.")
        if self.credit_score < 0:
            raise ValueError("Credit score cannot be negative.")