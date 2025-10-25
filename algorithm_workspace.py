# Perfect number controller

n = int(input("Entry a number: "))
while n <= 1:
    n = int(input("Entry a number greater than 1: "))
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
