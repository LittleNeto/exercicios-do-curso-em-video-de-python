valor = -1
print('=' * 30)
print('BANCO CEV')
print('=' * 30)
cedulas = (50, 20, 10, 1)
quantidades = list()
while valor < 0:
    valor = int(input('Que valor você quer sacar? R$'))
    if valor < 0:
        print('Valor Inválido! Por favor, tente novamente!')
for c in cedulas:
    quantidades.append(valor // c)
    valor %= c
    if quantidades[len(quantidades) - 1] != 0:
        print(f'Total de {quantidades[len(quantidades) - 1]} cédulas de R${c}')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')