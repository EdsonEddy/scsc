t = int(input())
for _ in range(t):
    n = input().strip()
    original = int(n)
    steps = ""
    
    while True:
        if len(n) == 1:
            result = int(n)
            break
        x = int(n[:-1])
        y = int(n[-1])
        steps += f"({x}, {y})"
        n = str(x + y * 5)
        if int(n) <= 81:
            result = int(n)
            break

    mod_original = original % 7
    mod_result = result % 7
    steps += f" {result}"
    if mod_result == mod_original:
        steps += " correcto"
    else:
        steps += " incorrecto"
    print(steps)
