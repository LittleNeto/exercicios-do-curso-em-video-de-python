frase = str(input('Digite uma frase: ')).strip().upper()
lista = frase.split()
frase = ''
for c in lista:
    frase += c
frase_invertida = ''
for c in range(len(frase) - 1, -1, -1):
    frase_invertida += frase[c]
print(f'O inverso de {frase} é {frase_invertida}')
print('Temos um palíndromo!') if frase == frase_invertida else print('A frase digitada não é um palíndromo!')