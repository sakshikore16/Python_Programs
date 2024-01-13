n = int(input("Enter number of rows: "))

for i in range(n):
    
    for j in range(i):
        print(' ', end='')
        
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='')
        
    print()
