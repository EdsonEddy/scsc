# Encontrando el siguiente

num_casos = int(input())
for cas in range(0,num_casos):
  n = int(input())
  if n == 1:
    print(1)
  else:
    num_uno = (n - 1)**3
    num_dos = n**3
    print(f"{num_uno}+{num_dos}")  