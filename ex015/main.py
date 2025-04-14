dias = int(input('quantos dias alugado? '))
km = float(input('quanto km rodados '))
if dias <= 0 or km <= 0:
  print('você não usou o carro')
else:
  print(f'o total a pagar é de R${(60 * dias + 0.15 * km):.2f}')