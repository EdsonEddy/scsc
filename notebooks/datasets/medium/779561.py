fib = [1, 2]

while fib[-1] <= 10**12:

    fib.append(fib[-1] + fib[-2])

try:

    while True:
    
        n = int(input())
        
        i = len(fib) - 1
        
        while fib[i] > n:
        
            i -= 1
        
        out = []
        
        for j in range(i, -1, -1):
        
            if fib[j] <= n:
            
                out.append('1')
                
                n -= fib[j]
            
            else:
            
                out.append('0')
        
        print(''.join(out))

except EOFError:

    pass