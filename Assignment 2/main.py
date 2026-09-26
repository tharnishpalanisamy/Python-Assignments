from pathlib import Path 
import json
from Modules.utilities import calculate_monthly_premium, process_insurance, process_loan, calculate_monthly_emi 
from datetime import datetime 
from config import USER_PATH , SERVICE_PATH


with SERVICE_PATH.open('r') as file:
    service_data: list[dict] = json.load(file)


print('Welcome To our System !') 

while True: 
    print('Please select the service you want to use : ') 
    user_input:int = int(input(
        f"1 , for Loan Services \n" 
        f"2 , for Insurance Services \n" 
        f"0 , to Exit : \n"
        )
    ) 

    match user_input : 
        case 0 : 
            print('Thank you for using our system !') 
            break 

        case 1 : 
            
            print('You have selected Loan Services !') 
            try : 
                loan_input:int = int(input(
                    f"1 , for Personal Loan \n" 
                    f"2 , for Home Loan \n" 
                    f"3 , for Car Loan \n"
                    f"4 , for Education Loan \n"
                    f"5 , to pay EMI \n"
                    f"0 , to Exit : \n"
                )) 
                 
                if loan_input == 0 : 
                    print('Thank you for using our system !') 
                    break 

                

                if loan_input not in [1, 2, 3, 4, 5] :
                    raise ValueError('Invalid input, please try again !') 


                
                if loan_input in [1,2,3,4] :
                    loan_data = service_data[loan_input - 1] 
                    print(f'You have selected {loan_data["service_name"]} !')
                    with USER_PATH.open('r') as file:
                        all_users: list[dict] = json.load(file) 

                        existing_user = None 
                        user_found = False 

                        id:int = int(input('Please enter your ID : ')) 

                        for user in all_users :
                            if user['id'] == id : 
                                existing_user = user 
                                user_found = True 

                        if user_found : 
                            print(f"Welcome Back {existing_user['name']} ! ")  
                            user = existing_user 
                        else : 
                            print('You are a new user !') 
                            name:str = input('Please enter your name : ') 
                            age:int = int(input('Please enter your age : ')) 
                            employed:str = input('Are you employed ? (1/0) : ') 
                            income:float = float(input('Please enter your income : ')) 
                            credit_score:int = int(input('Please enter your credit score : ')) 

                            user = {
                                
                                'id' : id, 
                                'name' : name, 
                                'age' : age, 
                                'employed' : employed, 
                                'income' : income, 
                                'credit_score' : credit_score , 
                                'history' : [] , 
                                'services' : [] , 
                                'loans' : [] , 
                                'insurance' : [] ,
                                'cards' : []
                            }

                            all_users.append(user) 


                        loan_amount:float = float(input('Please enter the loan amount you want to apply for : ')) 

                        loan_eligibility:bool = process_loan(user, loan_data , loan_amount) 

                        if not loan_eligibility : 
                            print('Sorry, you are not eligible for this loan !') 
                            continue

                        emi:float = calculate_monthly_emi(loan_amount, loan_data['interest_rate'], loan_data['duration_months']) 

                        print('You are eligible for this loan ! Further Details are as follows : ')  
                        print(f"Loan Amount : {loan_amount} ")
                        print(f"Interest Rate : {loan_data['interest_rate']} % ")
                        print(f"Duration : {loan_data['duration_months']} months ")
                        print(f"Monthly EMI : {emi:.2f} ") 

                        loan_choice:int = int(input('Do you want to proceed with the loan ? (1/0) : ') )

                        if(loan_choice == 1 ) : 
                            print('Congratulations, your loan has been approved !') 
                            user['loans'].append({
                                'loan_id' : len(user['loans']) + 1 ,
                                'loan_type' : loan_data['service_name'] , 
                                'loan_amount' : loan_amount , 
                                'emi' : emi , 
                                'interest_rate' : loan_data['interest_rate'] , 
                                'duration_months' : loan_data['duration_months'] , 
                                'status' : 'active' ,
                                'payment_history' : [] 
                            })
                            user['services'].append(loan_data['service_name']) 
                            user['history'].append(f"Applied for {loan_data['service_name']} of amount {loan_amount} with EMI {emi:.2f} at interest rate {loan_data['interest_rate']} % for duration of {loan_data['duration_months']} months.") 

                            with USER_PATH.open('w') as file:
                                json.dump(all_users, file, indent=4)


                        else : 
                            print('You have chosen not to proceed with the loan !') 

                        with USER_PATH.open('w') as file:
                            json.dump(all_users, file, indent=4) 
                            break 
                elif loan_input == 5 : 
                    print('You have selected to pay EMI !')
                    with USER_PATH.open('r') as file:
                        all_users: list[dict] = json.load(file) 

                        existing_user = None 
                        user_found = False 

                        id:int = int(input('Please enter your ID : ')) 

                        for user in all_users :
                            if user['id'] == id : 
                                existing_user = user 
                                user_found = True 

                        if not user_found : 
                            print('User not found ! Please apply for a loan first !') 
                            continue

                        print(f"Welcome Back {existing_user['name']} ! ")  
                        user = existing_user 

                        if len(user['loans']) == 0 : 
                            print('You have no active loans ! Please apply for a loan first !') 
                            continue

                        print('Your Active Loans are as follows : ') 
                        for loan in user['loans'] :
                            print(
                                f"Loan ID : {loan['loan_id']} , Loan Type : {loan['loan_type']} , "
                                f"Loan Amount : {loan['loan_amount']} , EMI : {loan['emi']:.2f} , "
                                f"Interest Rate : {loan['interest_rate']} % , Duration : {loan['duration_months']} months "
                                  ) 

                        loan_id:int = int(input('Please enter the Loan ID you want to pay EMI for : ')) 

                        selected_loan = None 
                        loan_found = False 

                        for loan in user['loans'] :
                            if loan['loan_id'] == loan_id : 
                                selected_loan = loan 
                                loan_found = True 

                        if not loan_found : 
                            print('Loan not found ! Please try again !') 
                            continue

                        print(f"You have selected Loan ID : {selected_loan['loan_id']} , Loan Type : {selected_loan['loan_type']} , Loan Amount : {selected_loan['loan_amount']} , EMI : {selected_loan['emi']:.2f} , Interest Rate : {selected_loan['interest_rate']} % , Duration : {selected_loan['duration_months']} months ") 

                        emi_payment:float = float(input('Please enter the EMI amount you want to pay : ')) 

                        if emi_payment < selected_loan['emi'] :
                            print(f"EMI amount is less than the required EMI of {selected_loan['emi']:.2f} . Please pay the full EMI amount !") 
                            continue
                        print(f"EMI of {emi_payment:.2f} paid successfully for Loan ID : {selected_loan['loan_id']} , Loan Type : {selected_loan['loan_type']} !")
                        selected_loan['payment_history'].append({
                            'loan_id' : selected_loan['loan_id'] ,
                            'loan_type' : selected_loan['loan_type'] ,
                            "amount": emi_payment,
                            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })

                        selected_loan['duration_months'] -= 1 

                        if selected_loan['duration_months'] == 0 :
                            selected_loan['status'] = 'closed' 
                            print(f"Congratulations ! You have completed your {selected_loan['loan_type']} !")

                        with USER_PATH.open('w') as file:
                            json.dump(all_users, file, indent=4) 
                            break


            except ValueError : 
                print('Invalid input, please try again !') 
                continue

            except Exception as e :
                print(f"An error occurred: {e}") 
                continue




        case 2 : 
            print('You have selected Insurance Services !') 

            try  : 
                insurance_input:int = int(input(
                    f"1 , for Health Insurance \n" 
                    f"2 , for Life Insurance \n"
                    f"0 , to Exit : \n"
                )) 

                if insurance_input == 0 : 
                    print('Thank you for using our system !') 
                    break 

                if insurance_input not in [1, 2] :
                    raise ValueError('Invalid input, please try again !') 


                insurance_data = service_data[insurance_input + 3] 

                print(f'You have selected {insurance_data["service_name"]} !')
                with USER_PATH.open('r') as file:
                    all_users: list[dict] = json.load(file) 
                    print(all_users) 

                    existing_user = None 
                    user_found = False 

                    id:int = int(input('Please enter your ID : ')) 

                    for user in all_users :
                        if user['id'] == id : 
                            existing_user = user 
                            user_found = True 

                    if user_found : 
                        print('Welcome back !') 
                        print(f"Welcome Back {existing_user['name']} ! ")  
                        user = existing_user 
                    else : 
                        print('You are a new user !') 
                        name:str = input('Please enter your name : ') 
                        age:int = int(input('Please enter your age : ')) 
                        employed:str = input('Are you employed ? (1/0) : ') 
                        income:float = float(input('Please enter your income : ')) 
                        credit_score:int = int(input('Please enter your credit score : '))  

                        user = {
                            
                            'id' : id, 
                            'name' : name, 
                            'age' : age, 
                            'employed' : employed, 
                            'income' : income, 
                            'credit_score' : credit_score , 
                            'history' : [] , 
                            'services' : [] , 
                            'loans' : [] , 
                            'insurance' : [] ,
                            'cards' : []
                        } 
                    all_users.append(user) 

                    coverage_amount:float = float(input('Please enter the coverage amount you want to apply for : ')) 

                    insurance_eligibility:bool = process_insurance(user, insurance_data , coverage_amount)

                    if not insurance_eligibility :
                        print('Sorry, you are not eligible for this insurance !') 
                        continue
                    monthly_premium:float = calculate_monthly_premium(coverage_amount, insurance_data['annual_premium_rate'], insurance_data['duration_months'])
                    print('You are eligible for this insurance ! Further Details are as follows : ')
                    print(f"Coverage Amount : {coverage_amount} ")  
                    print(f"Duration : {insurance_data['duration_months']} months ")
                    print(f"Monthly Premium : {monthly_premium:.2f} ")

                    insurance_choice:int = int(input('Do you want to proceed with the insurance ? (1/0) : ') ) 

                    if(insurance_choice == 1 ) :
                        print('Congratulations, your insurance has been approved !') 
                        user['insurance'].append({
                            'insurance_id' : len(user['insurance']) + 1 ,
                            'insurance_type' : insurance_data['service_name'] , 
                            'coverage_amount' : coverage_amount , 
                            'monthly_premium' : monthly_premium , 
                            'annual_premium_rate' : insurance_data['annual_premium_rate'] , 
                            'duration_months' : insurance_data['duration_months'] , 
                            'status' : 'active' ,
                            'payment_history' : [] 
                        })
                        user['services'].append(insurance_data['service_name']) 
                        user['history'].append(f"Applied for {insurance_data['service_name']} of coverage amount {coverage_amount} with monthly premium {monthly_premium:.2f} at annual premium rate {insurance_data['annual_premium_rate']} % for duration of {insurance_data['duration_months']} months.") 

                        with USER_PATH.open('w') as file:
                            json.dump(all_users, file, indent=4)
                    else : 
                        print('You have chosen not to proceed with the insurance !')

                    break 


                
            except ValueError : 
                print('Invalid input, please try again !') 
                continue
 


                    

                    