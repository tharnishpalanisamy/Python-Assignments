import csv 
from config import SERVICE_PATH 
from Modules.services.mail import EmailSender 
from Modules.models.LoanService import LoanService  
from Modules.services.LoanProcessor import LoanProcessor 
from Modules.services.LoanPaymentService import LoanPaymentService 
from Modules.repositories.UserRepository import UserRepository  

try:
    with SERVICE_PATH.open('r') as file:
        service_data: list[dict] = list(csv.DictReader(file)) 
except Exception as error:
    print(f"Error loading service data: {error}")
    exit(1)

print('Welcome To our System !') 

while True: 
    print('\nPlease select the service you want to use : ') 
    try:
        user_input: int = int(input(
            f"1 , for Loan Services \n" 
            f"0 , to Exit : \n"
        )) 
    except ValueError:
        print("Invalid input, please enter a valid number.")
        continue

    match user_input: 
        case 0: 
            print('Thank you for using our system !') 
            break 

        case 1: 
            print('You have selected Loan Services !') 
            try: 
                loan_input: int = int(input(
                    f"1 , for Personal Loan \n" 
                    f"2 , for Home Loan \n" 
                    f"3 , for Car Loan \n" 
                    f"4 , for Education Loan \n" 
                    f"5 , to pay EMI \n" 
                    f"0 , to Exit : \n"
                )) 
                
                if loan_input == 0: 
                    print('Thank you for using our system !') 
                    break 

                if loan_input not in [1, 2, 3, 4, 5]:
                    raise ValueError('Invalid input, please try again !') 

                if loan_input in [1, 2, 3, 4]:
                    loan = service_data[loan_input - 1] 
                    loan_data = LoanService(
                        id=int(loan["id"]),
                        service_name=loan["service_name"],
                        interest_rate=float(loan["interest_rate"]),
                        duration_months=int(loan["duration_months"]),
                        minimum_age=int(loan["minimum_age"]),
                        maximum_age=int(loan["maximum_age"]),
                        employment_required=loan["employment_required"].lower() == "true",
                        credit_score_required=int(float(loan["credit_score_required"]))
                    )

                    print(f'You have selected {loan_data.service_name} !')

                    id: int = int(input('Please enter your ID : ')) 
                    if id <= 0:
                        raise ValueError("User ID must be greater than zero.")

                    user_repository = UserRepository() 
                    user = user_repository.find(id)
                    if not user:
                        user = user_repository.create_user(id)
                        user_repository.save_user(user)
                    else:
                        print(f"Welcome Back {user.name} ! ")

                    loan_amount: float = float(input('Please enter the loan amount you want to apply for : ')) 
                    if loan_amount <= 0:
                        raise ValueError("Loan amount must be greater than zero.")

                    loan_processor = LoanProcessor() 
                    loan_data.display_eligibility(loan_amount=loan_amount) 

                    loan_eligibility: bool = loan_data.check_eligibility(
                        user_data=user, loan_amount=loan_amount
                    )
                    print()
                    if not loan_eligibility: 
                        print('Sorry, you are not eligible for this loan !') 
                        continue
                    
                    emi: float = loan_processor.calculate_emi(
                        loan_amount=loan_amount, 
                        interest=loan_data.interest_rate, 
                        duration=loan_data.duration_months
                    ) 

                    loan_processor.display_summary(loan_amount=loan_amount, loan_data=loan_data, emi=emi)

                    loan_choice: int = int(input('Do you want to proceed with the loan ? (1/0) : '))
                    if loan_choice not in [0, 1]:
                        raise ValueError("Invalid choice, enter 1 to proceed or 0 to cancel.")

                    if loan_choice == 1: 
                        email_sender = EmailSender() 
                        if email_sender.authenticate_user(user.email):
                            loan_approval = loan_processor.approve_loan(
                                loan_data=loan_data, 
                                user_data=user, 
                                loan_amount=loan_amount
                            ) 
                            if loan_approval:
                                print(f'Congratulations your loan of {loan_amount} has been sanctioned ! ') 
                        else:
                            print("Authentication was unsuccessful.")
                            continue 
                    else: 
                        print('You have chosen not to proceed with the loan !') 

                    break 

                elif loan_input == 5: 
                    print('You have selected to pay EMI !')

                    id: int = int(input('Please enter your ID : ')) 
                    if id <= 0:
                        raise ValueError("User ID must be greater than zero.")

                    user_repository = UserRepository()  
                    loan_processor = LoanProcessor() 
                    payment_processor = LoanPaymentService() 

                    user = user_repository.find(id) 
                    if not user:
                        print('User not found ! Please apply for a loan first !') 
                        continue
                    print(f"Welcome Back {user.name} ! ")  

                    has_loans = loan_processor.display_user_loans(user.id) 
                    if not has_loans:
                        continue

                    loan_id: int = int(input('Please enter the Loan ID you want to pay EMI for : ')) 
                    if loan_id <= 0:
                        raise ValueError("Loan ID must be greater than zero.")
                    
                    selected_loan = loan_processor.find_loan(loan_id=loan_id, user_data=user)
                    if not selected_loan:
                        print(f"Loan with ID {loan_id} was not found for this user.")
                        continue

                    if selected_loan.status.lower() == 'closed':
                        print('This loan is already closed and fully paid off.')
                        continue

                    loan_processor.display_selected_loan(selected_loan)

                    emi_payment: float = float(input('Please enter the EMI amount you want to pay : ')) 
                    if emi_payment <= 0:
                        raise ValueError("Payment amount must be greater than zero.")

                    valid_payment = payment_processor.validate_payment(amount=emi_payment, emi=selected_loan.emi) 

                    if valid_payment:
                        payment_processor.process_payment(loan_data=selected_loan, user_id=user.id, amount=emi_payment)  
                        break
                    else:
                        continue

            except ValueError as error:
                print(f"Invalid input: {error}")
                continue

            except Exception as e:
                print(f"An error occurred: {e}") 
                continue

        case _:
            print("Invalid option selected, please choose 1 or 0.")
