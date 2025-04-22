preco = float(input('qual é o preço do produto? R$'))
if preco < 0:
  print('valor não compatível')
else:
  print(f'o produto que custava R${preco:.2f}, na promoção com desconto de 5% de desconto, vai custar {(preco * 0.95):.2f}')