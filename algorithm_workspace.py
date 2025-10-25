# Perfect number controller
"""
n = int(input("Enter a number: "))
while n <= 1:
    n = int(input("Enter a number greater than 1: "))
print("Correct number")

i = 1
m = 0
while i < n:
    if n % i == 0:
        m = m + i
    else:
        pass
    i = i + 1
    print("m: {}, i: {}".format(m, i))

if m == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")
"""
# Armstrong number controller

number = int(input("Enter a number (bigger than 0): "))

count = 0
_number = number
buffer = []
print(type(_number))

if number <= 0:
    print("Try again!")

else:
    while _number > 0:
        _number = int(_number / 10)
        print(_number)
        x = _number * 10
        print(x)
        x = int((number/10**count)) - x
        print(x)
        buffer.append(x)
        print(buffer)
        count = count + 1
        print("_number {}, count {}".format(_number, count))

    print("Digit number is: ", count)

    total = 0

    for i in range(count):

        total = total + buffer[i]**count
        print(total)

    if total == number:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")
