# calculate percentage of five subject and give 1st,2nd and 3rd division according to percentage

a=float(input("Enter marks of 1st subject:"))
b=float(input("Enter marks of 2st subject:"))
c=float(input("Enter marks of 3st subject:"))
d=float(input("Enter marks of 4st subject:"))
e=float(input("Enter marks of 5st subject:"))
p=(a+b+c+d+e)/5
print("\nthe marks obtained in percentage:",p)
if p>=90:
    print("grade A and 1st Division")
elif p>=70:
    print("grade B and 2nd Division")
elif p>=50:
    print("grade C and 3rd Division")
elif p>=33:
    print("grade D and 4th Dividion")
else:
    print("fail")