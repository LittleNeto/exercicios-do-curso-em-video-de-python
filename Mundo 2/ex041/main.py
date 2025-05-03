from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
while idade > 117 or idade < 0:
  ano = int(input('''Informação inválida, tente novamente
Ano de nascimento: '''))
  idade = atual - ano
print(f'O atleta tem {idade} anos')
if idade <= 9:
  print('Classificação: MIRIM')
elif 9 < idade <= 14:
  print('Classificação: INFANTIL')
elif 14 < idade <= 19:
  print('Classificação: JUNIOR')
elif 19 < idade <= 25:
  print('Classificação: SÊNIOR')
else:
  print('Classificação: MASTER')