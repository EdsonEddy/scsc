T = int(input())
valores = [int(input()) for _ in range(T)]
secuencia = [i**3 for i in range(1, max(valores) + 2)]
for n in valores:
    print(f"{secuencia[n-2]}+{secuencia[n-1]}" if n > 1 else secuencia[0])