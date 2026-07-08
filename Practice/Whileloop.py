# Basic While Loop

m = int(input("Enter the table you want:"))
c = 1

while c <= 10:
    r = c * m
    print(f"{c}X{m}={r}")
    c += 1