from decimal import Decimal, ROUND_HALF_UP

# redondeo estilo Java/C
def round_java(x, decimales):
    return float(Decimal(str(x)).quantize(Decimal('1.' + '0'*decimales), rounding=ROUND_HALF_UP))

t = int(input())
for k in range(t):   
    s = input()
    arr = [0] * 26   
    for i in range(len(s)):
        idx = ord(s[i]) - ord('a')  
        arr[idx] += 1
    a=(arr[0]/len(s))*100
    e=(arr[4]/len(s))*100
    i=(arr[8]/len(s))*100
    o=(arr[14]/len(s))*100
    u=(arr[20]/len(s))*100
    print(f"Caso {k+1}:")
    print(f"a= {round_java(a,2):.2f}")
    print(f"e= {round_java(e,2):.2f}")
    print(f"i= {round_java(i,2):.2f}")
    print(f"o= {round_java(o,2):.2f}")
    print(f"u= {round_java(u,2):.2f}")
