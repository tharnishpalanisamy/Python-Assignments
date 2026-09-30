import json
from config import SERVICE_PATH 
from Modules.services.mail import EmailSender 
from Modules.models.LoanService import LoanService  
from Modules.services.LoanProcessor import LoanProcessor 
from Modules.services.LoanPaymentService import LoanPaymentService 
from Modules.repositories.UserRepository import UserRepository  
from Modules.Exception.exception import UserNotFoundException , InvalidEmailException,UserNotAuthenticatedException,LoanNotFoundException

with SERVICE_PATH.open('r') as file:
    service_data: list[dict] = json.load(file)

print('Welcome To our System !') 

while True: 
    print('Please select the service you want to use : ') 
    user_input:int = int(input(
        f"1 , for Loan Services \n" 
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
                    loan = service_data[loan_input - 1] 
                    loan_data = LoanService(
                        id = loan['id'] , 
                        service_name=loan['service_name'] , 
                        interest_rate=loan['interest_rate'] ,
                        duration_months=loan['duration_months'] ,
                        eligibility=loan['eligibility']
                        )

                    print(f'You have selected {loan_data.service_name} !')

                    id:int = int(input('Please enter your ID : ')) 

                    user_repository = UserRepository() 

                    try : 
                        user = user_repository.find(id)   
                    except UserNotFoundException as error :
                        try:
                            user = user_repository.create_user(id)
                            user_repository.save_user(user)  
                        except ValueError as error :
                            print(error) 
                            continue 
                        except InvalidEmailException as error : 
                            print(error) 
                            continue 
                    else : 
                        print(f"Welcome Back {user.name} ! ")  
                    

                    loan_amount:float = float(input('Please enter the loan amount you want to apply for : ')) 

                    loan_processor = LoanProcessor() 

                    loan_data.display_eligibility(loan_amount=loan_amount) 
                    loan_eligibility:bool = loan_data.check_eligibility(
                        user_data=user , loan_amount=loan_amount
                    )

                    if not loan_eligibility : 
                        print('Sorry, you are not eligible for this loan !') 
                        continue

                    emi:float = loan_processor.calculate_emi(
                        loan_amount=loan_amount , 
                        interest=loan_data.interest_rate , 
                        duration=loan_data.duration_months
                    ) 

                    loan_processor.display_summary(loan_amount=loan_amount , loan_data= loan_data , emi=emi)

                    loan_choice:int = int(input('Do you want to proceed with the loan ? (1/0) : ') )

                    if(loan_choice == 1 ) : 

                        email_sender = EmailSender() 
                        try : 

                            user_authenticated = email_sender.authenticate_user(user.email) 

                            loan_approval = loan_processor.approve_loan(
                                loan_data=loan_data , 
                                user_data=user , 
                                loan_amount=loan_amount
                            ) 
                            if loan_approval :
                                print(f'Congradulations your loan of {loan_amount} has been sanctioned ! ' ) 
                                
                                user_repository.update_user(user) 
                        except UserNotAuthenticatedException as error :
                            print(error) 
                            continue 

                    else : 
                        print('You have chosen not to proceed with the loan !') 

                    break 

                elif loan_input == 5 : 
                    print('You have selected to pay EMI !')

                    id:int = int(input('Please enter your ID : ')) 

                    user_repository = UserRepository()  
                    loan_processor = LoanProcessor() 
                    payment_processor = LoanPaymentService() 

                    try : 
                        user = user_repository.find(id) 
                        print(f"Welcome Back {user.name} ! ")  

                    except UserNotFoundException as error:
                        print('User not found ! Please apply for a loan first !') 
                        continue

                    if len(user.loans) == 0 : 
                        print('You have no active loans ! Please apply for a loan first !') 
                        continue

                    user.display_loans() 

                    loan_id:int = int(input('Please enter the Loan ID you want to pay EMI for : ')) 

                    try : 
                        selected_loan = loan_processor.find_loan(loan_id=loan_id , user_data=user)  

                    except LoanNotFoundException as error :
                        print(error) 
                        continue 

                    else : 

                        loan_processor.display_selected_loan(selected_loan)

                        emi_payment:float = float(input('Please enter the EMI amount you want to pay : ')) 

                        valid_payment = payment_processor.validate_payment(amount = emi_payment , emi = selected_loan.emi) 

                        if valid_payment :
                            payment_processor.process_payment(loan_data=selected_loan , amount= emi_payment)  

                        user_repository.update_user(user)
                        break

            except ValueError : 
                print('Invalid input, please try again !') 
                continue

            except Exception as e :
                print(f"An error occurred: {e}") 
                continue
