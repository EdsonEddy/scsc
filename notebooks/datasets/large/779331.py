t=int(input())
for _ in range(t):
 a=input();r=int(a)%7;s=''
 while int(a)>81:
  b=int(a[:-1]);c=int(a[-1])
  s+=f'({b}, {c})'
  a=str(b+c*5)
 x=int(a)
 s+=f' {x} {"correcto" if x%7==r else "incorrecto"}'
 print(s)