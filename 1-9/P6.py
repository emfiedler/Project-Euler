#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


x = 1
y = 1
n = 0

while x <= float("inf"):
    d = True
    y = 1
    while y <= x:
        if x % y == 0 and y != 1:
            if y < x:
                d = False
            if y == x and d == True:
                n = n + 1
                print(x)
        if d == False:
            break
        else:
            y = y + 1
    if n == 10001:
        print(x)
        break
    x = x + 1
