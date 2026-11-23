name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))

hra = basic * 0.20
da = basic * 0.10

gross = basic + hra + da

deductions = basic * 0.12

net = gross - deductions

print("\nEmployee Name:", name)
print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross)
print("Deductions:", deductions)
print("Net Salary:", net)