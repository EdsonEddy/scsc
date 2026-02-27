def fibonacci_up_to(limit):
    fib = [1, 2]  
    while True:
        next_fib = fib[-1] + fib[-2]
        if next_fib > limit:
            break
        fib.append(next_fib)
    return fib

def to_fibonacci_base(n):
    fib = fibonacci_up_to(n)
    result = []
    
    for f in reversed(fib):
        if f <= n:
            result.append('1')
            n -= f
        elif result: 
            result.append('0')
    
    return ''.join(result)

def main():
    while True:
        try:
            n = int(input())
            print(to_fibonacci_base(n))
        except EOFError:
            break  

if __name__ == "__main__":
    main()