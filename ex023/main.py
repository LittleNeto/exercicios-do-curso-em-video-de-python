#essa solução não utiliza os métodos internos das strings
num = int(input('Informe um número: '))
print(f'''Analisando o número {num}
Unidade: {num % 10}
Dezena: {num % 100 // 10}
Centena: {num % 1000 // 100}
Milhar: {num % 10000 // 1000}''')