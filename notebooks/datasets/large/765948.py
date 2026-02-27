def encontrando_siguiente(n):
  if n == 1:
    return 1
  else:
    cont = 1
    i = 1
    j = 2
    while cont < n:
      result =  f"{i}+{j**3}"
      i = j**3
      cont += 1
      j += 1
    return result
    
num_casos = int(input())
for casos in range(num_casos):
  num = int(input())
  print(encontrando_siguiente(num))  