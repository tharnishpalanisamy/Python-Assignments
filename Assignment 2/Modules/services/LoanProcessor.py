from Modules.models.User import User 
from Modules.models.Loan import Loan 
import math 

class LoanProcessor : 
    def __init__(self): 
        self.eligibility = False  



    def display_eligibility(self,loan_data:Loan , user_data:User , loan_amount:float ) ->None : 

        print(f'Eligibility Criteria for {loan_data.service_name} is Below : ') 
        eligibility:dict = loan_data.eligibility 
        minimum_income = f"{math.ceil(loan_amount / 60 ) : .2f}"
    
        for field , requirement in eligibility.items() :
            if field == 'minimum_income' : 
                print(f"{field:<15} : {minimum_income} ")
                continue
            print(f"{field:<15} : {requirement} ") 
        print('\n')

    def check_eligibility(self , loan_data:Loan , user_data:User , loan_amount:float) : 

        eligibility:dict = loan_data.eligibility 
        minimum_income = f"{math.ceil(loan_amount / 60 ) : .2f}"
        if (
            eligibility['minimum_age'] <= user_data.age <= eligibility['maximum_age'] 
            and 
            float(user_data.income) >= float(minimum_income)  
            and 
            eligibility['credit_score_required'] <= user_data.credit_score 
            and 
            (
            (eligibility['employment_required'] and user_data.employed ) or (not eligibility['employment_required'])
            )
        ) : 
            return True  
    
        else : 
            return False   


    def calculate_emi(self , loan_amount:float , interest:float , duration:int) : 

        monthly_rate = (interest / 12) / 100
    
        if monthly_rate == 0:
            return loan_amount / duration
            
        # Standard EMI Formula: [P x R x (1+R)^N] / [(1+R)^N - 1]
        numerator = loan_amount * monthly_rate * ((1 + monthly_rate) ** duration)
        denominator = ((1 + monthly_rate) ** duration) - 1
        
        emi = numerator / denominator
        return round(emi, 2)

    def approve_loan(self , loan_data:Loan , user_data:User , loan_amount) -> bool  : 
        if not self.check_eligibility(loan_data , user_data , loan_amount) :
            return False 
        
        EMI  = self.calculate_emi(loan_amount , loan_data.interest_rate , loan_data.duration_months)
        user_data.history.append(
            f'Applied for {loan_data.service_name} of amount {loan_amount} with EMI {EMI} at interest rate {loan_data.interest_rate} % for '
            f'duration of {loan_data.duration_months} months.'
            )
        user_data.services.append(loan_data.service_name) 
        user_data.loans.append({
            'loan_id' : len(user_data.loans) + 1 ,  
            'loan_type' : loan_data.service_name , 
            'loan_amount' : loan_amount , 
            'emi' : EMI  , 
            'interest_rate' : loan_data.interest_rate , 
            'duration_months' : loan_data.duration_months , 
            'status' : 'active' , 
            'payment_history' : [] 
 
        })

        return True 



