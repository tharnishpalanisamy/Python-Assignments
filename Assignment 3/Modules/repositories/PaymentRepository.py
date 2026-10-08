from Modules.repositories.BaseRepository import BaseRepository 
from Modules.utilities import PAYMENT_FIELD  
from config import PAYMENT_PATH 
import csv 
from Modules.models.EMI import EMI  
from dataclasses import asdict

class PaymentRepository(BaseRepository):
    def __init__(self):
        self.payment_path = PAYMENT_PATH 

    def get_all(self):
        if not self.payment_path.exists():
            return []
        try:
            with self.payment_path.open('r', newline="") as file:
                data = list(csv.DictReader(file))
                return [row for row in data if row.get('payment_id') and row.get('payment_id') != 'payment_id']
        except Exception as error:
            print(f"Error reading payment file: {error}")
            return []

    def add_payment(self, payment_data: EMI) -> bool:
        try:
            file_exists = self.payment_path.exists() and self.payment_path.stat().st_size > 0
            with self.payment_path.open('a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=PAYMENT_FIELD) 
                if not file_exists:
                    writer.writeheader() 
                writer.writerow(asdict(payment_data))
            return True
        except Exception as error:
            print(f"Error saving payment: {error}")
            return False