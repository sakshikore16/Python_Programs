# WAP to calculate how many sundays have you lived from the day you were born. take input of birthday from user.

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

birthdate = int(input("Birth Day : "))
birthmonth = int(input("Birth Month : "))
birthyear = int(input("Birth Year :  "))

todayday = input("What is today's day(M/Tu/W/Th/F/Sa/Su) : ")

currentdate = int(input("Current date : "))
currentmonth = int(input("Current Month : "))
currentyear = int(input("Current year: "))

dayslived = 0
sundayslived = 0

for m in range(currentmonth - 1):
    dayslived += month[m]
dayslived += currentdate

for m in range(birthmonth - 1, 12):
    if m == birthmonth - 1:
        dayslived += month[m] - birthdate + 1
    else:
        dayslived += month[m]

totalyears = currentyear - birthyear - 1
dayslived += totalyears * 365

leapyear = [i for i in range(birthyear + 1, currentyear) if (i % 400 == 0) or (i % 4 == 0 and (i % 100 != 0))]
dayslived += len(leapyear)

if (birthyear % 400 == 0 or (birthyear % 4 == 0 and birthyear % 100 != 0)) and birthmonth < 3 and birthdate != 29:
    dayslived += 1

if (currentyear % 400 == 0 or (currentyear % 4 == 0 and currentyear % 100 != 0)) and currentmonth >= 2:
    if currentmonth == 2 and currentdate == 29:
        dayslived += 1
    elif currentmonth > 2:
        dayslived += 1

sundayslived += dayslived // 7

print("Total Number Of Sunday's You Have Lived: ", sundayslived)
