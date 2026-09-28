










        # case 2 : 
        #     print('You have selected Insurance Services !') 

        #     try  : 
        #         insurance_input:int = int(input(
        #             f"1 , for Health Insurance \n" 
        #             f"2 , for Life Insurance \n"
        #             f"0 , to Exit : \n"
        #         )) 

        #         if insurance_input == 0 : 
        #             print('Thank you for using our system !') 
        #             break 

        #         if insurance_input not in [1, 2] :
        #             raise ValueError('Invalid input, please try again !') 


        #         insurance_data = service_data[insurance_input + 3] 

        #         print(f'You have selected {insurance_data["service_name"]} !')
        #         with USER_PATH.open('r') as file:
        #             all_users: list[dict] = json.load(file) 
        #             print(all_users) 

        #             existing_user = None 
        #             user_found = False 

        #             id:int = int(input('Please enter your ID : ')) 

        #             for user in all_users :
        #                 if user['id'] == id : 
        #                     existing_user = user 
        #                     user_found = True 

        #             if user_found : 
        #                 print('Welcome back !') 
        #                 print(f"Welcome Back {existing_user['name']} ! ")  
        #                 user = existing_user 
        #             else : 
        #                 print('You are a new user !') 
        #                 name:str = input('Please enter your name : ') 
        #                 age:int = int(input('Please enter your age : ')) 
        #                 employed:str = input('Are you employed ? (1/0) : ') 
        #                 income:float = float(input('Please enter your income : ')) 
        #                 credit_score:int = int(input('Please enter your credit score : '))  

        #                 user = {
                            
        #                     'id' : id, 
        #                     'name' : name, 
        #                     'age' : age, 
        #                     'employed' : employed, 
        #                     'income' : income, 
        #                     'credit_score' : credit_score , 
        #                     'history' : [] , 
        #                     'services' : [] , 
        #                     'loans' : [] , 
        #                     'insurance' : [] ,
        #                     'cards' : []
        #                 } 
        #             all_users.append(user) 

        #             coverage_amount:float = float(input('Please enter the coverage amount you want to apply for : ')) 

        #             insurance_eligibility:bool = process_insurance(user, insurance_data , coverage_amount)

        #             if not insurance_eligibility :
        #                 print('Sorry, you are not eligible for this insurance !') 
        #                 continue
        #             monthly_premium:float = calculate_monthly_premium(coverage_amount, insurance_data['annual_premium_rate'], insurance_data['duration_months'])
        #             print('You are eligible for this insurance ! Further Details are as follows : ')
        #             print(f"Coverage Amount : {coverage_amount} ")  
        #             print(f"Duration : {insurance_data['duration_months']} months ")
        #             print(f"Monthly Premium : {monthly_premium:.2f} ")

        #             insurance_choice:int = int(input('Do you want to proceed with the insurance ? (1/0) : ') ) 

        #             if(insurance_choice == 1 ) :
        #                 print('Congratulations, your insurance has been approved !') 
        #                 user['insurance'].append({
        #                     'insurance_id' : len(user['insurance']) + 1 ,
        #                     'insurance_type' : insurance_data['service_name'] , 
        #                     'coverage_amount' : coverage_amount , 
        #                     'monthly_premium' : monthly_premium , 
        #                     'annual_premium_rate' : insurance_data['annual_premium_rate'] , 
        #                     'duration_months' : insurance_data['duration_months'] , 
        #                     'status' : 'active' ,
        #                     'payment_history' : [] 
        #                 })
        #                 user['services'].append(insurance_data['service_name']) 
        #                 user['history'].append(f"Applied for {insurance_data['service_name']} of coverage amount {coverage_amount} with monthly premium {monthly_premium:.2f} at annual premium rate {insurance_data['annual_premium_rate']} % for duration of {insurance_data['duration_months']} months.") 

        #                 with USER_PATH.open('w') as file:
        #                     json.dump(all_users, file, indent=4)
        #             else : 
        #                 print('You have chosen not to proceed with the insurance !')

        #             break 


                
        #     except ValueError : 
        #         print('Invalid input, please try again !') 
        #         continue
 


                    

                    