from Modules.models.UserLoan import UserLoan 
from Modules.models.EMI import EMI 
from datetime import datetime 

class LoanPaymentService:
    def __init__(self) :
        pass 

    def validate_payment(self , amount , emi ) -> bool :
        if amount <= 0 :
            print('Amount cannot be Zero or negative') 
            return False 
        elif amount < emi :
            print('Amount cannot be lesser than emi ')  
            return False 
        return True 

    def process_payment(self , loan_data:UserLoan , amount:float ) -> bool : 
        print(f'Sucessfully paid {amount} as EMI')
        payment = EMI(
            loan_id=loan_data.loan_id , 
            loan_type=loan_data.loan_type , 
            amount=amount , 
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        loan_data.payment_history.append(payment)
        loan_data.duration_months -= 1 

        balance = amount - loan_data.emi 
        payment.display_emi_report() 
        
        if loan_data.duration_months <= 0 :
            print(f'Congradulations you have Completed your {loan_data.loan_type}') 
            return True 
        elif balance > 0 :

            print(f"You have paid an additional amount of {balance} with your emi that will directly reduce the principal") 
            loan_data.loan_amount -= balance 

            if loan_data.loan_amount == 0 :
                print(f'Congradulations you have Completed your {loan_data.loan_type}') 
                loan_data.status = 'closed'
                return True 
            
            elif loan_data.loan_amount < 0 :
                loan_data.status = 'closed'
                print(f'Congradulations you have Completed your {loan_data.loan_type}')
                print(f'You have additionally paid {abs(loan_data.loan_amount)} , the additioanlly amount will be refunded within 7 days ') 
                return True 
            
        


