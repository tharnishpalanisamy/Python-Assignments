# if(take_loan == 1 ) : 
#                                 with user_path.open('r') as file:
#                                     users = json.load(file)  

#                                     user = check_user_exists(id)

#                                     if user:
#                                         user['services'].append(loan_data['service_name'])

#                                         user['history'].append(
#                                             f"Took a ${loan_amount} {loan_data['service_name']} "
#                                             f"with a duration of {loan_data['duration_months']} months"
#                                         )

#                                         user['emi_history'].setdefault(emi_name, []).append(emi)

#                                     else:
#                                         user = {
#                                             'id': id,
#                                             'name': name,
#                                             'age': age,
#                                             'income': income,
#                                             'employed': employed,
#                                             'history': [
#                                                 f"Took a ${loan_amount} {loan_data['service_name']} "
#                                                 f"with a duration of {loan_data['duration_months']} months"
#                                             ],
#                                             'services': [
#                                                 loan_data['service_name']
#                                             ],
#                                             'emi_history': {
#                                                 emi_name: [emi]
#                                             }
#                                         }

#                                         users.append(user)

#                                     with user_path.open('w') as file:
#                                         json.dump(users, file, indent=4)  

#                                         print('Your Loan is Sanctioned Successfullly ! ') 
#                                         break