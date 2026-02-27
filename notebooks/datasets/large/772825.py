T = int(input())  
for _ in range(T):
    n = int(input()) 
    if n == 1:
        print("1") 
    else:
        sum1 = (n - 1) ** 3  
        sum2 = n ** 3 
        print(f"{sum1}+{sum2}") 