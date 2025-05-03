sexo = input('Informe seu sexo: [M/F] ').strip().upper()
while sexo != 'M' and sexo != 'F':
  sexo = input('Dados inválidos. por favor, informe seu sexo: ').strip().upper()
print(f'Sexo {sexo} registado com sucesso')