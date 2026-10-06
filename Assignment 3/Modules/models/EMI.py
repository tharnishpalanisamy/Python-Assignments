from dataclasses import dataclass
from typing import Union
from datetime import datetime

@dataclass
class EMI:
    payment_id: int 
    loan_id: int 
    user_id: int 
    loan_type: str 
    loan_amount: float 
    date: Union[datetime, str]

    def __post_init__(self):
        try:
            self.payment_id = int(self.payment_id)
            self.loan_id = int(self.loan_id)
            self.user_id = int(self.user_id)
            self.loan_amount = float(self.loan_amount)
        except (ValueError, TypeError):
            raise ValueError("Invalid numeric values for EMI payment.")

        if self.payment_id <= 0:
            raise ValueError("Payment ID must be positive.")
        if self.loan_id <= 0:
            raise ValueError("Loan ID must be positive.")
        if self.user_id <= 0:
            raise ValueError("User ID must be positive.")
        if self.loan_amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")

    def display_emi_report(self): 
        print('EMI Payment Report : ')
        print(
            f'Loan Id   : {self.loan_id}\n' 
            f'Loan Type : {self.loan_type}\n'
            f'Amount    : {self.loan_amount}\n'
            f'Date      : {self.date}\n'
        )