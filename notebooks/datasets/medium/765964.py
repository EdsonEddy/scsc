def factores_primos(n):
    factores = []
    factor = 2
    
    while factor * factor <= n:
        if n % factor == 0:
            count = 0
            while n % factor == 0:
                count += 1
                n //= factor
            if count > 1:
                factores.append(f"{factor}^{count}")
            else:
                factores.append(str(factor))
        factor += 1 if factor == 2 else 2  
    
    if n > 1:
        factores.append(str(n))
    
    return '*'.join(factores)
while True:
    n = int(input())
    if n == -1:
        break
    print(f"{n} = {factores_primos(n)}")
