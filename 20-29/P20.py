import math

n = 100

num = math.factorial(n)

strn = str(num)

sm = 0
for i in range(0, len(strn) - 1):
    sm += int(strn[i])

print(sm)
