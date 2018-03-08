num = 10000

def div(n):
    s = 0
    for y in range(1, n + 1):
        if n % y == 0 and n != y:
            s += y

    return s

z = []
for x in range(1, num + 1):
    dv = div(x)
    pv = div(dv)
    if x == div(dv) and dv != x:
        print(x)
        z.append(x)

print(sum(z))
