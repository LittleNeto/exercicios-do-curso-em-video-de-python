soma_idade = maior_idade = quant_mulheres = 0
nome_maior_idade = sexo = ' '
idade = -1
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().upper()
    while idade < 0:
        idade = int(input('Idade: '))
        if idade < 0:
            print('Valor inválido! Por favor, tente novamente!')
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).strip()
        if sexo not in 'FM':
            print('Resposta inválida! Por favor, tente novamente!')
    soma_idade += idade
    if c == 1:
        maior_idade = idade
        nome_maior_idade = nome
    else:
        if idade > maior_idade:
            maior_idade = idade
            nome_maior_idade = nome
    if idade < 20 and sexo == 'F':
        quant_mulheres += 1
    idade = -1
    sexo = ' '
print(f'''A média de idade do grupo é de {(soma_idade / 4):.1f} anos
O homem mais velho tem {maior_idade} anos e se chama {nome_maior_idade}
Ao todo são {quant_mulheres} com menos de 20 anos''')