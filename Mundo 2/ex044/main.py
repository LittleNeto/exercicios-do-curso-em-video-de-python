print('=========== LOJAS GUANABARA ============')
val = float(input('Preço das compras: R$'))
while val <= 0:
  print('valorinválido, tente novamente')
  val = float(input('Preço das compras: R$'))
op = int(input(('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual a sua opção? ''')))
while op < 1 or op > 4:
  print('Valor inválido, tente novamente')
  op = int(input('Qual a sua opção?'))
if op == 1:
  fim = val * 0.9
elif op == 2:
  fim = val * 0.95
elif op == 4:
  fim = val * 1.2
  parc = int(input('Quantas parcelas? '))
  while parc < 3:
    print('informação inválida, tente novamente')
    parc = int(input('Quantas parcelas? '))
  print(f'Sua compra será parcelada em {parc}x de R${(fim / parc):.2f} COM JUROS')
else:
  fim = val
  print(f'Sua compra será parcelada em 2x de R${(fim / 2):.2f}')
print(f'Sua compra de R${val:.2f} vai custar R${fim:.2f} no final.')