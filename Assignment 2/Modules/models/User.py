from dataclasses import dataclass 

@dataclass
class User:
    id:int 
    name:str 
    email : str 
    age:int 
    employed:int 
    income:float 
    credit_score : int 
    history : list 
    services : list 
    loans : list 


    
        