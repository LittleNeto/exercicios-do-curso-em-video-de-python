maior = menor = 0
info = 0
cont = 0
tot = 0
while info != 'N':
  num = int(input('Digite um número: '))
  cont += 1
  tot += num
  if cont == 1:
    maior = num
    menor = num
  else:
    if num > maior:
      maior = num
    elif num < menor:
      menor = num
  info = str(input('Quer continuar? [S/N] ')).strip().upper()
print(f'''Você digitou {cont} números e a médi foi {tot / cont:.2f}
O maior valor foi {maior} e o menor foi {menor}''')