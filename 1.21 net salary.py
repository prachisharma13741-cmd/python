grosssalary = int(input("Enter gross salary"))
allowance = 0.10*grosssalary
deduction = 0.03*grosssalary

netsalary = grosssalary + allowance - deduction

print("net salary",netsalary)
