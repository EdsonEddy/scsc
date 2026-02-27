import math
casos = int(input())
for j in range(casos):
    n, k = map(int, input().split())

    for i in range(k):
        guardo_n = n
        while n>=10:
            suma = 0
            while n>0:
                digito = n%10
                suma += digito
                n //= 10
            n = suma
        digito_final = suma
        #print(digito_final)

        digitos_n = int(math.log10(guardo_n))
        #print(digitos_n)

        pre_nuevo_numero = digito_final*(10**digitos_n)
        #print(pre_nuevo_numero)

        elim_digito = guardo_n//10
        #print(elim_digito)

        nuevo_numero = pre_nuevo_numero + elim_digito
        #print(nuevo_numero)
    
        n = nuevo_numero
    
    numero_final = n
    
    print(numero_final)