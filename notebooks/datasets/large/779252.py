t = int(input())
for _ in range(t):
    n = int(input())
    r = n % 7 
    p = "" 
    while n > 81:
        ld = n % 10
        s = n // 10
        n = s + (ld * 5)
        p += f"({s}, {ld})"
    r = "correcto" if n % 7 == r else "incorrecto"
    print(p, n, r)