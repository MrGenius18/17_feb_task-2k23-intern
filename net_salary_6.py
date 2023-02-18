''' 
    enter salary of employee monthly
    if salary is grt than 200000 then give 5% tax
    if salary is grt than 500000 then give 10% tax
    if salary is grt than 1000000 then give 15% tax
    if salary is grt than 1500000 then give 20% tax
    net salary
'''
month=int(input("Enter the monthly salary:"))

salary=month*12

if salary>200000:
    net=salary-(salary*0.05)
    print("net salary is",net/12)
elif salary>500000:
    net=salary-(salary*0.1)
    print("net salary is",net/12)
elif salary>1000000:
    net=salary-(salary*0.2)
    print("net salary is",net/12)
else:
    print("net salary is",salary)
