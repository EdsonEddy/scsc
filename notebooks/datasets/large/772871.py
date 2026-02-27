def calcular_resultado(n):
    return n ** 3
T = int(input())
n_values = [int(input()) for _ in range(T)]
for n in n_values:
    sum_previous = 1
    if n == 1:
        print(1)
    else:
        for i in range(2, n + 1):
            sum_current = calcular_resultado(i)
            if i == n:  
                print(f"{sum_previous}+{sum_current}")
            sum_previous = sum_current
