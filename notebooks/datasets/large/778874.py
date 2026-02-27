t = int(input())  
for i in range(t):
    n = int(input())
    original = n
    pasos = []
    while n > 81:
        d = n % 10
        r = n // 10
        pasos.append(f"({r}, {d})")
        n = r + d * 5

    r = "correcto" if n % 7 == original % 7 else "incorrecto"
    print(''.join(pasos) + f" {n} {r}")
