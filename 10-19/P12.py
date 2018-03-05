#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#Let us list the factors of the first seven triangle numbers:

#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28

#We can see that 28 is the first triangle number to have over five divisors.

#What is the value of the first triangle number to have over five hundred divisors?

z = []
x = 1

while x > 0:
    z.append(x)
    r = sum(z)
    q = []
    if r == 1:
        q.append(r)
    else:
        q.append(r)
        q.append(1)
    for y in range(2,(r+1)):
        if y >= (r**0.5):
            break
        if r % 2 == 1:
            break
        if r % y == 0:
            q.append(y)
            q.append(y)
    if len(q) > 500:
        print(r)
        break
    x = x + 1