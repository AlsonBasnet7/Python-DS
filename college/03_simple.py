Employee_name=str(input("Enter the Employee name"))
basic_salary=float(input("Enter the basic salary"))
Calculate_allowance=(10/100)*basic_salary
tax=(5/100)*basic_salary
netSalary=basic_salary+Calculate_allowance-tax
print("The allowance allowance amount is",Calculate_allowance)
print("The tax amount is",tax)
print('The net salary is ',netSalary)
