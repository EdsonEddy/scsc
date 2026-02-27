for _ in range(int(input())):
    n = int(input())
    pares = []
    while n > 81:
        ultimo_digito = n % 10
        n //= 10
        multiplicacion = ultimo_digito * 5
        primeros_digitos = n 
        suma = primeros_digitos + multiplicacion       
        pares.append((primeros_digitos, ultimo_digito)) 
        n = suma

    if n % 7 == 0:
        resultado = "correcto"
    else:
        resultado = "incorrecto"
    salida = ''.join([f"({par[0]}, {par[1]})" for par in pares]) + f" {n} {resultado}"
    print(salida)