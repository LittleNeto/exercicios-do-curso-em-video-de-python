distancia = int(input('qual é a distância da sua viagem, em Km? '))
if distancia <= 0:
  print('valor inválido')
else:
  print(f'você está prestes a começar a sua viajem de {distancia}Km.')
  if distancia > 200:
    print(f'E o preço da sua passagem será de R${(distancia * 0.45):.2f}')
  else:
    print(f'E o preço da sua passagem será de R${(distancia * 0.5):.2f}')