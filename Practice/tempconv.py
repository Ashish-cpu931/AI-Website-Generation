# convert temperature farenhite to celcius and vice-versa

f=float(input("Enter the temperature:"))
d=int(input("1 for farenhite to degree celcius and 2 for degree celcius to farenhite :"))
if d==1:
    c=(5/9)*(f-32)
    print("temperatue in degree celcius",c)
elif d==2:
    fn=f*(9/5)+32
    print("temperature in farenhite:",fn)