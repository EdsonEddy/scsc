def sumd(n):
    while n >= 10:
        n = sum(map(int, str(n)))
    return n
def procesar_numero(n, k):
    for _ in range(k):
        suma = sumd(n)
        n //= 10
        n = int(str(suma) + str(n))
    return n
def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        resultado = procesar_numero(n, k)
        print(resultado)

if __name__ == "__main__":
    main()
