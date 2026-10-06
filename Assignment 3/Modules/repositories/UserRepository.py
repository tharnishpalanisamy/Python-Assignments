from config import USER_PATH 
import csv 
from Modules.models.User import User  
from dataclasses import asdict 
from Modules.utilities import validate_email, USER_FIELDS
from Modules.Exception.exception import UserNotFoundException, InvalidEmailException
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
        except (IOError, OSError) as error:
            print(f"Error reading users file: {error}")
            return []

    def create_user(self, user_id: int) -> User:
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("User ID must be a positive integer.")

        print('You are a new User !') 
        name = input("Enter your name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        email = input("Enter your email: ").strip()
        if not validate_email(email=email):
            raise InvalidEmailException(f"The email id '{email}' is not valid.")

        try:
            age = int(input("Enter your age: ").strip())
        except ValueError:
            raise ValueError("Age must be a valid integer.")
        if age <= 0 or age > 120:
            raise ValueError("Age must be between 1 and 120.")

        employed_input = input("Are you employed? (1/0): ").strip()
        if employed_input not in ['0', '1']:
            raise ValueError("Employment status must be 1 (Yes) or 0 (No).")
        employed = int(employed_input)

        try:
            income = float(input("Enter your income: ").strip())
        except ValueError:
            raise ValueError("Income must be a valid number.")
        if income < 0:
            raise ValueError("Income cannot be negative.")

        try:
            credit_score = int(input("Enter your credit score: ").strip())
        except ValueError:
            raise ValueError("Credit score must be a valid integer.")
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

    def find(self, user_id: int) -> User:
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("User ID must be a positive integer.")

        all_users = self.get_all()
        for user in all_users:
            if not user or not user.get("id"):
                continue
            try:
                curr_id = int(user["id"])
            except (ValueError, TypeError):
                continue

            if curr_id == user_id:
                raw_employed = str(user.get("employed", "0")).strip().lower()
                employed = 1 if raw_employed in ("true", "1", "yes") else 0
                return User(
                    id=curr_id,
                    name=user["name"],
                    age=int(user["age"]),
                    email=user["email"],
                    employed=employed,
                    income=float(user["income"]),
                    credit_score=int(float(user["credit_score"])),
                )

        raise UserNotFoundException(f"User not found corresponding to the id {user_id}")
    
    def save_user(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError("Expected User instance.")
        try:
            file_exists = self.user_path.exists() and self.user_path.stat().st_size > 0
            with self.user_path.open('a', newline="") as file: 
                writer = csv.DictWriter(file, fieldnames=USER_FIELDS) 
                if not file_exists:
                    writer.writeheader()
                writer.writerow(asdict(user)) 
        except (IOError, OSError) as error:
            print(f"Error saving user: {error}")

    def update_user(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError("Expected User instance.")
        all_users = self.get_all()
        found = False
        for index, current_user in enumerate(all_users):
            try:
                if int(current_user['id']) == user.id:
                    all_users[index] = asdict(user)
                    found = True
                    break
            except (ValueError, KeyError):
                continue

        if not found:
            raise UserNotFoundException(f"User with ID {user.id} not found to update.")

        try:
            with self.user_path.open('w', newline="") as file: 
                writer = csv.DictWriter(file, fieldnames=USER_FIELDS)
                writer.writeheader()
                writer.writerows(all_users)
        except (IOError, OSError) as error:
            print(f"Error updating user: {error}")
