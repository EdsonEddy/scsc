import sys
import math

def prime_factors(n):
    if n == 1:
        return [(1, 1)]

    factors = []
    
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    if count > 0:
        factors.append((2, count))
        
    p = 3
    while p * p <= n:
        count = 0
        while n % p == 0:
            count += 1
            n //= p
        if count > 0:
            factors.append((p, count))
        p += 2
        
    if n > 1:
        factors.append((n, 1))
    return factors

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        num = int(line)
        if num == -1:
            break
        
        factors = prime_factors(num)
        
        factor_strs = []
        for prime, exp in factors:
            if exp == 1:
                factor_strs.append(str(prime))
            else:
                factor_strs.append(f"{prime}^{exp}")
        
        print(f"{num} = " + "*".join(factor_strs))

if __name__ == "__main__":
    main()
