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
        self.loan_id = int(self.loan_id)
        self.user_id = int(self.user_id)
        self.loan_amount = float(self.loan_amount)
        self.emi = float(self.emi)
        self.interest_rate = float(self.interest_rate)
        self.duration_months = int(self.duration_months)

        if self.loan_amount < 0 or self.emi < 0 or self.interest_rate < 0 or self.duration_months < 0:
            raise ValueError("Loan amounts and durations cannot be negative.")
        if str(self.status).lower() not in ("active", "closed"):
            raise ValueError("Status must be 'active' or 'closed'.")
