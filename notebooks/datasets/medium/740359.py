def sumaRecursiva(i, dig):
    if i > 201 or len(dig)==1:
        return dig
    else:
        s = 0
        for j in dig:
            s += int(j)
        # print(s)
        return sumaRecursiva(i+1, str(s))

import sys
sys.set_int_max_str_digits(0)
casos = int(input())
for _ in range(casos):
    x, k = map(int, input().split())
    dig = str(x**k)
    print(sumaRecursiva(1, dig))
# x = 2019
# k = 2019
# dig = str(x**k)
# print(sumaRecursiva(1, dig))