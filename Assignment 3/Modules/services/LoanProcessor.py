from Modules.models.User import User 
from Modules.models.UserLoan import UserLoan 
from Modules.models.LoanService import LoanService
from Modules.Exception.exception import LoanNotFoundException  
from Modules.repositories.LoanRepository import LoanRepository 

class LoanProcessor: 
    def __init__(self): 
        self.eligibility = False  
        self.loan_repository = LoanRepository() 

    def calculate_emi(self, loan_amount: float, interest: float, duration: int) -> float: 
        if not isinstance(loan_amount, (int, float)) or loan_amount <= 0:
            raise ValueError("Loan amount must be a positive number.")
        if not isinstance(interest, (int, float)) or interest < 0:
            raise ValueError("Interest rate cannot be negative.")
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Duration must be a positive integer.")

        monthly_rate = (interest / 12) / 100
    
        if monthly_rate == 0:
            return round(loan_amount / duration, 2)
            
        numerator = loan_amount * monthly_rate * ((1 + monthly_rate) ** duration)
        denominator = ((1 + monthly_rate) ** duration) - 1
        
        emi = numerator / denominator
        return round(emi, 2)

    def approve_loan(self, loan_data: LoanService, user_data: User, loan_amount: float) -> bool: 
        if not isinstance(loan_data, LoanService):
            raise TypeError("Invalid loan data provided.")
        if not isinstance(user_data, User):
            raise TypeError("Invalid user data provided.")
        if not isinstance(loan_amount, (int, float)) or loan_amount <= 0:
            raise ValueError("Loan amount must be a positive number.")

        if not loan_data.check_eligibility(user_data, loan_amount):
            return False 
        
        emi = self.calculate_emi(loan_amount, loan_data.interest_rate, loan_data.duration_months)

        all_loans = self.loan_repository.get_all() 
        loan = UserLoan(
            loan_id=len(all_loans) + 1,  
            user_id=user_data.id,
            loan_type=loan_data.service_name, 
            loan_amount=float(loan_amount), 
            emi=emi, 
            interest_rate=loan_data.interest_rate, 
            duration_months=loan_data.duration_months, 
            status='active' 
        )
        self.loan_repository.add_loan(loan)
        return True 

    def find_loan(self, loan_id: int, user_data: User) -> UserLoan:
        if not isinstance(loan_id, int) or loan_id <= 0:
            raise ValueError("Loan ID must be a positive integer.")
        if not user_data or not isinstance(user_data, User):
            raise ValueError("Valid user data is required.")

        all_loans = self.loan_repository.get_all()

        for loan in all_loans:
            try:
                curr_loan_id = int(loan['loan_id'])
                curr_user_id = int(loan['user_id'])
            except (ValueError, KeyError):
                continue

            if curr_loan_id == loan_id and curr_user_id == user_data.id:
                return UserLoan(
                    loan_id=curr_loan_id,
                    user_id=curr_user_id,
                    loan_type=loan['loan_type'],
                    loan_amount=float(loan['loan_amount']),
                    emi=float(loan['emi']),
                    interest_rate=float(loan['interest_rate']),
                    duration_months=int(loan['duration_months']),
                    status=loan['status']
                )

        raise LoanNotFoundException(f"Loan with ID {loan_id} was not found for this user.")

    def display_user_loans(self, user_id: int) -> bool:
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("User ID must be a positive integer.")

        all_loans = self.loan_repository.get_all() 
        user_loans = []
        for loan in all_loans:
            try:
                if int(loan.get("user_id", -1)) == user_id:
                    user_loans.append(loan)
            except (ValueError, TypeError):
                continue

        if not user_loans:
            print('You have no active loans !')
            return False

        print('Your Active Loans are as follows : ') 
        for loan in user_loans: 
            print(
                f"---------------------------------------------------\n"
                f"Loan Id       : {loan['loan_id']}\n"
                f"Loan Type     : {loan['loan_type']}\n"
                f"Loan Amount   : {float(loan['loan_amount']):.2f}\n"
                f"EMI           : {float(loan['emi']):.2f}\n"
                f"Interest Rate : {loan['interest_rate']} %\n"
                f"Duration      : {loan['duration_months']} months\n"
                f"Status        : {loan.get('status', 'active')}\n"
                f"---------------------------------------------------"
            )
        return True
                
    def display_summary(self, loan_data: LoanService, loan_amount: float, emi: float) -> None:
        if not isinstance(loan_data, LoanService):
            raise TypeError("Invalid loan data provided.")
        if not isinstance(loan_amount, (int, float)) or loan_amount <= 0:
            raise ValueError("Loan amount must be a positive number.")
        if not isinstance(emi, (int, float)) or emi <= 0:
            raise ValueError("EMI must be a positive number.")

        print('\nYou are eligible for this loan ! Further Details are as follows : ')  
        print(f"Loan Amount   : {loan_amount:,.2f} ")
        print(f"Interest Rate : {loan_data.interest_rate} % ")
        print(f"Duration      : {loan_data.duration_months} months ")
        print(f"Monthly EMI   : {emi:.2f} \n") 

    def display_selected_loan(self, loan_data: UserLoan) -> None:
        if not isinstance(loan_data, UserLoan):
            raise TypeError("Expected UserLoan instance.")

        print(f'\nYou have selected Loan ID : {loan_data.loan_id}\n'
            f'Loan Type     : {loan_data.loan_type}\n'
            f'Loan Amount   : {loan_data.loan_amount:,.2f}\n'
            f'EMI           : {loan_data.emi:.2f}\n'
            f'Interest Rate : {loan_data.interest_rate} %\n'
            f'Duration      : {loan_data.duration_months} months\n'
            f'Status        : {loan_data.status}\n')
