from dataclasses import dataclass, asdict 
from Modules.models.EMI import EMI

@dataclass 
class UserLoan : 
    loan_id : int  
    user_id : int 
    loan_type : str 
    loan_amount : float 
    emi : float 
    interest_rate : float 
    duration_months : int 
    status : str 





