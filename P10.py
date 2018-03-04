#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

m = 10

for a in range(2,m):
    for x in range(2,m):
        if a % x == 0:
            if x < a:
                break
            if a == x:
                d = x
                print(d)
                d += d
                break

print(d)
