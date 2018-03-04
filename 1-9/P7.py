#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

n = 600851475143 
f = 1
fa = []

while f < n:
    if n % f == 0:
        x = 1
        while x <= f:
            if f % x == 0 and x != 1:
                if x < f:
                    break
                else:
                    print(f)
                    fa.append(f)
            x = x + 2
    f = f + 2

print(max(fa))
