algo = input('digite algo: ')
print(f'o tipo primitivo desse valor é {type(algo)}')
print(f'só tem espaços? {algo.isspace()}')
print(f'é um número? {algo.isnumeric()}')
print(f'é alfabético? {algo.isalpha()}')
print(f'é alfanumérico? {algo.isalnum()}')
print(f'está em maiúsculas? {algo.isupper()}')
print(f'está em minúsculas? {algo.islower()}')
print(f'está capitalizada? {algo.istitle()}')