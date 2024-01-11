for j in range(2,0,-1):
    i = 67
    i-=(2-j)
    for k in range(0,j):
        print(" ",end=" ")
    for k in range(0,(5-j)):
        print(chr(i)+"  ",end=" ")
        i+=1
    print()
for j in range(0,3):
    i = 65
    for k in range(0,j):
        print(" ",end=" ")
    for k in range(j,5):
        print(chr(j+i)+"  ",end=" ")
        i+=1
    print()
    