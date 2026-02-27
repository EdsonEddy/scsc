cantidad = int(input())
for i in range(cantidad):
    n = int(input())

    if n == 1:
        print(1)
    else:
        primer_numero = (n-1)**3
        segundo_numero = n**3
        print(f"{primer_numero}+{segundo_numero}")