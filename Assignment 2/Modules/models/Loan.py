from dataclasses import dataclass 

@dataclass
class Loan:
    id: int
    service_name: str
    interest_rate: float
    duration_months: int
    eligibility: dict



