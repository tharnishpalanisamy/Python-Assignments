from Modules.repositories.LoanRepository import LoanRepository
from Modules.Exception.exception import LoanNotFoundException

try:
    l = LoanRepository() 
    print(l.find(1))
except LoanNotFoundException as e:
    print(f"Loan not found: {e}")
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")