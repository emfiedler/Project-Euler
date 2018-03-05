#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

def p(a):
    for b in range(2, int(a**0.5 +1)):
        if a % b == 0:
            return False
        
    return True

def s(n):
    sum = 2

    for x in range(3,n,2):
        if p(x):
            sum += x 

    return sum

print(s(2000000))
