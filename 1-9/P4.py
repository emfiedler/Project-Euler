#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

x = 20
b = 1
d = False

while x < float("inf"):
    b = 1
    while b <= 20:
        if x % b == 0:
            if b == 20:
                print(x)
                d = True
        else:
            break
        b = b + 1
    x = x + 20
    if d:
        break
