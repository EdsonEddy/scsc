def reduccion_digital(n):
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

for _ in range(int(input())):
    x, k = map(int, input().split())
    resultado = reduccion_digital(reduccion_digital(x) ** k)
    print(resultado)
