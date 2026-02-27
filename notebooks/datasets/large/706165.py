def cubos_sucesion(n):
    cubo=n**3
    cubo_anterior= (n-1)**3
    if cubo_anterior == 0:
        return f"{cubo}"
    else:
        return f"{cubo_anterior}+{cubo}"
t = int(input())
for _ in range (t):
    n=int(input())
    print(cubos_sucesion(n))