from dataclasses import dataclass

@dataclass 
class UserLoan: 
    loan_id: int  
    user_id: int 
    loan_type: str 
    loan_amount: float 
    emi: float 
    interest_rate: float 
    duration_months: int 
    status: str 

    def __post_init__(self):
        try:
            self.loan_id = int(self.loan_id)
            self.user_id = int(self.user_id)
            self.loan_amount = float(self.loan_amount)
            self.emi = float(self.emi)
            self.interest_rate = float(self.interest_rate)
            self.duration_months = int(self.duration_months)
        except (ValueError, TypeError):
            raise ValueError("Invalid numeric values for UserLoan.")

        if self.loan_id <= 0:
            raise ValueError("Loan ID must be a positive integer.")
        if self.user_id <= 0:
            raise ValueError("User ID must be a positive integer.")
        if self.loan_amount < 0:
            raise ValueError("Loan amount cannot be negative.")
        if self.emi < 0:
            raise ValueError("EMI cannot be negative.")
        if self.interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if self.duration_months < 0:
            raise ValueError("Duration cannot be negative.")
        if str(self.status).lower() not in ("active", "closed"):
            raise ValueError("Status must be 'active' or 'closed'.")
