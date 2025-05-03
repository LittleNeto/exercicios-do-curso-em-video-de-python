quant_termos = 10
num = int(input('''Gerador de PA
-=-=-=-=-=-=-=-=-=-=
Primeiro termo: '''))
raz = int(input('Razão da PA: '))
while quant_termos != -1:
    print(f'{num}', end=' ') if quant_termos != 0 else print('FIM')
    if quant_termos != 0:
        print('->', end=' ')
    num += raz
    quant_termos -= 1