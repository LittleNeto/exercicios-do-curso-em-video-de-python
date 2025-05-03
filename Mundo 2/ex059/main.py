from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
op = 0
while op != 5:
  op = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
>>>>> Qual a sua opção? '''))
  if op == 1:
    print(f'A soma ente {num1} + {num2} é {num1 + num2}')
  elif op == 2:
    print(f'''O resultado de {num1} x {num2} é {num1 * num2}''')
  elif op == 3:
    if num1 > num2:
      print(f'Ente {num1} e {num2} o maior é {num1}')
    elif num1 < num2:
      print(f'Entre {num1} e {num2} o maior é {num2}')
    else:
      print('Os dois valores são iguais')
  elif op == 4:
    num1 = int(input('''Informe os números novamente:
Primeiro valor: '''))
    num2 = int(input('Segundo valor: '))
  elif op == 5:
    print('Finalizando...')
  else:
    print('Opção inválida. Tente novamente')
  print('=-=' * 10)
  sleep(2)
print('Fim do programa, volte sempre')