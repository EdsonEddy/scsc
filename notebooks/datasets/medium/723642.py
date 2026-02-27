import sys
def power(a, b):
    ans = 1
    while b > 0:
         
        if b % 2 == 1:
            ans *= a
             
        a *= a
        b //= 2
 
    return ans
def suma(x):
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10
    return ans
t = int(sys.stdin.readline())
for i in range(t):
    x, k = map(int, sys.stdin.readline().split())
    ans = power(x, k)
    ans = ans % 9
    if ans == 0:
        ans = 9
    sys.stdout.write( str(ans) + "\n")