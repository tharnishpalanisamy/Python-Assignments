from Modules.models.User import User 
from Modules.models.UserLoan import UserLoan 
from Modules.models.LoanService import LoanService
from Modules.Exception.exception import LoanNotFoundException
class LoanProcessor : 
    def __init__(self): 
        self.eligibility = False  

    def calculate_emi(self , loan_amount:float , interest:float , duration:int) : 

        monthly_rate = (interest / 12) / 100
    
        if monthly_rate == 0:
            return loan_amount / duration
            
        # this si the Standard EMI Formula: [P x R x (1+R)^N] / [(1+R)^N - 1]
        numerator = loan_amount * monthly_rate * ((1 + monthly_rate) ** duration)
        denominator = ((1 + monthly_rate) ** duration) - 1
        
        emi = numerator / denominator
        return round(emi, 2)

    def approve_loan(self , loan_data:LoanService , user_data:User , loan_amount) -> bool  : 
        if not loan_data.check_eligibility(user_data , loan_amount) :
            return False 
        
        emi  = self.calculate_emi(loan_amount , loan_data.interest_rate , loan_data.duration_months)
        user_data.history.append(
            f'Applied for {loan_data.service_name} of amount {loan_amount} with EMI {emi} at interest rate {loan_data.interest_rate} % for '
            f'duration of {loan_data.duration_months} months.'
            )
        user_data.services.append(loan_data.service_name) 
        user_data.loans.append({
            'loan_id' : len(user_data.loans) + 1 ,  
            'loan_type' : loan_data.service_name , 
            'loan_amount' : loan_amount , 
            'emi' : emi  , 
            'interest_rate' : loan_data.interest_rate , 
            'duration_months' : loan_data.duration_months , 
            'status' : 'active' , 
            'payment_history' : [] 
 
        })

        return True 


    def find_loan(self ,user_data:User, loan_id:int  ) -> UserLoan :
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
        raise LoanNotFoundException('Loan with id : {loan_id} Not Found ! ') 


    def display_summary(self,loan_data , loan_amount , emi ) ->None :
        print('\nYou are eligible for this loan ! Further Details are as follows : ')  
        print(f"Loan Amount : {loan_amount} ")
        print(f"Interest Rate : {loan_data.interest_rate} % ")
        print(f"Duration : {loan_data.duration_months} months ")
        print(f"Monthly EMI : {emi:.2f} \n") 

    def display_selected_loan(self , loan_data):
        print(f'You have selected Loan ID : {loan_data.loan_id} ,'
            f'Loan Type : {loan_data.loan_type} , Loan Amount : {loan_data.loan_amount} , \n'
            f'EMI : {loan_data.emi:.2f} , Interest Rate : {loan_data.interest_rate} % , '
            f'Duration : {loan_data.duration_months} months' )


