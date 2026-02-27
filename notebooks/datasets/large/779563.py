def modu(n):
    res = ''
    while True:
        a, b = n//10, n%10
        res +=f'({a}, {b})'
        c = a+(b*5)
        if c <= 81: break
        n = c
    return res, c

for _ in range(int(input())):
    n = int(input())
    res, c = modu(n)

    print(res, c, 'correcto' if (c%7) == (n%7) else 'incorrecto')