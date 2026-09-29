from dataclasses import dataclass 

@dataclass
class LoanService:
    id: int
    service_name: str 
    interest_rate: float
    duration_months: int
    eligibility: dict


