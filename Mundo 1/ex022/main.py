nome = str(input('digite seu nome: ')).strip()
print(f'''analisando seu nome...'
seu nome em maiúsculas é {nome.upper()}
seu nome em minúsculas é {nome.lower()}
seu nome tem ao todo {len(nome) - nome.count(' ')} letras
seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras''')