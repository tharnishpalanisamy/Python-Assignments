from config import USER_PATH 
import csv 
from Modules.models.User import User  
from dataclasses import asdict 
from Modules.utilities import validate_email, USER_FIELDS
from Modules.repositories.BaseRepository import BaseRepository 

class UserRepository(BaseRepository):
    def __init__(self):
        self.user_path = USER_PATH  

    def get_all(self):
        if not self.user_path.exists():
            return []
        try:
            with self.user_path.open('r', newline="") as file: 
                reader = csv.DictReader(file)
                return [row for row in reader if row.get("id")]
        except Exception as error:
            print(f"Error reading users file: {error}")
            return []

    def create_user(self, user_id: int) -> User:
        print('You are a new User !') 
        name = input("Enter your name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        email = input("Enter your email: ").strip()
        if not validate_email(email=email):
            raise ValueError(f"The email id '{email}' is not valid.")

        age = int(input("Enter your age: ").strip())
        if age <= 0 or age > 120:
            raise ValueError("Age must be between 1 and 120.")

        employed_input = input("Are you employed? (1/0): ").strip()
        if employed_input not in ['0', '1']:
            raise ValueError("Employment status must be 1 (Yes) or 0 (No).")
        employed = int(employed_input)

        income = float(input("Enter your income: ").strip())
        if income < 0:
            raise ValueError("Income cannot be negative.")

        credit_score = int(input("Enter your credit score: ").strip())
        if credit_score < 0:
            raise ValueError("Credit score cannot be negative.")

        return User(
            id=user_id,
            name=name,
            email=email,
            age=age,
            employed=employed,
            income=income,
            credit_score=credit_score,
        )

    def find(self, user_id: int) -> User | None:
        all_users = self.get_all()
        for user in all_users:
            if user.get("id") and int(user["id"]) == user_id:
                raw_employed = str(user.get("employed", "0")).strip().lower()
                employed = 1 if raw_employed in ("true", "1", "yes") else 0
                return User(
                    id=int(user["id"]),
                    name=user["name"],
                    age=int(user["age"]),
                    email=user["email"],
                    employed=employed,
                    income=float(user["income"]),
                    credit_score=int(float(user["credit_score"])),
                )
        return None
    
    def save_user(self, user: User) -> None:
        try:
            file_exists = self.user_path.exists() and self.user_path.stat().st_size > 0
            with self.user_path.open('a', newline="") as file: 
                writer = csv.DictWriter(file, fieldnames=USER_FIELDS) 
                if not file_exists:
                    writer.writeheader()
                writer.writerow(asdict(user)) 
        except Exception as error:
            print(f"Error saving user: {error}")

    def update_user(self, user: User) -> None:
        all_users = self.get_all()
        found = False
        for index, current_user in enumerate(all_users):
            if int(current_user.get('id', -1)) == user.id:
                all_users[index] = asdict(user)
                found = True
                break

        if not found:
            raise ValueError(f"User with ID {user.id} not found to update.")

        try:
            with self.user_path.open('w', newline="") as file: 
                writer = csv.DictWriter(file, fieldnames=USER_FIELDS)
                writer.writeheader()
                writer.writerows(all_users)
        except Exception as error:
            print(f"Error updating user: {error}")
