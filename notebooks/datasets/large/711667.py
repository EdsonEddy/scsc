def suma_digitos(n):
    """ Suma los dígitos del número `n` hasta obtener un solo dígito. """
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def transformar_numero(n, k):
    """ Aplica las transformaciones descritas `k` veces al número `n`. """
    n_str = str(n)
    
    for _ in range(k):
        # Calcula la suma de los dígitos y reduce a un solo dígito
        suma = suma_digitos(int(n_str))
        # Elimina el último dígito
        n_str = n_str[:-1]
        # Inserta la suma al principio
        n_str = str(suma) + n_str
    
    return n_str

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    casos_de_prueba = int(data[0])
    index = 1
    
    resultados = []
    
    for _ in range(casos_de_prueba):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        resultado = transformar_numero(n, k)
        resultados.append(resultado)
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()