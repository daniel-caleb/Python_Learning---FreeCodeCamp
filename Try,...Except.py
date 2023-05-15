try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid output")

try:
    try1 = 10 / 0
except ZeroDivisionError as err:
    print(err)
