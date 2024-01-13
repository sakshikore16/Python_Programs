# Diamond Pattern

x = int (input ("Enter number of rows: "))

for i in range (1, x+1):
    for j in range (1, x - i + 1):
        print (" ", end = " ")
    
    for j in range (1, 2 * i):
        print("*", end = " ")
    
    print()

for i in range (x - 1, 0, -1):
    for j in range (1, x - i + 1):
        print (" ", end = " ")
    
    for j in range (1, 2 * i):
        print ("*", end = " ")

    print()

    
