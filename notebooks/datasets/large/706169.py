def calcular_resultado(n):
    if n == 1:
        return "1"
    else:
        cubo_n = n ** 3
        cubo_n_menos_1 = (n - 1) ** 3
        return f"{cubo_n_menos_1}+{cubo_n}"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    T = int(data[0])
    resultados = []
    
    for i in range(1, T + 1):
        n = int(data[i])
        resultado = calcular_resultado(n)
        resultados.append(resultado)
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
    