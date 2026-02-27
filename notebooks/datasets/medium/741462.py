def suma_digitos(n):
    """Función que devuelve la suma de los dígitos de n."""
    return sum(int(digit) for digit in str(n))

def suma_modular(x, k):
    """Calcula x^k mod 9 usando la propiedad de los dígitos."""
    if x == 0:
        return 0
    if x % 9 == 0:
        return 9

    # Calcular x mod 9
    x_mod = x % 9
    # Aplicar la propiedad de potencias
    if k == 0:
        return 1  # Cualquier número a la potencia 0 es 1

    resultado = 1
    for _ in range(k):
        resultado = (resultado * x_mod) % 9

    return 9 if resultado == 0 else resultado

def suma_recursiva(x, k):
    """Calcula a201 a partir de x y k."""
    # Calcula a1 = s(x^k)
    a1 = suma_modular(x, k)
    # Calcula a2 = s(a1)
    a2 = suma_digitos(a1)
    # Calcula a3 = s(a2)
    a3 = suma_digitos(a2)

    return 9 if a3 > 9 else a3

def main():
    n = int(input())
    resultados = []

    for _ in range(n):
        x, k = map(int, input().split())
        resultado = suma_recursiva(x, k)
        resultados.append(resultado)

    # Mostrar resultados
    for resultado in resultados:
        print(resultado)

# supiiro
if __name__ == "__main__":
    main()
