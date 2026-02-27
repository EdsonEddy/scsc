def fibonacci_representation(n):
    fib = [1, 2]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    fib.pop()
    
    representation = []
    for num in reversed(fib):
        if n >= num:
            representation.append('1')
            n -= num
        else:
            representation.append('0')
    
    return ''.join(representation).lstrip('0') or '0'

while True:
    try:
        n = int(input())
        print(fibonacci_representation(n))
    except:
        break