def calcular_suma(n):
    suma_anterior = 1  # Iniciamos con la primera suma
    cubo_anterior = 1  # El primer cubo es 1 (1^3)

    for i in range(1, n):
        cubo_actual = (i + 1) ** 3  # Calculamos el siguiente cubo
        suma_anterior = cubo_anterior  # La suma anterior es el cubo del paso anterior
        cubo_anterior = cubo_actual  # Actualizamos el cubo anterior

    return suma_anterior, cubo_anterior

def main():
    T = int(input())  # Número de casos de prueba

    for _ in range(T):
        n = int(input())
        suma1, suma2 = calcular_suma(n)
        if n == 1:
            print(suma1)
        else:
            print(f"{suma1}+{suma2}")

if __name__ == "__main__":
    main()
