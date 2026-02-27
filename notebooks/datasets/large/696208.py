import math

def redondeo(num):
    d = 2
    fac = 10 ** d
    num *= fac
    if num - math.floor(num) == 0.5:
        r = math.ceil(num)
    elif num - math.floor(num) == -0.5:
        r = math.floor(num)
    else:
        r = round(num)
    return r / fac

def encontrar(cadm):
    tam = len(cadm)
    ac = 0
    ec = 0
    ic = 0
    oc = 0
    uc = 0
    for k in range(tam):
        if cadm[k] == 'a': ac += 1
        if cadm[k] == 'e': ec += 1
        if cadm[k] == 'i': ic += 1
        if cadm[k] == 'o': oc += 1
        if cadm[k] == 'u': uc += 1
    a = redondeo((ac / tam) * 100)
    e = redondeo((ec / tam) * 100)
    i = redondeo((ic / tam) * 100)
    o = redondeo((oc / tam) * 100)
    u = redondeo((uc / tam) * 100)
    return a, e, i, o, u

T = int(input())
for i in range(1, T + 1):
    cad = input()
    cadm = cad.lower()
    A, E, I, O, U = encontrar(cadm)
    print("Caso {}:".format(i))
    print("a= {:.2f}".format(A))
    print("e= {:.2f}".format(E))
    print("i= {:.2f}".format(I))
    print("o= {:.2f}".format(O))
    print("u= {:.2f}".format(U))
    