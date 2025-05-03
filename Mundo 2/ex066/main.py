cont = 0
tot = 0
continua = True
while continua:
  num = int(input('Digite um valor (999 para parar): '))
  if num != 999:
    tot += num
    cont += 1
  else:
    continua = False
print(f'A soma do {cont} valores foi {tot}!')