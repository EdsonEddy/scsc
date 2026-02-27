def div7(n):
    original_resto, terminos = n % 7, []
    while n > 81:
        ultimoDig = n % 10
        primerosDig = n // 10
        newNumero = primerosDig + 5 * ultimoDig
        terminos.append(f"({primerosDig}, {ultimoDig})")
        n = newNumero
    terminos.append(" " + str(n))
    resultado_resto = n % 7
    if resultado_resto == original_resto:
        terminos.append(" correcto")
    else:
        terminos.append(" incorrecto")
    return "".join(terminos)
import sys
for i in sys.stdin:
    n = int(i)
    for j in range(n):
        x = int(input())
        print(div7(x))