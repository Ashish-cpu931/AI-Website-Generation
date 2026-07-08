# leap year or not

y=int(input("Enter the year:"))
if y%400==0 and y%4==0:
    print("leap year")
elif y%100!=0:
    print("Not a leap year")
    
# leap year
'''def is_leap(year):
    leap = False
    
    if (year%400==0):
        leap = True
    elif(year%4==0):
        leap = True
    elif (year%100==0):
        leap = False 
    # Write your logic here
    return leap

year = int(input())
print(is_leap(year))'''