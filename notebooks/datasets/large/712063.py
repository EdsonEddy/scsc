def suma_digitos(n):
    while n >= 10:
        n = sum(int(digito) for digito in str(n))
    return n

def procesar_caso(n, k):
    n_str = str(n)
    for _ in range(k):
        suma = suma_digitos(sum(int(digito) for digito in n_str))
        n_str = str(suma) + n_str[:-1]
    return n_str

def main():
    # Leer la cantidad de casos de prueba
    casos = int(input())
    
    resultados = []
    
    for _ in range(casos):
        # Leer cada caso de prueba
        n, k = map(int, input().split())
        resultado = procesar_caso(n, k)
        resultados.append(resultado)
    
    # Imprimir los resultados
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
