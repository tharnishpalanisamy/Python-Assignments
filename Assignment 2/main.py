import json
from pathlib import Path 
from utilities import process_loan  , calculate_monthly_emi , check_user_exists , process_insurance 
import math

path = Path('./data/data.json')

user_path = Path('./data/enrolled.json') 
with path.open('r') as file :
    data:list[dict] = json.load(file) 
    file.close() 



print(type(data))

print('Welcome to Our Program ! ')  

while True : 
    try : 
        user_choice : int = int(input(
            f"1 , for Loan services  \n" 
            f"2 , for Insurance services \n" 
            f"3 , for card services \n" 
            f"0 , to exit :  \n"  

        ))  
        if user_choice not in (0,1,2,3) :
            raise ValueError
    except ValueError :
        print('Please enter a valid choice ') 
        continue 


    match user_choice : 
        case 0 : 
            print('Thanks for using our service ! ') 
            break 
        case 1 : 
            print('You have choosen Loan Services') 

            try: 
                loan_choice = int(input(
                                    f"1 , for Personal Loan  \n" 
                                    f"2 , for Home Loan \n" 
                                    f"3 , for Car Loan \n" 
                                    f"4 , for Educational Loan\n" 
                                    f"0 , to Exit : \n"   
                                ))  
                vals = [1,2,3,4] 

                if loan_choice == 0 :
                    print('Thanks for using our service ! ') 
                    break 

                if loan_choice not in vals :
                    raise ValueError
            except ValueError :
                    print('Please enter a valid choice ')   
                    continue 

            else:
                print('Please enter the following details ' ) 

                try:
                    id : int = int(input('Enter your unique Id : ')) 
                    name : str = input('Enter your Name : ' )  
                    age : int = int(input('Enter your age : '))  
                    employed : int = int(input('Enter 1 for employed , 0 for otherwsie : ') ) 
                    income:float = float(input('Enter your Income : '))  
                    loan_amount:float = float(input('Enter the amount you a=want to borrow : '))
                    credit_score : int = int(input('Enter your Credit Score : '))  
                    loan_data = data[loan_choice-1] 
                except ValueError :
                    print("You have entered Invalid value , Please try again !") 

                else : 
                    user_data : dict = { 
                        'id' : id , 
                        'name' : name , 
                        'age' : age , 
                        'employed' : employed , 
                        'income' : income , 
                        'credit_score' : credit_score  ,
                        'loan_amount' : loan_amount
                    }
                    eligible = process_loan(
                        loan_type = loan_choice , 
                        user_data = user_data , 
                        loan_data = loan_data 
                        )

                    if not eligible :
                        print('You are not eligible for the loan !') 
                        break 

                    print('You are eligble for the Loan , The Loan Details are below ')



                    emi = math.ceil(calculate_monthly_emi(
                                loan_amount ,loan_data['interest_rate'] , loan_data['duration_months'] 
                            ))
                    emi_name = loan_data['service_name']
                    if(eligible ) :
                        print(
                            f"Interest Rate : {loan_data['interest_rate']}% \n" 
                            f"Total Loan Amount : ${loan_amount : .2f}\n"  
                            f"Total tenure : {loan_data['duration_months']} months\n"
                            f"Your Monthly Emi Would be {emi:.2f}\n"
                        )
                        try : 
                            take_loan = int(input('1 - to continue , 0 - to stop : ')) 

                            if take_loan not in (0 , 1) :
                                raise ValueError 
                            
                            if take_loan == 1:
                                with user_path.open('r') as file:
                                    users = json.load(file)

                                user = None
                                position = None

                                for i, item in enumerate(users):
                                    if item['id'] == id:
                                        user = item
                                        position = i
                                        break

                                if user is None:
                                    user = {
                                        'id': id,
                                        'name': name,
                                        'age': age,
                                        'income': income,
                                        'employed': employed,
                                        'history': [
                                            f"Took a ${loan_amount} {loan_data['service_name']} "
                                            f"with a duration of {loan_data['duration_months']} months"
                                        ],
                                        'services': [
                                            loan_data['service_name']
                                        ],
                                        'emi_history': {
                                            emi_name: [emi]
                                        }
                                    }
                                    users.append(user)

                                else:
                                    user['history'].append(
                                        f"Took a ${loan_amount} {loan_data['service_name']} "
                                        f"with a duration of {loan_data['duration_months']} months"
                                    )

                                    user['services'].append(
                                        loan_data['service_name']
                                    )

                                    if loan_data['service_name'] not in user['emi_history']:
                                        user['emi_history'][loan_data['service_name']] = [emi]
                                    else:
                                        user['emi_history'][loan_data['service_name']].append(emi)

                                with user_path.open('w') as file:
                                    json.dump(users, file, indent=4)
                        except ValueError :
                            print('Your have choosen an invalid choice please try again ! ') 
                            continue 


        case 2 : 
            print('You have choosen Insurance Services') 
            
            try: 
                insurance_choice = int(input(
                                    f"1 , Health Insurance  \n" 
                                    f"2 , Life Insurance \n" 
                                    f"0 , to Exit : \n"   
                                ))   
                if insurance_choice == 0 :
                    print('Thanks for using our service !') 
                    break 

                if insurance_choice not in (1,2) :
                    raise ValueError  
                

            except ValueError :
                print('You have selected an invalid choice please try again !') 
                continue 

            else : 
                print('Please enter the following details ' ) 

                try:
                    id : int = int(input('Enter your unique Id : ')) 
                    name : str = input('Enter your Name : ' )  
                    age : int = int(input('Enter your age : '))  
                    employed : int = int(input('Enter 1 for employed , 0 for otherwsie : ') ) 
                    income:float = float(input('Enter your Income : '))  
                    cover_amount:float = float(input('Enter the amount you a=want to borrow : '))


                    insurance_data = data[insurance_choice + 3 ] 

                    

                except ValueError :
                    print('You have selected an invalid choice please try again !') 
                    continue 
                