# Greatest of 3 given number

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if a>b and a>c:
    print("the given 1st number is greatest",a)
elif b>a and b>c:
    print("the given 2nd number is greatest",b)
elif c>a and c>b:
    print("the given 3rd number is greatest",c)
else:
    print("\nplease check all given numbers are equal:",a)
    print("",b)
    print("",c)