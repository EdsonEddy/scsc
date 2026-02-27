fib = [1, 2]
while fib[-1] + fib[-2] <= 10**12:
    fib.append(fib[-1] + fib[-2])

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if not line:
        continue

    n = int(line)
    rem = n
    bits = []
    started = False

    for f in reversed(fib):
        if f <= rem:
            bits.append('1')
            rem -= f
            started = True
        elif started:
            bits.append('0')

    if not bits:
        bits = ['0']
    print(''.join(bits))
