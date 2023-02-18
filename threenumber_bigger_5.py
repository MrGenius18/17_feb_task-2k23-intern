# Take 3 numbers from user and check which one is bigger or same??

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))

if a==b & a==c:
    print("all are same")
elif a>=b & a>=c:
    print(a, "is bigger")
elif b>=a & b>=c:
    print(b, "is bigger")
else:
    print(c, "is bigger")           

