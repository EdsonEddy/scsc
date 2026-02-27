import math

def red(n):
    return math.floor(n * 100 + 0.5) / 100

T = int(input())

for S in range(T):
    fruta = input().lower()
    a = fruta.count("a")
    e = fruta.count("e")
    i = fruta.count("i")
    o = fruta.count("o")
    u = fruta.count("u")
    total = len(fruta) - fruta.count(" ")
    print("Caso {0}:".format(S + 1))
    print("a=", "{0:.2f}".format(red((a * 100) / total)))
    print("e=", "{0:.2f}".format(red((e * 100) / total)))
    print("i=", "{0:.2f}".format(red((i * 100) / total)))
    print("o=", "{0:.2f}".format(red((o * 100) / total)))
    print("u=", "{0:.2f}".format(red((u * 100) / total)))