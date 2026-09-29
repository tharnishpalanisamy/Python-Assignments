from dataclasses import dataclass
from datetime import datetime
@dataclass

class EMI :
    loan_id : int 
    loan_type : str 
    amount : float 
    date : datetime   

    def display_emi_report(self): 
        print('EMI Payment Report : ')
        print(
            f'Loan Id   : {self.loan_id}' 
            f'Loan Type : {self.loan_type}'
            f'Amount    : {self.amount}'
            f'Date      : {self.date}'
        )



    