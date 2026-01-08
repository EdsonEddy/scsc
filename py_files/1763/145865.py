def esPrimo(n):
    if n in primos:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    else:
        primos.append(n)
        return True
casos = int(input())
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
for i in range(casos):
    k = int(input())
    if 1 <= k <= 1000 :
        n = 0
        while True:
            N = k * 2**n + 1
            if esPrimo(N):
                print(N)
                break
            n += 1
            if N > 10**4:
                print(-1)
                break