#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import time

start_time = time.time()

#Finding abundants
def div(n):
    num = []
    for y in range(1, n):
        if n % y == 0:
            num.append(y)
    
    sm = sum(num)
    if sm > n:
        return True
    else:
        return False

#Listing abundants
ab = []
for x in range(1, 28123 + 1):
    d = div(x)
    if d is True:
        ab.append(x)

#Summing of sums
bb = []
for z in ab:
    for y in ab:
        add = z + y
        if add > 28123:
            break
        else:
            bb.append(add)

#Uniques
un = set(bb)
#Summing non-abundants
f = 0
for c in range(1, 28123 + 1):
    if c not in un:
        f += c
    else:
        continue

print(f)
print("{} ms".format(round(1000 * (time.time() - start_time))))
