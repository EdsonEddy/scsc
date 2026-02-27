def prime_factors(n):
    factors = []
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    if count > 0:
        factors.append(f"2^{count}" if count > 1 else "2")
    
    factor = 3
    while factor * factor <= n:
        count = 0
        while n % factor == 0:
            count += 1
            n //= factor
        if count > 0:
            factors.append(f"{factor}^{count}" if count > 1 else str(factor))
        factor += 2
    
    if n > 1:
        factors.append(str(n))
    
    return "*".join(factors)

def main():
    while True:
        try:
            num = int(input())
            if num == -1:
                break
            print(f"{num} = {prime_factors(num)}")
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
