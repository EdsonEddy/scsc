inicio = int(input())
for i in range(inicio):
    exp = 0
    pp = int(input())
    i = 0
    var = pp * (2**exp) + 1    
    valor = 1
    if (var > 10**4):
        print("-1")
    else:
        while (var < 10**4):
            while (valor <= var):
                dig = var % valor
                if (dig == 0): 
                    i = i + 1
                    valor = valor + 1
                else:
                    valor = valor + 1
            if (i == 2):
                print(var)
                break
            else:
                i = 0
                valor = 1
                exp = exp + 1
                var = pp * (2**exp) + 1
        if (var > 10**4):
            print("-1")