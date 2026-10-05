from dataclasses import dataclass 
from Modules.models.User import User 
import math 

# id,service_name,description,fee,interest_rate,duration_months,minimum_age,maximum_age,
# minimum_income,employment_required,credit_score_required

@dataclass
class LoanService:
    id: int
    service_name: str 
    interest_rate: float
    duration_months: int
    minimum_age : int 
    maximum_age : int 
    employment_required : bool 
    credit_score_required : int 

    def check_eligibility(self , user_data:User , loan_amount:float) -> bool  : 
        
        minimum_income = math.ceil(loan_amount / 60) 
        if (
            self.minimum_age <= int(user_data.age) <= self.maximum_age 
            and 
            float(user_data.income) >= float(minimum_income)  
            and 
            self.credit_score_required <= int(user_data.credit_score) 
            and 
            (
            (self.employment_required and user_data.employed ) or (not self.employment_required)
            )
        ) : 
            return True  
    
        else : 
            return False 


    def display_eligibility(self, loan_amount: float) -> None:

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