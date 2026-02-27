from sys import stdin
import sys
sys.set_int_max_str_digits(100000)

def input():
    return stdin.readline().strip()

def contarDigitos(x:int)->int:
    ans=0
    while x>0:
        ans+=x%10
        x//=10
    return ans

def binpow(b:int,e:int)->int:
    if e==0:return 1
    pot=binpow(b,e//2)
    pot*=pot
    if e%2==1:pot*=b
    return pot%9



res=""

for _ in range(int(input())):
    x,k=map(int,input().split())
    last=contarDigitos(binpow(x,k))
    # print(x**k)
    for i in range(201):
        last=contarDigitos(last)
    if last==0:last=9
    res+=(str(last)+"\n")


print(res)



