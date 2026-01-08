def esPrimo(n):
    for i in l:
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True
l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
for i in range(31, 100, 2):
    if esPrimo(i):
        l.append(i)
n = int(input())
for x in range(n):
    k = int(input())
    for i in range(k):
        num = k * (2 ** i) + 1
        if esPrimo(num):
            print(num)
            break