casos = int(input())
for _ in range(casos):
    n = input()
    original = int(n)
    original_residuo = original % 7
    salida = ""
    while True:
        ultimo = int(n[-1])
        primeros = int(n[:-1]) if len(n) > 1 else 0
        salida += f"({primeros}, {ultimo})"
        n = str(primeros + ultimo * 5)
        if int(n) <= 81:
            break
    resultado = int(n)
    if resultado % 7 == original_residuo:
        salida += f" {resultado} correcto"
    else:
        salida += f" {resultado} incorrecto"
    print(salida)