quant = -1
termo_atual = 0
proximo_termo = 1
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
while quant < 0:
    quant = int(input('Quantos termos você quer mostrar? '))
    if quant < 0:
        print('Valor inválido! Por favor, tente novamente!')
print('~' * 30)
while quant > -1:
    print(termo_atual, end=' ') if quant != 0 else print('FIM')
    if quant != 0:
        print('->', end=' ')
    quant -= 1
    termo_atual, proximo_termo = proximo_termo, termo_atual + proximo_termo
print('~' * 30)