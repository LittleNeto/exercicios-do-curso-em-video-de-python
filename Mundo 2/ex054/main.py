from datetime import date
quant_menor_idade = quant_maior_idade = 0
for c in range(1, 8):
    ano = -1
    while ano < 0:
        ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
        if ano < 0:
            print('Valor inválido! Por favor, tente novamente!')
    if date.today().year - ano < 18:
        quant_menor_idade += 1
    else:
        quant_maior_idade += 1
print(f'''Ao todo tivemos {quant_maior_idade} pessoas maiores de idade
E também tivemos {quant_menor_idade} pessoas menores de idade''')