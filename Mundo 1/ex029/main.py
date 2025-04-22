velocidade = float(input('qual a veclocidade percorrida, em Km/h? '))
if velocidade <= 0:
  print('velocidade inexistente')
else:
  if velocidade > 80:
    print(f'você foi multado! a multa vai custar R${((velocidade - 80) * 7):.2f}!')
  else:
    print('você não foi multado! tenha um bom dia!')