# accept input number from user
n = int(input("Enter any number: "))

# logic to calculate the factorial of a number
f = 1
while n >= 1:
    f *= n
    n -= 1

# print output
print("Factorial is", f)