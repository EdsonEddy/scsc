for _ in range(int(input())):
    n = input()
    m = int(n) % 7
    r = []
    while int(n) > 81:
        x, y = n[:-1], n[-1]
        r.append(f"({x}, {y})")
        n = str(int(x) + int(y)*5)
    f = int(n)
    print("".join(r) + f" {f} {'correcto' if f%7==m else 'incorrecto'}")    