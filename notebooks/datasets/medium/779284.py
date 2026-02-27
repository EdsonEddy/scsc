fib = [1, 2]
while fib[-1] <= 10**12:
    fib.append(fib[-1] + fib[-2])
while True:
    try:
        m = int(input()) 
    except EOFError:
        break 
    r = ""
    for i in range(len(fib) - 1, -1, -1): 
        if fib[i] <= m:
            r += "1"
            m -= fib[i]
        else:
            r += "0"
    print(r.lstrip('0'))