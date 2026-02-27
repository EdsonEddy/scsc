t=int(input())
for _ in range(t):
 n=input()
 a=int(n)%7
 while int(n)>81:
  x=n[:-1]
  y=n[-1]
  print(f'({x}, {y})',end='')
  n=str(int(x)+int(y)*5)
 print('',n,'correcto' if int(n)%7==a else 'incorrecto')
