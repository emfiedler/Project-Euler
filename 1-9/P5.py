#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

x = 1
sq = []
su = []

while x <= 100:
    y = x**2
    sq.append(y)
    su.append(x)
    x = x + 1

print((sum(su))**2-sum(sq))
