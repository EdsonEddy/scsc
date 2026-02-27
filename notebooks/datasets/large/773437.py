import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    
    pl = int(sys.stdin.readline().strip())
    
    if pl == 1:
        
        print("1")
    
    else:

        print(f"{(pl-1)**3}+{pl**3}")