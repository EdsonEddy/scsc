def LP(lim):
    l = [True] * (lim + 1)
    l[0] = l[1] = False
    r = []
    for i in range(2, int(lim**0.5) + 1):
        if l[i]:
            r.append(i)
            for j in range(i * i, lim + 1, i):
                l[j] = False
    r.extend([x for x in range(int(lim**0.5) + 1, lim + 1) if l[x]])
    return r
def factorizar(lp, i):
    j = 0
    l = []
    while i != 1:
        if i % lp[j] == 0:
            l.append(lp[j])
            i //= lp[j]
        else:
            j += 1
    return l
def exp(r):
    cad = ""
    s = sorted(set(r))
    for i in s:
        c = r.count(i)
        if c > 1:
            cad += f"{i}^{c}*"
        else:
            cad += f"{i}*"
    return cad[:-1]
l = []
n = int(input())
while n != -1:
    l.append(n)
    n = int(input())
lim = max(l)
lp = LP(lim)
for i in l:
    r = factorizar(lp, i)
    e = exp(r)
    print(f"{i} = {e}")
