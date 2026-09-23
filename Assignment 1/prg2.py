emp_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
experience = float(input("Enter years of experience: "))

hra = 0.20 * basic_salary
da = 0.10 * basic_salary
gross_salary = basic_salary + hra + da

if experience >= 5:
    bonus = 0.15 * basic_salary
elif experience >= 3:
    bonus = 0.10 * basic_salary
else:
    bonus = 0.05 * basic_salary

net_salary = gross_salary + bonus

if net_salary >= 80000:
    category = "High"
elif net_salary >= 40000:
    category = "Medium"
else:
    category = "Entry Level"

print("\n--- Salary Details ---")
print(f"Employee Name : {emp_name}")
print(f"Basic Salary  : {basic_salary:.2f}")
print(f"HRA (20%)     : {hra:.2f}")
print(f"DA (10%)      : {da:.2f}")
print(f"Gross Salary  : {gross_salary:.2f}")
print(f"Bonus         : {bonus:.2f}")
print(f"Net Salary    : {net_salary:.2f}")
print(f"Salary Band   : {category}")
