num = int(input("Enter a number: "))
temp = num
sum = 0
power = len(str(num))

while num > 0:
    digit = num % 10
    sum = sum + digit ** power
    num = num // 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")