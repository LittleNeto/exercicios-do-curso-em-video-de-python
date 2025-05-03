tot_comp = mais1000 = meno_valor = menor_prod = cont = 0
continua = True
print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)
while continua:
  prod = str(input('Nome do produto: ')).strip().capitalize()
  preço = float(input('Preço: R$'))
  while preço <= 0:
    preço = float(input('''Valor inválido, tente novamente
Preço: R$'''))
  tot_comp += preço
  if preço > 1000:
    mais1000 += 1
  cont += 1
  if cont == 1:
    menor_valor = preço
    menor_prod = prod
  else:
    if preço < menor_valor:
      menor_valor = preço
      menor_prod = prod
  quer = str(input('Quer continuar? [S/N] ')).strip().upper()
  while quer not in 'SN':
    quer = str(input('''Valor inválido, tente novamente
Quer continuar? [S?N] '''))
  if quer == 'N':
    continua = False
print(f'''---------- FIM DO PROGRAMA ----------
O total da compra foi R${tot_comp:.2f}
Temos {mais1000} produtos custando mais de R$1000.00
O produto mais barato foi {menor_prod} que custa R${menor_valor:.2f}''')