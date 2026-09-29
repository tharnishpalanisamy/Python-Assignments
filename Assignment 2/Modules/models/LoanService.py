from dataclasses import dataclass 
from Modules.models.User import User 
import math 

@dataclass
class LoanService:
    id: int
    service_name: str 
    interest_rate: float
    duration_months: int
    eligibility: dict

    def check_eligibility(self , user_data:User , loan_amount:float) -> bool  : 
    
        minimum_income = f"{math.ceil(loan_amount / 60 ) : .2f}"
        if (
            self.eligibility['minimum_age'] <= user_data.age <= self.eligibility['maximum_age'] 
            and 
            float(user_data.income) >= float(minimum_income)  
            and 
            self.eligibility['credit_score_required'] <= user_data.credit_score 
            and 
            (
            (self.eligibility['employment_required'] and user_data.employed ) or (not self.eligibility['employment_required'])
            )
        ) : 
            return True  
    
        else : 
            return False 


    def display_eligibility(self, loan_amount:float ) ->None : 
    
        print(f'Eligibility Criteria for {self.service_name} is Below : ') 
        eligibility:dict = self.eligibility 
        minimum_income = f"{math.ceil(loan_amount / 60 ) : .2f}"
    
        for field , requirement in eligibility.items() :
            if field == 'minimum_income' : 
                print(f"{field:<15} : {minimum_income} ")
                continue
            print(f"{field:<15} : {requirement} ") 
        print('\n')