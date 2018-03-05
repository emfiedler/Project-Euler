def ch(n):
    c = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        c += 1
    return c

cc = [0]
mx = []

for n in range(1, 1000000):
    if ch(n) > max(cc):
        mx.append(n)
        cc.append(ch(n))


print("Longest chain produced by %d, with a length of %d" % (mx[-1], cc[-1]))
