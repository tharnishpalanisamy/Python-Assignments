from config import USER_PATH  
import json 
from Modules.models.User import User  
from dataclasses import asdict 
from Modules.utilities import validate_email
from Modules.Exception.exception import UserNotFoundException , InvalidEmailException
from Modules.repositories.BaseRepository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self) :
        self.user_path = USER_PATH 

    def get_all(self) :

        with self.user_path.open('r') as file : 
            data = json.load(file)
            return data 

    def create_user(self, user_id: int) -> User  :
        print('You are a new User !') 
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        age = int(input("Enter your age: "))
        employed = input("Are you employed? (1/0): ")
        income = float(input("Enter your income: "))
        credit_score = int(input("Enter your credit score: "))
        if validate_email(email=email) : 
            return User(
                id=user_id,
                name=name,
                email=email,
                age=age,
                employed=employed,
                income=income,
                credit_score=credit_score,
                history=[],
                services=[],
                loans=[]
            ) 
        else:
            raise InvalidEmailException(f'The email id {email} is not valid ')

    
    def find(self, user_id: int) -> User :

        all_users = self.get_all()
        for user in all_users:
            if user["id"] == user_id:
                return User(
                    id=user["id"],
                    name=user["name"],
                    age=user["age"],
                    email=user["email"],
                    employed=user["employed"],
                    income=user["income"],
                    credit_score=user["credit_score"],
                    history=user["history"],
                    services=user["services"],
                    loans=user["loans"]
                )

        raise UserNotFoundException(f"User not found corresponding to the id {user_id}")
    
    def save_user(self , user : User ) -> None :
        all_users = self.get_all() 
        all_users.append(asdict(user))  

        with self.user_path.open('w' ) as file  : 
            json.dump(all_users , file , indent=4) 

    def update_user(self, user: User) -> None:
        all_users = self.get_all()

        for index, current_user in enumerate(all_users):
            if current_user['id'] == user.id:
                all_users[index] = asdict(user)
                break

        with self.user_path.open('w') as file:
            json.dump(all_users, file, indent=4)
