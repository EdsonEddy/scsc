def calcular_suma(n):
    if n == 1:
        return "1"
    else:
        termino_anterior = (n-1)**3
        termino_actual = n**3
        return f"{termino_anterior}+{termino_actual}"

def main():
    T = int(input())
    resultados = []
    for _ in range(T):
        n = int(input())
        resultados.append(calcular_suma(n))
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()