# Función para calcular la suma de los dígitos de un número
def suma_digitos(n):
    return sum(int(digito) for digito in str(n))

# Función para resolver usando módulo 9
def exponencial():
    t = int(input())
    
    for _ in range(t):
        x, k = map(int, input().split())

        if x == 0:
            result = 0
        else:
            mod_result = pow(x, k, 9)
            
            result = mod_result if mod_result != 0 else 9
        
        print(result)


exponencial()
