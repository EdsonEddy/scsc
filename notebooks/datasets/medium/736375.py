import sys

def potencia_modular(base, exponente, mod):
    """Calcula (base^exponente) % mod usando exponenciación rápida."""
    resultado = 1
    base = base % mod  # Reduce la base antes de entrar al bucle
    while exponente > 0:
        if exponente % 2 == 1:  # Si exponente es impar
            resultado = (resultado * base) % mod
        base = (base * base) % mod  # Elevar la base al cuadrado
        exponente //= 2  # Dividir el exponente entre 2
    return resultado

def main():
    # Leer la cantidad de casos
    t = int(sys.stdin.readline())
    for _ in range(t):
        x, k = map(int, sys.stdin.readline().split())
        # Usar potencia_modular para obtener x^k mod 9
        resultado_mod = potencia_modular(x, k, 9)
        # Ajustar el resultado según la raíz digital
        if resultado_mod == 0:
            resultado_mod = 9
        # Imprimir el resultado
        sys.stdout.write(str(resultado_mod) + "\n")

if __name__ == "__main__":
    main()

