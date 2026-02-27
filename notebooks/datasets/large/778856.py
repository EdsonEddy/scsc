def verificar_divisibilidad_por_7(n):
    original_mod = n % 7
    pasos = []
    while n > 81:
        d = n % 10
        r = n // 10
        pasos.append(f"({r}, {d})")
        n = r + 5 * d

    resultado = "correcto" if n % 7 == original_mod else "incorrecto"
    return "".join(pasos) + f" {n} {resultado}"
t = int(input())
for _ in range(t):
    numero = int(input())
    print(verificar_divisibilidad_por_7(numero))