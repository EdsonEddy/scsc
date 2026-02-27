def sieve(max_num):
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

def factorize(n, primes):
    factors = {}
    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n = n // p
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def format_factors(factors):
    parts = []
    for prime in sorted(factors.keys()):
        exp = factors[prime]
        if exp == 1:
            parts.append(str(prime))
        else:
            parts.append(f"{prime}^{exp}")
    return '*'.join(parts)

primes = sieve(10**6)
numbers = []
while True:
    num = int(input())
    if num == -1:
        break
    numbers.append(num)

for num in numbers:
    if num == 1:
        print(f"1 = 1")
        continue
    factors = factorize(num, primes)
    formatted = format_factors(factors)
    print(f"{num} = {formatted}")