def fibonacci_base(num):
    fib = [1, 2]
    while fib[-1] <= num:
        fib.append(fib[-1] + fib[-2])
    
    result = []
    for i in range(len(fib) - 1, -1, -1):
        if fib[i] <= num:
            num -= fib[i]
            result.append('1')
        elif result:
            result.append('0')
    
    return ''.join(result)

def main():
    import sys
    input = sys.stdin.read
    numbers = map(int, input().split())

    for num in numbers:
        print(fibonacci_base(num))

if __name__ == "__main__":
    main()