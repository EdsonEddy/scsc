def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def maxprimos(k):
    maxcount = 0
    count = 0
    for n in range(1, 501):
        valor = n**2 - n + k
        if primo(valor):
            count += 1
            if count > maxcount:
                maxcount = count
        else:
            count = 0
    return maxcount

casos = int(input())
constantes = [int(input()) for _ in range(casos)]

for k in constantes:
    print(f"{k}: {maxprimos(k)}")