from Modules.repositories.BaseRepository import BaseRepository 
from config import LOANS_PATH
from Modules.models.UserLoan import UserLoan
from Modules.utilities import LOANS_FIELD
from dataclasses import asdict 
import csv 




class LoanRepository(BaseRepository) : 
    def __init__(self) : 
        self.loans_path = LOANS_PATH 

    def get_all(self) :
        with self.loans_path.open('r' , newline="")  as file : 
            data = list(csv.DictReader(file))
            return data 

    def add_loan(self , loan:UserLoan ) :
        with self.loans_path.open('a' , newline="") as file :
            writer  = csv.DictWriter(file , fieldnames=LOANS_FIELD)
            writer.writerow(asdict(loan))

    def find(self , id:int) :
        all_loans = self.get_all() 
        


                         