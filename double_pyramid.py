n = int (input("Enter the number of rows: "))

for i in range (1, n + 1):
    for j in range(i, n):
        print(" ", end="")
    
    for j in range(1, 2 * i):
        print("*", end="")
    
    for j in range(2 * i, 2 * n):
        print(" ", end="")
    
    for j in range(1, 2 * i):
        print("*", end="")
    
    print()