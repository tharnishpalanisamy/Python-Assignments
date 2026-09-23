employees = [
    {"id": 101, "name": "Ravi", "dept": "IT", "salary": 55000.0},
    {"id": 102, "name": "Meena", "dept": "HR", "salary": 48000.0},
    {"id": 103, "name": "Karthik", "dept": "IT", "salary": 72000.0}
]

while True:
    print("\n--- Employee Management Console ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Find Highest Salary")
    print("5. Display Employees by Department")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    match choice:
        case "1":
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            salary = float(input("Enter Salary: "))

            emp = {"id": emp_id, "name": name, "dept": dept, "salary": salary}
            employees.append(emp)
            print("Employee added successfully.")

        case "2":
            if not employees:
                print("No employees found.")
            else:
                print("\nID\tName\t\tDepartment\tSalary")
                print("-" * 45)
                for e in employees:
                    print(f"{e['id']}\t{e['name']:<12}\t{e['dept']:<10}\tRs. {e['salary']:.2f}")

        case "3":
            query = input("Enter employee ID or name to search: ").lower()
            results = [e for e in employees if str(e["id"]) == query or e["name"].lower() == query]

            if results:
                for e in results:
                    print(f"Found: ID={e['id']}, Name={e['name']}, Dept={e['dept']}, Salary=Rs. {e['salary']:.2f}")
            else:
                print("Employee not found.")

        case "4":
            if not employees:
                print("No employee records available.")
            else:
                top_earner = max(employees, key=lambda e: e["salary"])
                print(f"Highest Salary: {top_earner['name']} with Rs. {top_earner['salary']:.2f} ({top_earner['dept']})")

        case "5":
            dept_name = input("Enter department name: ").strip().lower()
            filtered = [e for e in employees if e["dept"].lower() == dept_name]

            if filtered:
                print(f"\nEmployees in {dept_name.upper()}:")
                for e in filtered:
                    print(f"- {e['name']} (ID: {e['id']}), Salary: Rs. {e['salary']:.2f}")
            else:
                print(f"No employees found in department '{dept_name}'.")

        case "6":
            print("Exiting Employee Management Console.")
            break

        case _:
            print("Invalid choice, please select between 1 and 6.")
