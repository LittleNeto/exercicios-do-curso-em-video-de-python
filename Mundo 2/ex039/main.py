from datetime import date
gen = input('Qual o seu gênero? (M/F) ').strip().upper()
while gen != 'M' and gen != 'F':
  gen = input('''Informação inválida, tente novamente
Qual o seu gênero? (M/F) ''').strip().upper()
if gen == 'F':
  print('Você não precisa fazer alistamento militar')
else:
  atual = date.today().year
  ano = int(input('Ano de nascimento: '))
  idade = atual - ano
  while idade < 0 or idade > 117:
    ano = int(input('''informação inválida, tente novamente!
Ano de nascimento: '''))
    idade = atual - ano
  print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
  if idade < 18:
    print(f'''Ainda falta(m) {18 - idade} ano(s) para o alistamento
Seu alistamento será em {atual + 18 - idade}''')
  elif idade > 18:
    print(f'''Você já deveria ter se alistado há {idade - 18} ano(s)
Seu alistamento foi em {atual - idade + 18}''')
  else:
    print('Você tem que se alistar IMEDIATAMENTE!')