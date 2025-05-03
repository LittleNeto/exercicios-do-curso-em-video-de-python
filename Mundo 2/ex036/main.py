valor = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
if salário <= 0 or valor <= 0 or anos <=0:
  print('valor incompatível')
else:
  print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${(valor / (anos * 12)):.2f}')
  print('empréstimo NEGADO!') if (valor / (anos * 12)) > salário * 0.3 else print('empréstimo CONCEDIDO!')