from dataclasses import dataclass
from Modules.utilities import validate_email
from Modules.Exception.exception import InvalidEmailException

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
        try:
            self.id = int(self.id)
            if self.id <= 0:
                raise ValueError("User ID must be a positive integer.")
        except (ValueError, TypeError):
            raise ValueError("User ID must be a valid positive integer.")

        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("User name cannot be empty.")

        if not validate_email(self.email):
            raise InvalidEmailException(f"Invalid email: {self.email}")

        try:
            self.age = int(self.age)
            if self.age <= 0 or self.age > 120:
                raise ValueError("Age must be between 1 and 120.")
        except (ValueError, TypeError):
            raise ValueError("Age must be a valid integer.")

        if self.employed not in (0, 1):
            raise ValueError("Employed status must be 0 or 1.")

        try:
            self.income = float(self.income)
            if self.income < 0:
                raise ValueError("Income cannot be negative.")
        except (ValueError, TypeError):
            raise ValueError("Income must be a valid non-negative number.")

        try:
            self.credit_score = int(self.credit_score)
            if self.credit_score < 0:
                raise ValueError("Credit score cannot be negative.")
        except (ValueError, TypeError):
            raise ValueError("Credit score must be a valid integer.")