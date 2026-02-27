def calcular_sucesion(n):
    if n == 1:
        return "1"
    else:
        primer_numero = (n - 1)**3
        segundo_numero = n**3
        return f"{primer_numero}+{segundo_numero}"
def main():
    T = int(input())
    resultados = []
    for _ in range(T):
        n = int(input())
        resultados.append(calcular_sucesion(n))
    for resultado in resultados:
        print(resultado)
main()