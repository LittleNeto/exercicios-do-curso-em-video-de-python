maior = 0
menor = 0
for c in range(1, 6):
  peso = float(input('digite seu peso: '))
  if c == 1:
    maior = peso
    menor = peso
  else:
   if peso > maior:
    maior = peso
   elif peso < menor:
    menor = peso
print(f'''O maior peso lido foi de {maior}Kg 
O menor peso lido foi de {menor}Kg''')