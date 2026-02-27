def insert_dig_sum(dig, i):
  str_num = f"{dig}{i}"
  return int(str_num)

def eliminar_ultimo_dig(e):
  return e // 10

def sumita(s):
    sumita = 0
    while s > 0:
      sumita += s % 10
      s //= 10
    return sumita

def siguiendo_reglas(num, n):
  for j in range(n):
    dig_suma = num
    while len(str(dig_suma)) != 1:
      dig_suma = sumita(dig_suma)
    e = eliminar_ultimo_dig(num)
    i = insert_dig_sum(dig_suma, e)
    num = i
  return i

num_casos = int(input())
for i in range(num_casos):
  s, k = map(int, input().split())
  print(siguiendo_reglas(s, k))
