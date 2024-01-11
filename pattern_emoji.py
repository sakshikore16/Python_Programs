n = 5  # You can adjust the size of the pattern by changing this value
for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "💗 " * (2 * i + 1)
        print(spaces + stars)

for i in range(n - 2, -1, -1):
        spaces = " " * (n - i - 1)
        stars = "💗 " * (2 * i + 1)
        print(spaces + stars)

