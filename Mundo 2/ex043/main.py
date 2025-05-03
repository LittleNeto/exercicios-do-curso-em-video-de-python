peso = float(input('Qual o seu peso? (Kg) '))
alt = float(input('Qual a sua altura? (m) '))
while peso > 595 or peso < 2.1 or alt > 2.51 or alt < 0.62:
  print('Uma ou mais informações inválidas, tente de novo')
  peso = float(input('Qual o seu peso? (Kg) '))
  alt = float(input('Qual a sua altura? (m) '))
imc = peso / (alt ** 2)
print(f'O IMC dessa pesoa é de {imc:.1f}')
if 18.5 < imc < 25:
  print('PARABÉNS, você está na faixa do PESO NORMAL')
elif imc < 18.5:
  print('Você está ABAIXO DO PESO normal')
elif 25 <= imc < 30:
  print('Você está em SOBREPESO')
elif 30 <= imc <=40:
  print('Você está em OBESIDADE')
else:
  print('Você está em OBECIDADE MÓRBIDA, cuidado!')