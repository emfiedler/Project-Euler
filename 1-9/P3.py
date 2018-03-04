#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


x = 100
a = []

while x < 999:
    y = 100
    while y < 999:
        z = y * x
        y = y + 1
        s = str(z)
        if s[::1] == s[::-1]:
            i = int(s)
            a.append(i)
    x = x + 1

print(max(a))
