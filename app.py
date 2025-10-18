import time

first = "Emine"
last = "Güven Akyol"
full = f"{len(first)} {len(last)}"
print(full)

a = {24+57}
print(a)

course = "Python for Beginners"
print(course.upper())
print(course.lower())
print(course.title())


count = 0

while True:

    count = count + 1
    print("Deneme:", count)
    time.sleep(0.5)

    if count == 10:
        print("bıyyy")
        break
