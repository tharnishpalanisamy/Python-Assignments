from dataclasses import dataclass 
from Modules.models.UserLoan import UserLoan

@dataclass
class User:
    id:int 
    name:str 
    email : str 
    age:int 
    employed:int 
    income:float 
    credit_score : int 
    # history : list 
    # services : list 
    # loans : list[UserLoan] 

    def display_loans(self) : 
        print('Your Active Loans are as follows : ') 
        for loan in self.loans : 
            if loan['status'] == 'active' : 
                print(
                    f"Loan ID : {loan['loan_id']} , Loan Type : {loan['loan_type']} , "
                    f"Loan Amount : {loan['loan_amount']} , EMI : {loan['emi']:.2f} , "
                    f"Interest Rate : {loan['interest_rate']} % , Duration : {loan['duration_months']} months "
                    ) 
     
        