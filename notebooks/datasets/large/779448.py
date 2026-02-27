t = int(input())
for _ in range(t):
    n = int(input())
    original_mod = n % 7
    pasos = []
    while n > 81:
        ult = n % 10
        resto = n // 10
        pasos.append(f"({resto}, {ult})")
        n = resto + ult * 5
    resultado = n
    estado = "correcto" if resultado % 7 == original_mod else "incorrecto"
    print(''.join(pasos) + f" {resultado} {estado}")