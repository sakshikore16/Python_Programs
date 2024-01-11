print("_________________Welcome to calculator !_________________ ")  

#Assigment operators used to simply assign data. 
a = int (input ("Enter first number: ") )
b = int (input ("Enther secound number: "))
choice = int (input ("Enter the calculation you want to perform 1 for Addition, 2 for substraction, 3 for multiplication and 4 for division "))


#logical operator used to check if condition. 
if choice <= 4:
    #Arthematic operators used for calculations. 
    def case1 ():
        print (a+b)
    def case2 ():
        print (a-b)
    def case3 ():
        print (a*b)
    def case4 ():
        print (a/b)

    def switch_case(case):
        #comparision operators to check conditions. 
        if(case == 1):
            case1()
        elif(case == 2):
            case2()
        elif(case == 3):
            case3()
        elif(case == 4):
            case4()
        
    switch_case(choice)

    

else:
    print ("Enter number between 1 to 5... Please! ")  