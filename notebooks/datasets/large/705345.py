def encontrandoSig(n):
    if n > 1:
        return f"{(n-1)**3}+{n**3}"
    return 1
    
for _ in range(int(input())):
    print(encontrandoSig(int(input())))