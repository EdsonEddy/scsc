import sys
def potencia_modular(base, exponente, mod):
    resultado = 1
    base = base % mod
    while exponente > 0:
        if exponente % 2 == 1: 
            resultado = (resultado * base) % mod
        base = (base * base) % mod 
        exponente //= 2
    return resultado
def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        x, k = map(int, sys.stdin.readline().split())
        resultado_mod = potencia_modular(x, k, 9)
        if resultado_mod == 0:
            resultado_mod = 9
        sys.stdout.write(str(resultado_mod) + "\n")

if __name__ == "__main__":
    main()
