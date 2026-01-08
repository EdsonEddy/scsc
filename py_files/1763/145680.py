def primo(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0 and n!=i:
            return False
            break
    return True

n=int(input())
for i in range(n):
    k=int(input())
    sw=False
    for j in range(1000):
        m=k*(2**j)+1
        if primo(m):
            print(m)
            sw=True
            break
    if sw==False:
        print('-1')
