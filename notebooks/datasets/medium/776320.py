def factores(n):
    d, f = 2, {}
    while d*d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1: f[n] = 1
    return f
while True:
    n = int(input())
    if n == -1: break
    print(f"{n} = ", end="")
    print("*".join(f"{p}^{e}" if e>1 else str(p) for p, e in sorted(factores(n).items())))

