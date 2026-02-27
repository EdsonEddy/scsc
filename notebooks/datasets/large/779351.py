t = int(input())
for _ in range(t):
    n = int(input())
    r0 = n % 7
    pasos = ""
    while n > 81:
        x, y = divmod(n, 10)
        n = x + y * 5
        pasos += f"({x}, {y})"
    r1 = n % 7
    estado = "correcto" if r0 == r1 else "incorrecto"
    print(f"{pasos} {n} {estado}")