mais18 = masculino = mulher_menos_20 = 0
continua = False
print('-' * 30)
print('CADASTRE UMA PESSOA')
print('-' * 30)
while continua:
  idade = int(input('Idade: '))
  while idade > 117 or idade < 0:
    idade = int(input('''Valor inválido, tente novamente
Idade: '''))
  if idade > 18:
    mais18 += 1
  sexo = str(input('Sexo: [M/F] ')).strip().upper()
  while sexo not in 'MF':
    sexo = str(input('''Valor inválido, tente novamente
Sexo: [M/F] ''')).strip().upper()
  if sexo == 'M':
    masculino += 1
  if sexo == 'F' and idade < 20:
    mulher_menos_20 += 1
  print('-' * 30)
  quer = str(input('Quer continuar? [S/N] ')).strip().upper()
  while quer not in 'SN':
    quer = str(input('''Valor inválido, tente novamente
Quer continuar? [S/N] ''')).strip().upper()
  if quer == 'N':
    continua = False
print(f'''Total de pessoas com mais de 18 anos: {mais18}
Ao todo temos {masculino} homens cadastrados
E temos {mulher_menos_20} mulheres com menos de 20 anos''')