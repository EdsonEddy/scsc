def procesar_numero(n):
    pasos = []
    original_mod = n % 7  
    while n > 81:
        ult = n % 10  
        resto = n // 10 
        pasos.append(f"({resto}, {ult})")
        n = resto + ult * 5  

    final_mod = n % 7
    resultado = "correcto" if final_mod == original_mod else "incorrecto"
    return ''.join(pasos) + f" {n} {resultado}"

t = int(input())
for _ in range(t):
    numero = int(input())
    print(procesar_numero(numero))
