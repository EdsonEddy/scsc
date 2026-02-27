def llenar_mat ():
    f = int(input())
    c = f
    mat = [[0 for j in range(c)] for i in range(f)]
    for i in range (f):
        numero = str(input())
        mat[i] = [int(digito) for digito in numero]
    return mat
            
def dig_principal(mat):
    c = f = len(mat)
    sum_d = 0
    for i in range (f):
        for j in range(c):
            if i == j:
                sum_d = sum_d + mat[i][j]
    return sum_d
            
def dig_secundaria(mat):
    c = f = len(mat)
    sum_s = 0
    for i in range (f):
        for j in range(c):
            if (i + j) == (c-1):
                sum_s = sum_s + mat[i][j]
    return sum_s

def desproporcion (mat):
    dp = dig_principal(mat)
    ds = dig_secundaria(mat)
    des = dp - ds
    return des
    
    
x = int(input())
for i in range (x):
    mat = llenar_mat()
    des = desproporcion(mat)
    print (des)