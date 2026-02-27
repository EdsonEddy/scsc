def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    pos = 1
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        original = n
        pairs = ""
        while True:
            first = n // 10
            last = n % 10
            pairs += f"({first}, {last})"
            n = first + last * 5
            if n <= 81:
                break
        final_result = n
        if (original % 7) == (final_result % 7):
            verdict = "correcto"
        else:
            verdict = "incorrecto"
        print(f"{pairs} {final_result} {verdict}")

if __name__ == '__main__':
    main()
