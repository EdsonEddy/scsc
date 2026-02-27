def sumar_digitos(numero):
    """Suma los dígitos del número y reduce a un solo dígito si es necesario."""
    while numero >= 10:
        numero = sum(int(digit) for digit in str(numero))
    return numero

def procesar_caso(n, k):
    """Procesa el caso dado n y k siguiendo las reglas especificadas."""
    n = str(n)
    for _ in range(k):
        suma_digitos = sumar_digitos(int(n))
        n = n[:-1]  # Elimina el último dígito
        n = str(suma_digitos) + n  # Inserta la suma al principio
    return n

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    numero_casos = int(data[0])
    index = 1
    resultados = []
    
    for _ in range(numero_casos):
        n = int(data[index])
        k = int(data[index + 1])
        resultado = procesar_caso(n, k)
        resultados.append(resultado)
        index += 2
    
    for resultado in resultados:
        print(resultado)

# Llamar a main si el script se ejecuta directamente
if __name__ == "__main__":
    main()
