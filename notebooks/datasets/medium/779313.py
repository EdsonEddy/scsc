def f(a):
 b=[1,2]
 while b[-1]+b[-2]<=a:b.append(b[-1]+b[-2])
 return b

def g(a,b):
 c='';d=0
 for i in reversed(range(len(b))):
  if b[i]<=a:
   c+='1';a-=b[i];d=1
  elif d:c+='0'
 return c

import sys
for x in sys.stdin.read().split():
 print(g(int(x),f(10**12)))