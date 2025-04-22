nome = input('digite seu nome completo: ').strip().title()
palavra = nome.split()
print(f'''muito prazer em te conhecer!
seu primeiro nome é {palavra[0]}
seu último nome é {palavra[len(palavra) - 1]}''')