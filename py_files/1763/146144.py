n=int(input())
def np(n):# np numero primo
    for j in range(2,int(n**(1/2))+1):
        if n%j==0 and n!=j:
            return False
    return True
for p in range(n):
    s = int(input())
    pw = False
    for j in range(1000):
        h = s * (2 ** j) + 1
        if np(h):
            print(h)
            pw = True
            break
    if pw == False:
        print('-1')
