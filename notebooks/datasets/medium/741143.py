def soma_dejetos(n):
    return sum(int(d) for d in str(n))
def repete(n):
    if n == 0:
        return 0
    else:
        return 1 + (n - 1) % 9

def imp(algo):
    print(algo)
n = int(input())
for _ in range(n):
    x, k = map(int, input().split())
    h = x ** k
    resultado = repete(h)
    imp(resultado)