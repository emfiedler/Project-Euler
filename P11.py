a = [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8]
b = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0]
c = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65]
d = [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91]
e = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
f = [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
g = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
h = [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
i = [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
j = [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95]
k = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92]
l = [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57]
m = [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
n = [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40]
o = [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
p = [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
q = [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
r = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16]
s = [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54]
t = [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]

Dr = []
Hr = []
for wi in range(0,17):
    xi = wi + 1
    yi = xi + 1
    zi = yi + 1
    #Diagonal right
    Dr.append(a[wi]*b[xi]*c[yi]*d[zi])
    Dr.append(b[wi]*c[xi]*d[yi]*e[zi])
    Dr.append(c[wi]*d[xi]*e[yi]*f[zi])
    Dr.append(d[wi]*e[xi]*f[yi]*g[zi])
    Dr.append(e[wi]*f[xi]*g[yi]*h[zi])
    Dr.append(f[wi]*g[xi]*h[yi]*i[zi])
    Dr.append(g[wi]*h[xi]*i[yi]*j[zi])
    Dr.append(h[wi]*i[xi]*j[yi]*k[zi])
    Dr.append(i[wi]*j[xi]*k[yi]*l[zi])
    Dr.append(j[wi]*k[xi]*l[yi]*m[zi])
    Dr.append(k[wi]*l[xi]*m[yi]*n[zi])
    Dr.append(l[wi]*m[xi]*n[yi]*o[zi])
    Dr.append(m[wi]*n[xi]*o[yi]*p[zi])
    Dr.append(n[wi]*o[xi]*p[yi]*q[zi])
    Dr.append(o[wi]*p[xi]*q[yi]*r[zi])
    Dr.append(p[wi]*q[xi]*r[yi]*s[zi])
    Dr.append(q[wi]*r[xi]*s[yi]*t[zi])
    #Horizontal
    Hr.append(a[wi]*a[xi]*a[yi]*a[zi])
    Hr.append(b[wi]*b[xi]*b[yi]*b[zi])
    Hr.append(c[wi]*c[xi]*c[yi]*c[zi])
    Hr.append(d[wi]*d[xi]*d[yi]*d[zi])
    Hr.append(e[wi]*e[xi]*e[yi]*e[zi])
    Hr.append(f[wi]*f[xi]*f[yi]*f[zi])
    Hr.append(g[wi]*g[xi]*g[yi]*g[zi])
    Hr.append(h[wi]*h[xi]*h[yi]*h[zi])
    Hr.append(i[wi]*i[xi]*i[yi]*i[zi])
    Hr.append(j[wi]*j[xi]*j[yi]*j[zi])
    Hr.append(k[wi]*k[xi]*k[yi]*k[zi])
    Hr.append(l[wi]*l[xi]*l[yi]*l[zi])
    Hr.append(m[wi]*m[xi]*m[yi]*m[zi])
    Hr.append(n[wi]*n[xi]*n[yi]*n[zi])
    Hr.append(o[wi]*o[xi]*o[yi]*o[zi])
    Hr.append(p[wi]*p[xi]*p[yi]*p[zi])
    Hr.append(q[wi]*q[xi]*q[yi]*q[zi])
    Hr.append(r[wi]*r[xi]*r[yi]*r[zi])
    Hr.append(s[wi]*s[xi]*s[yi]*s[zi])
    Hr.append(t[wi]*t[xi]*t[yi]*t[zi])

Vr = []
for wj in range(0,20):
    xj = yj = zj = wj
    Vr.append(a[wj]*b[xj]*c[yj]*d[zj])
    Vr.append(b[wj]*c[xj]*d[yj]*e[zj])
    Vr.append(c[wj]*d[xj]*e[yj]*f[zj])
    Vr.append(d[wj]*e[xj]*f[yj]*g[zj])
    Vr.append(e[wj]*f[xj]*g[yj]*h[zj])
    Vr.append(f[wj]*g[xj]*h[yj]*i[zj])
    Vr.append(g[wj]*h[xj]*i[yj]*j[zj])
    Vr.append(h[wj]*i[xj]*j[yj]*k[zj])
    Vr.append(i[wj]*j[xj]*k[yj]*l[zj])
    Vr.append(j[wj]*k[xj]*l[yj]*m[zj])
    Vr.append(k[wj]*l[xj]*m[yj]*n[zj])
    Vr.append(l[wj]*m[xj]*n[yj]*o[zj])
    Vr.append(m[wj]*n[xj]*o[yj]*p[zj])
    Vr.append(n[wj]*o[xj]*p[yj]*q[zj])
    Vr.append(o[wj]*p[xj]*q[yj]*r[zj])
    Vr.append(p[wj]*q[xj]*r[yj]*s[zj])
    Vr.append(q[wj]*r[xj]*s[yj]*t[zj])

Dl = []
for wk in range(3, 20):
    xk = wk - 1
    yk = xk - 1
    zk = yk - 1
    Dl.append(a[wk]*b[xk]*c[yk]*d[zk])
    Dl.append(b[wk]*c[xk]*d[yk]*e[zk])
    Dl.append(c[wk]*d[xk]*e[yk]*f[zk])
    Dl.append(d[wk]*e[xk]*f[yk]*g[zk])
    Dl.append(e[wk]*f[xk]*g[yk]*h[zk])
    Dl.append(f[wk]*g[xk]*h[yk]*i[zk])
    Dl.append(g[wk]*h[xk]*i[yk]*j[zk])
    Dl.append(h[wk]*i[xk]*j[yk]*k[zk])
    Dl.append(i[wk]*j[xk]*k[yk]*l[zk])
    Dl.append(j[wk]*k[xk]*l[yk]*m[zk])
    Dl.append(k[wk]*l[xk]*m[yk]*n[zk])
    Dl.append(l[wk]*m[xk]*n[yk]*o[zk])
    Dl.append(m[wk]*n[xk]*o[yk]*p[zk])
    Dl.append(n[wk]*o[xk]*p[yk]*q[zk])
    Dl.append(o[wk]*p[xk]*q[yk]*r[zk])
    Dl.append(p[wk]*q[xk]*r[yk]*s[zk])
    Dl.append(q[wk]*r[xk]*s[yk]*t[zk])
    

print("Diagonal right\t", max(Dr))
print("Horizontal\t", max(Hr))
print("Vertical\t", max(Vr))
print("Diagonal left\t", max(Dl))
