from dataclasses import dataclass 
from Modules.models.User import User 
import math 

@dataclass
class LoanService:
    id: int
    service_name: str 
    interest_rate: float
    duration_months: int
    minimum_age: int 
    maximum_age: int 
    employment_required: bool 
    credit_score_required: int 

    def __post_init__(self):
        try:
            self.id = int(self.id)
            self.interest_rate = float(self.interest_rate)
            self.duration_months = int(self.duration_months)
            self.minimum_age = int(self.minimum_age)
            self.maximum_age = int(self.maximum_age)
            self.credit_score_required = int(self.credit_score_required)
        except (ValueError, TypeError):
            raise ValueError("Invalid numeric fields in LoanService.")

        if self.interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if self.duration_months <= 0:
            raise ValueError("Duration months must be greater than zero.")
        if self.minimum_age <= 0 or self.maximum_age < self.minimum_age:
            raise ValueError("Invalid age criteria.")
        if self.credit_score_required < 0:
            raise ValueError("Credit score requirement cannot be negative.")

    def check_eligibility(self, user_data: User, loan_amount: float) -> bool:
        if not user_data or not isinstance(user_data, User):
            return False
        if not isinstance(loan_amount, (int, float)) or loan_amount <= 0:
            return False

        minimum_income = math.ceil(loan_amount / 60) 
        if (
            self.minimum_age <= int(user_data.age) <= self.maximum_age 
            and 
            float(user_data.income) >= float(minimum_income)  
            and 
            self.credit_score_required <= int(user_data.credit_score) 
            and 
            (
                (self.employment_required and bool(user_data.employed)) or (not self.employment_required)
            )
        ): 
            return True  
        return False 

    def display_eligibility(self, loan_amount: float) -> None:
        if not isinstance(loan_amount, (int, float)) or loan_amount <= 0:
            raise ValueError("Loan amount must be greater than zero.")

        minimum_income = math.ceil(loan_amount / 60)

        print(f"\nEligibility Criteria for {self.service_name}")
        print("-" * 45)
        print(f"{'Minimum Age':<25}: {self.minimum_age}")
        print(f"{'Maximum Age':<25}: {self.maximum_age}")
        print(f"{'Minimum Income':<25}: ₹{minimum_income:,.2f}")
        print(f"{'Employment Required':<25}: {'Yes' if self.employment_required else 'No'}")
        print(f"{'Minimum Credit Score':<25}: {self.credit_score_required}")
        print(f"{'Interest Rate':<25}: {self.interest_rate}%")
        print(f"{'Duration':<25}: {self.duration_months} months")
        print("-" * 45)