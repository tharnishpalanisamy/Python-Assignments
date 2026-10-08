from Modules.repositories.LoanRepository import LoanRepository

try:
    l = LoanRepository() 
    print(l.find(1))
except ValueError as e:
    print(f"Loan not found / invalid: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")