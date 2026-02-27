serieM = [0] * 101

for i in range(1, 101):
    serieM[i] = serieM[i - 1] + i

for _ in range(int(input())):
    n = int(input())
    par = 2
    impar = 1
    resp = n * par + serieM[n - 1]
    resi = n * impar + serieM[n - 1]
    
    if resp % 2 == 0 and resi % 2 == 0:
        print("Par")
    elif resp % 2 != 0 and resi % 2 != 0:
        print("Impar")
    else:
        print("Cualquiera")
