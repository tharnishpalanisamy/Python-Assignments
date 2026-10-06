from Modules.models.UserLoan import UserLoan 
from Modules.models.EMI import EMI 
from datetime import datetime 
from Modules.repositories.PaymentRepository import PaymentRepository 
from Modules.repositories.LoanRepository import LoanRepository 
from Modules.Exception.exception import LoanNotFoundException

class LoanPaymentService:
    def __init__(self):
        self.payment_repository = PaymentRepository()  
        self.loan_repository = LoanRepository() 

    def validate_payment(self, amount, emi) -> bool:
        try:
            amount = float(amount)
            emi = float(emi)
        except (ValueError, TypeError):
            print('Invalid payment or EMI amount.')
            return False

        if amount <= 0:
            print('Amount cannot be Zero or negative') 
            return False 
        elif amount < emi:
            print('Amount cannot be lesser than emi ')  
            return False 
        return True 

    def process_payment(
        self,
        loan_data: UserLoan,
        user_id: int,
        amount: float
    ) -> bool:
        if not isinstance(loan_data, UserLoan):
            raise TypeError("Expected UserLoan instance.")
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("User ID must be a positive integer.")
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            raise ValueError("Payment amount must be a valid number.")

        if not self.validate_payment(amount, loan_data.emi):
            raise ValueError("Payment validation failed.")

        if loan_data.status.lower() == 'closed':
            raise ValueError("Cannot make payments on an already closed loan.")

        all_payments = self.payment_repository.get_all()

        payment = EMI(
            payment_id=len(all_payments) + 1,
            loan_id=loan_data.loan_id,
            user_id=user_id,
            loan_type=loan_data.loan_type,
            loan_amount=amount,
            date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        self.payment_repository.add_payment(payment)

        all_loans = self.loan_repository.get_all()
        user_loan = None

        for loan in all_loans:
            try:
                if int(loan['loan_id']) == loan_data.loan_id:
                    user_loan = loan
                    break
            except (ValueError, KeyError):
                continue

        if user_loan is None:
            raise LoanNotFoundException(f"Loan with ID {loan_data.loan_id} not found.")

        balance = amount - float(loan_data.emi)

        current_duration = int(user_loan['duration_months']) - 1
        user_loan['duration_months'] = max(0, current_duration)

        if balance > 0:
            print(
                f"You have paid an additional amount of "
                f"{balance:.2f} with your EMI that will "
                f"directly reduce the principal"
            )
            new_amount = float(user_loan['loan_amount']) - balance
            user_loan['loan_amount'] = max(0.0, round(new_amount, 2))

        if int(user_loan['duration_months']) <= 0 or float(user_loan['loan_amount']) <= 0:
            user_loan['status'] = 'closed'
            print(
                f"Congratulations! You have completed "
                f"your {user_loan['loan_type']}"
            )

        self.loan_repository.update_loan(user_loan)
        print(f'Successfully paid {amount} as EMI')
        return True
