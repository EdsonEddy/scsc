def sumar_digitos(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def proceso_n_veces(n, k):
    for _ in range(k):
        # Paso 1: Sumar los dígitos hasta tener un solo dígito
        suma_digitos = sumar_digitos(n)
        
        # Paso 2: Eliminar el último dígito de n
        n = n // 10
        
        # Paso 3: Insertar la suma al principio
        n = int(str(suma_digitos) + str(n))
    
    return n

def main():
    # Leer el número de casos de prueba
    casos = int(input().strip())
    
    for _ in range(casos):
        # Leer los valores de n y k
        n, k = map(int, input().strip().split())
        
        # Ejecutar el proceso k veces y obtener el resultado final
        resultado = proceso_n_veces(n, k)
        
        # Imprimir el resultado
        print(resultado)

# Llamar a la función principal
if __name__ == "__main__":
    main()
