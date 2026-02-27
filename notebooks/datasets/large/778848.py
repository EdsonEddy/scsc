def aplicar_metodo_divisibilidad(n):
    pasos = []
    while n > 81:
        ult_dig = n % 10
        resto = n // 10
        pasos.append((resto, ult_dig))
        n = resto + ult_dig * 5
    return pasos, n

def verificar_divisibilidad(original, resultado_final):
    return (original % 7) == (resultado_final % 7)

def procesar_caso(n):
    pasos, resultado = aplicar_metodo_divisibilidad(n)
    es_correcto = verificar_divisibilidad(n, resultado)
    salida = ''.join(f"({a}, {b})" for a, b in pasos)
    salida += f" {resultado} {'correcto' if es_correcto else 'incorrecto'}"
    return salida

def procesar_entrada():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(procesar_caso(n))

if __name__ == "__main__":
    procesar_entrada()
