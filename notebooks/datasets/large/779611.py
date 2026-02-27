t = int(input())
for _ in range(t):
    n = int(input())
    original_mod = n % 7
    current = n
    pairs = []
    while current > 81:
        ult = current % 10
        resto = current // 10
        pairs.append((resto, ult))
        current = resto + ult * 5
    resultado = current
    estado = "correcto" if resultado % 7 == original_mod else "incorrecto"
    pares_str = "".join(f"({r}, {u})" for r, u in pairs)
    print(f"{pares_str} {resultado} {estado}")