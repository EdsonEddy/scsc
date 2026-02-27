import sys
for l in sys.stdin:
 n=int(l)
 if n==-1:break
 r=n
 i=2
 a=[]
 while i*i<=n:
  c=0
  while n%i==0:
   n//=i
   c+=1
  if c:a.append((i,c))
  i+=1
 if n>1:a.append((n,1))
 s=str(r)+' = '
 s+='*'.join(f'{p}' if e==1 else f'{p}^{e}' for p,e in a)
 print(s)
