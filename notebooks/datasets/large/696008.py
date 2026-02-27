def round_fix(number):
    rounded = number * 100
    rounded = int(rounded + 0.5)
    return rounded / 100


T = int(input())
for k in range(1, T + 1):
    text = input()
    total = len(text)
    a, e, i, o, u = 0, 0, 0, 0, 0
    for char in text:
        if char == "a":
            a += 1
        elif char == "e":
            e += 1
        elif char == "i":
            i += 1
        elif char == "o":
            o += 1
        elif char == "u":
            u += 1

    print(f"Caso {k}:")
    print(f"a= {round_fix(a * 100 / total):.2f}")
    print(f"e= {round_fix(e * 100 / total):.2f}")
    print(f"i= {round_fix(i * 100 / total):.2f}")
    print(f"o= {round_fix(o * 100 / total):.2f}")
    print(f"u= {round_fix(u * 100 / total):.2f}")