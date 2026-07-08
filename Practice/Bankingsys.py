# Mini project on banking system

import time
print("\t \t \t WELCOME TO OUR BANKING SYSYTEM")
for i in range(1,17):
    print("  *  ",end="")
    time.sleep(0.2)
p=int(input("\nEnter the password:"))
if p==987543:
    print("password is correct")
    x=input("Enter your name:")
    y=int(input("Enter your accounts number:"))
    print("\n* * * CHECK YOUR NAME AND ACCOUNT NUMBER * * *\n",x)
    print("",y)
    print("\nThis is our service")
    a=int(input("\npress 1: Deposit\npress 2: Widthdrawal\npress 3: check balence\npress 4: Exit\nEnter your choice:"))
    bal=10000
    if a==1:
       i=int(input("Enter the amount you want to deposit in your account:"))
       sum=bal+i
       print("Now current balence is:",sum)
       print("THANK YOU")
    elif a==2:
        i=int(input("Enter the amount you want to widthdrawal:"))
        if i>bal:
            print("insufficient balence")
            print("THANK YOU")
        else:
            sub=bal-i
            print("Now current balence is:",sub)
            print("THANK YOU")
    elif a==3:
        print("your current balence",bal)
        print("THANK YOU")
    else:
        print("THANK YOU")
else:
    print("incorrect password please try again!!!")
    print("THANK YOU")
