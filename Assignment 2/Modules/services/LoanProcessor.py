from Modules.models.User import User 
from Modules.models.UserLoan import UserLoan 
from Modules.models.LoanService import LoanService
import math 
from Modules.models.EMI import EMI 

class LoanProcessor : 
    def __init__(self): 
        self.eligibility = False  

    def display_eligibility(self,loan_data:LoanService , user_data:User , loan_amount:float ) ->None : 

        print(f'Eligibility Criteria for {loan_data.service_name} is Below : ') 
        eligibility:dict = loan_data.eligibility 
        minimum_income = f"{math.ceil(loan_amount / 60 ) : .2f}"
    
        for field , requirement in eligibility.items() :
            if field == 'minimum_income' : 
                print(f"{field:<15} : {minimum_income} ")
                continue
            print(f"{field:<15} : {requirement} ") 
        print('\n')

    def check_eligibility(self , loan_data:LoanService , user_data:User , loan_amount:float) : 

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

    def approve_loan(self , loan_data:LoanService , user_data:User , loan_amount) -> bool  : 
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


    def find_loan(self ,user_data:User, loan_id:int  ) -> EMI | None :
        for loan in user_data.loans :
            if loan['loan_id'] == loan_id :
                return UserLoan(
                    loan_id = loan['loan_id'] ,
                    loan_type = loan['loan_type'] ,
                    loan_amount = loan['loan_amount'] ,
                    emi = loan['emi'] ,
                    interest_rate = loan['interest_rate'] ,
                    duration_months = loan['duration_months'] ,
                    status = loan['status'] ,
                    payment_history = loan['payment_history']
                )
        return None  


    def display_summary(self,loan_data , loan_amount , emi ) ->None :
        print('\nYou are eligible for this loan ! Further Details are as follows : ')  
        print(f"Loan Amount : {loan_amount} ")
        print(f"Interest Rate : {loan_data.interest_rate} % ")
        print(f"Duration : {loan_data.duration_months} months ")
        print(f"Monthly EMI : {emi:.2f} \n") 


