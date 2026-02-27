def sucesion(n):
    if n==1:
        return "1"
    else:
        cuboanterior=(n-1)**3
        cuboactual=n**3
        return f"{cuboanterior}+{cuboactual}"
casos=int(input())
for _ in range(casos):
    n=int(input())
    print(sucesion(n))