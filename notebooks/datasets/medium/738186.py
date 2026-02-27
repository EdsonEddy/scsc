def digit_root(n):
    return 9 if n % 9 == 0 and n != 0 else n % 9

n = int(input())
for _ in range(n):
    x, k = map(int, input().split())
    resultado = digit_root(pow(x, k))
    print(resultado)
