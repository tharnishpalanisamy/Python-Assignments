employees = [
    {   
        'id' : 101 , 
        'name' : 'tharnish' ,  
        'salary' : 20000 , 
        'department' : 'IT'
        
    } , 
    {
        'id' : 102 , 
        'name' : 'Sastha' , 
        'salary' : 25000 , 
        'department' : 'HR'
    } , 
    {
        'id' : 103 , 
        'name' : 'Karthik' , 
        'salary' : 30000 ,
        'department' : 'IT'
    }

]

print("Initial list of employees:") 
for emp in employees : 
    print('-------------')
    print(emp) 
    print('-------------')


while True : 
    choice = int (input(
        f"1 . Add Employee  \n" 
        f"2. View Employee \n " 
        f"3. Search Employee \n" 
        f"4. Highest Salary \n" 
        f"5. display employees by department \n" 
        f"6. Exit  : " 
    ))

    match choice : 
        case 1 : 
            employee_id = int(input('Enter the employee id : '))
            employee_name = input('Enter the employee Name  : ' )  
            employee_salary = float(input('Enter the employee Salary : ')) 
            employee_department = input('Enter the employee department : ')

            new_emp = {
                'id' : employee_id , 'name' : employee_name , 'salary' : employee_salary , 'department' : employee_department
            }

            employees.append(new_emp)

            user_continue = input('click 1 to continue : ')
            if user_continue != '1' :
                break


        case 2 :
            search_id = int(input('Enter the employee id to search : '))
            for emp in employees : 
                if emp['id'] == search_id :
                    print(
                        f"Id : {emp['id']}" 
                        f"Name : {emp['name']}" 
                        f"Salary : {emp['salary']}" 
                        f"Department : {emp['department']}"
                    ) 
                    break

            user_continue = input('click 1 to continue : ')
            if user_continue != '1':
                break

        case 3 :
            search_id = int(input('Enter the employee id to search : '))

            for emp in employees :
                if emp['id'] == search_id :
                    print(
                        f"Id : {emp['id']}" 
                        f"Name : {emp['name']}" 
                        f"Salary : {emp['salary']}" 
                        f"Department : {emp['department']}"
                    )
                    break
            print('Employee Not Found')
            user_continue = input('click 1 to continue : ')
            if user_continue != '1':
                break
        case 4 :
            highest = 0
            search_id = 0
            for emp in employees :
                if emp['salary'] > highest :
                    highest = emp['salary']
                    search_id = emp['id']
            for emp in employees :
                if emp['id'] == search_id :
                    print(
                        f"Id : {emp['id']}" 
                        f"Name : {emp['name']}" 
                        f"Salary : {emp['salary']}" 
                        f"Department : {emp['department']}"
                    )
                    break

            user_continue = input('click 1 to continue : ')
            if user_continue != '1':
                break

        case 5 :
            depts = set()
            for emp in employees :
                depts.add(emp['department'])

            for dept in depts :
                for emp in employees :
                    if dept == emp['department'] :
                        print(
                            f"Id : {emp['id']}" 
                            f"Name : {emp['name']}" 
                            f"Salary : {emp['salary']}" 
                            f"Department : {emp['department']}"
                        )

            user_continue = input('click 1 to continue : ')
            if user_continue != '1':
                break
        case 6 :
            print('Thanks for using out system')
            break
        case _ :
            print('Invalid Choice')





