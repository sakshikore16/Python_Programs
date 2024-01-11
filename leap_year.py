a=int(input("Enter a Year: "))

if(a%400==0 and a%4==0):
    print("The year ",a, "is a leap year ")
else:
    print("The year ",a," is not a leap year ")