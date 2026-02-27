def round_java_style(value, decimals=2):
    multiplier = 10 ** decimals
    return int(value * multiplier + 0.5) / multiplier

t = int(input())

for case in range(1, t + 1):
    s = input().strip()
    
    count_a = s.count('a')
    count_e = s.count('e')
    count_i = s.count('i')
    count_o = s.count('o')
    count_u = s.count('u')
    
    total_chars = len(s)
    
    print(f"Caso {case}:")
    
    if total_chars == 0:
        print("a= 0.00")
        print("e= 0.00")
        print("i= 0.00")
        print("o= 0.00")
        print("u= 0.00")
    else:
        percent_a = round_java_style((count_a * 100.0) / total_chars)
        percent_e = round_java_style((count_e * 100.0) / total_chars)
        percent_i = round_java_style((count_i * 100.0) / total_chars)
        percent_o = round_java_style((count_o * 100.0) / total_chars)
        percent_u = round_java_style((count_u * 100.0) / total_chars)
        
        print(f"a= {percent_a:.2f}")
        print(f"e= {percent_e:.2f}")
        print(f"i= {percent_i:.2f}")
        print(f"o= {percent_o:.2f}")
        print(f"u= {percent_u:.2f}")

