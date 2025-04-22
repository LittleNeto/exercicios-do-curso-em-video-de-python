salario = float(input('qual o salário do funcionário? R$'))
if salario <= 0:
  print('salário inexistente')
else:
  if salario < 1250:
    print(f'Quem ganhava R${salario:.2f} passa a receber R${(salario * 1.1):.2f}')
  else:
    print(f'Quem ganhava R${salario:.2f} passa a receber R${(salario * 1.15):.2f}')