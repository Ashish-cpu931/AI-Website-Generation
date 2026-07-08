print(" \t \t * * * WELCOME BOOK STORE SYSTEM * * *")
lbook=[]
lname=[]
lbranch=[]
lyear=[]
while(1):
    a=int(input("\nWe have the following services \n1) Detail Entry \n2) Check Details \n3) Return Book \n4) Exit \n\nEnter your choice:"))
    if (a==1):
        name=input("Enter your name:")
        branch=input("Enter your branch:")
        year=int(input("Enter your year:"))
        nbook=int(input("\nHow many book you want:"))
        for i in range(nbook):
            book=input()
            lbook.append(book)
        lname.append(name)
        lbranch.append(branch)
        lyear.append(year)
        print("Data added successfully")
    elif (a==2):
         checkname=input("Enter your name:")
         for i in lname:
            if(checkname==i):
                print(lbook)
    elif (a==3):
        returnbook=input()
        for i in lname:
            if(returnbook==i):
                lbook.remove(i)
        print("Book return successfully")
    else:
        print("THANK YOU")
        break
        
             
        
        
        
            
        
        
        
