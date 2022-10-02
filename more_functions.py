def checkOddEven(n):
    evenSet = []
    oddset = []
    if n % 2 != 0:
        statement1 = (f"{n} is odd")
        for i in range(3, 31):
            oddset.append(i)
        if n in oddset:
            statement = (f"{n} is within the range of 3 and 30")
        else:
            statement = (f"{n} is not within this range")
    elif n % 2 == 0:
        statement1 = (f"{n} is even")
        for i in range(2, 21):
            evenSet.append(i)
        if n in evenSet:
            statement = (f"{n} is within the range of 2 and 20")
        else:
            statement = (f"{n} is not within this range")
    else:
        print("outside parameters")

    return (statement1, statement)


def checkLeapYear(n):
    if n % 4 == 0:
        Statement = (f"{n} is a leap year")
    else:
        Statement = (f"{n} is not a leap year")
    return Statement


def checkAttendanceStatus(n):
    n = (n / 12) * 100
    if n <= 75:
        statement = ("you are not eligible to write this exam")
    else:
        statement = ("you are eligible to write this exam")
    return statement


def dispalyReverseList(k):
    k = set(k)
    k = list(k)
    k.reverse()
    return k


wantMore = "yes"
while wantMore == "yes":
    num = input("enter your number")
    num = int(num)
    if num % 2 != 0:
        print(f"{num} is an odd number")
    elif num % 2 == 0:
        print(f"{num} is an even number")
    wantMore = input("wanna continue")