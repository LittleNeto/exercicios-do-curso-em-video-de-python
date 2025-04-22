salario = float(input('qual é o salário de um funcionário? R$'))
if salario < 0:
  print('valor não compatível')
elif salario == 0:
  print('seu trabalho é escravo')
else:
  print(f'um funcionário que ganhava {salario:.2f}, com 15% de aumento, passa a receber {(salario * 1.15):.2f}')