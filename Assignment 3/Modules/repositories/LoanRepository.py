from Modules.repositories.BaseRepository import BaseRepository 
from config import LOANS_PATH
from Modules.models.UserLoan import UserLoan
from Modules.utilities import LOANS_FIELD
from dataclasses import asdict 
import csv 
from Modules.Exception.exception import LoanNotFoundException 

class LoanRepository(BaseRepository): 
    def __init__(self): 
        self.loans_path = LOANS_PATH 

    def get_all(self):
        if not self.loans_path.exists():
            return []
        try:
            with self.loans_path.open('r', newline="") as file: 
                data = list(csv.DictReader(file))
                return [row for row in data if row.get('loan_id')]
        except (IOError, OSError) as error:
            print(f"Error reading loans file: {error}")
            return []

    def add_loan(self, loan: UserLoan):
        if not isinstance(loan, UserLoan):
            raise TypeError("Expected UserLoan instance.")
        try:
            file_exists = self.loans_path.exists() and self.loans_path.stat().st_size > 0
            with self.loans_path.open('a', newline="") as file:
                writer = csv.DictWriter(file, fieldnames=LOANS_FIELD)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(asdict(loan))
        except (IOError, OSError) as error:
            print(f"Error adding loan: {error}")

    def find(self, id: int):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("Loan ID must be a positive integer.")
        all_loans = self.get_all()

        for loan in all_loans:
            try:
                if int(loan['loan_id']) == id:
                    return loan
            except (ValueError, KeyError):
                continue

        raise LoanNotFoundException(
            f"Loan with ID {id} was not found."
        )

    def update_loan(self, updated_loan: dict):
        if not isinstance(updated_loan, dict) or 'loan_id' not in updated_loan:
            raise ValueError("Invalid loan data provided for update.")

        all_loans = self.get_all()
        found = False

        for loan in all_loans:
            try:
                if int(loan['loan_id']) == int(updated_loan['loan_id']):
                    loan.update(updated_loan)
                    found = True
                    break
            except (ValueError, KeyError):
                continue

        if not found:
            raise LoanNotFoundException(
                f"Loan with ID {updated_loan.get('loan_id')} not found to update."
            )

        try:
            with self.loans_path.open('w', newline='') as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=LOANS_FIELD
                )
                writer.writeheader()
                writer.writerows(all_loans)
        except (IOError, OSError) as error:
            print(f"Error updating loan: {error}")