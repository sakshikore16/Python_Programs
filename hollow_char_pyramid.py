n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')

    count = 0
    for k in range(2 * i + 1):
        if k == 0 or k == 2 * i:
            print(chr(65 + count), end='')
            count += 1
        else:
            if i == n - 1:
                print(chr(65 + count), end='')
                count += 1
            else:
                print(' ', end='')
    print()