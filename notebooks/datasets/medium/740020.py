def digito_raiz_mod(x, k):
    return 9 if pow(x, k, 9) == 0 else pow(x, k, 9)

def main():
    for _ in range(int(input())):
        x, k = map(int, input().split())
        print(digito_raiz_mod(x, k))

if __name__ == "__main__":
    main()
