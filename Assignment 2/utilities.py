import math
import json
from pathlib import Path
def process_loan(loan_type:int , user_data:dict ,  loan_data:dict  ) -> bool :  

    print(f'Eligibility Criteria for {loan_data['service_name']} is Below : ') 

    eligibility:dict = loan_data['eligibility'] 
    for field , requirement in eligibility.items() :
        print(f"{field:<15} : {requirement} ")  

    minimum_income = f"{math.ceil(user_data['loan_amount'] / 60 ) : .2f}"

    if (
        eligibility['minimum_age'] <= user_data['age'] <= eligibility['maximum_age'] 
        and 
        float(user_data['income']) >= float(minimum_income)  
        and 
        eligibility['credit_score_required'] <= user_data['credit_score'] 
        and 
        (
        (eligibility['employment_required' ] and user_data['employed'] ) or (not eligibility['employment_required'])
        )
    ) : 
        return True 

    else : 
        return False 


    


def calculate_monthly_emi(principal, annual_interest_rate, duration_months):
    r = (annual_interest_rate / 12) / 100
    
    if r == 0:
        return principal / duration_months
        
    emi = (principal * r * (1 + r)**duration_months) / ((1 + r)**duration_months - 1)
    
    return emi





def check_user_exists(search_id: int) -> dict :
    path = Path('./data/enrolled.json')
    
    with path.open('r') as file:
        data: list[dict] = json.load(file)

    for user in data:
        if user.get("id") == search_id:
            return user  
            
    return None  




def process_insurance() -> bool : 
    return True 