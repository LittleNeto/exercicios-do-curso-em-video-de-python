cont = 0
tot = 0
num = 0
while num != 999:
  num = int(input('Digite um número [999 para parar]: '))
  if num != 999:
    cont += 1
    tot += num
print(f'Você digitou {cont} números e a soma entre eles foi {tot}')