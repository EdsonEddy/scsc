a = int(input())
for x in range(a):
    e = 0
    k = int(input())
    x = 0
    m = k * (2**e) + 1    
    t = 1
    if (m > 10**4):
        print("-1")
    else:
        while (m < 10**4):
            while (t <= m):
                dig = m % t
                if (dig == 0): 
                    x = x + 1
                    t = t + 1
                else:
                    t = t + 1
            if (x == 2):
                print(m)
                break
            else:
                x = 0
                t = 1
                e = e + 1
                m = k * (2**e) + 1
        if (m > 10**4):
            print("-1")