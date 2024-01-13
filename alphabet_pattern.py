n = int(input("Enter Number of rows: "))

for i in range (-1, 0, n):
    for j in range (n + 1, i):
        print (chr(j+64), end = " ") 
    print(" ")
