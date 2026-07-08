print("\t\t * * * WELCOME TO OUR PHONE BOOK * * *")
lname=[]
lnumber=[]
while(1):
    a=int(input("\n OUR SERVICES ARE:- \n\n 1.Add new phone number \n 2.Show all phone numbers \n 3.Delete phone number \n 4.Exit \n\nEnter your choice:"))
    if a==1:
        c=str(input("Enter mobile number:"))
        if len(c)==10:
            lnumber.append(c)
            b=input("Enter your name:")
            lname.append(b)
            print("\nGiven number added successfully \nThank you")
        else:
            print("Invalid number \nplease try again")
    elif a==2:
        if len(lname)==0:
            print("Phone book is empty")
        else:
            print("The numbers are:-")
            for i in range(len(lname)):
                print(lname[i],":",lnumber[i])
    elif a==3:
        d=input("Enter the name you want to delete:")
        if len(lname)==0:
            print("phone book is empty")
        else:
            for i in range(len(lname)):
                    if lname [i]==d:
                        lname.pop(i)
                        lnumber.pop(i)
                        print("given name and number deleted sucessfully")
    else:
        break
print("\t \t \t * * * Thank you * * *")
        
        
