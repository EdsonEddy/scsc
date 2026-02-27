def raiz_digital(n):
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

def main():
    t = int(input())
    
    for _ in range(t):
        x, k = map(int, input().split())
        raiz_x = raiz_digital(x)
        resultado = raiz_digital(raiz_x ** k)
        print(resultado)

if __name__ == "__main__":
    main()
