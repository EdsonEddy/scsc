def factorizar(n):
    factores = []
    divisor = 2

    while divisor * divisor <= n:
        exponente = 0
        while n % divisor == 0:
            n //= divisor
            exponente += 1
        if exponente > 0:
            if exponente == 1:
                factores.append(f"{divisor}")
            else:
                factores.append(f"{divisor}^{exponente}")
        divisor += 1

    if n > 1:
        factores.append(f"{n}")  # n es primo

    return '*'.join(factores)

def main():
    while True:
        try:
            entrada = input().strip()
            if entrada == '':
                continue
            n = int(entrada)
            if n == -1:
                break
            print(f"{n} = {factorizar(n)}")
        except EOFError:
            break

if __name__ == "__main__":
    main()
