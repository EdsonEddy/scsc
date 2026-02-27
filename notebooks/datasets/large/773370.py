import sys
casos = int(sys.stdin.readline().strip())
for _ in range(casos):
    indice = int(sys.stdin.readline().strip())
    if indice == 1:
        print("1")
    else:
        print(f"{(indice-1)**3}+{indice**3}")