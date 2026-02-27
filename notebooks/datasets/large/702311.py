def determinar_paridad(n):
    if n % 4 == 0:
        return "Par"
    elif n % 4 == 1:
        return "Cualquiera"
    elif n % 4 == 2:
        return "Impar"
    else:
        return "Cualquiera"

def main():
    num_casos = int(input())
    for _ in range(num_casos):
        n = int(input())
        resultado = determinar_paridad(n)
        print(resultado)

if __name__ == "__main__":
    main()