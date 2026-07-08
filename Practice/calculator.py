# calculator for 2 numbers user input 

a=float(input("Enter 1st number:"))
b=float(input("Enter 2nd number:"))
c=int(input("\nEnter 1 for addition \nEnter 2 for multiplication \nEnter 3 for subtraction \nEnter 4 for division \nEnter 5 for modulus \n\nEnter the number:\n"))
if c==1:
    print("the addition of given numbers:",a+b)
elif c==2:
    print("the multiplicaton of given numbers:",a*b)
elif c==3:
    print("the subtraction of given numbers:",a-b)
elif c==4:
    print("the division of given numbers:",a/b)
elif c==5:
    print("the modulus of given numbers:",a%b)