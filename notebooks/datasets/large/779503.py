def metodo_divisible_por_7(n):
    original_residuo = n % 7
    pasos = []
    
    while n > 81:
        ult = n % 10
        resto = n // 10
        pasos.append(f"({resto}, {ult})")
        n = resto + ult * 5

    resultado_final = n
    veredicto = "correcto" if resultado_final % 7 == original_residuo else "incorrecto"
    return ''.join(pasos) + f" {resultado_final} {veredicto}"

t = int(input())
for _ in range(t):
    n = int(input())
    print(metodo_divisible_por_7(n))