num1 = int(input('primeiro número: '))
num2 = int(input('segundo número: '))
num3 = int(input('terceiro número: '))
if num1 > num2 > num3 or num1 > num3 > num2:
 print(f'o maior número é {num1}')
elif num2 > num1 > num3 or num2 > num3 > num1:
 print(f'o maior número é {num2}')
elif num3 > num1 > num2 or num3 > num2 > num1:
 print(f'o maior número é {num3}')
else:
 print('existe igualdade entre dois ou mais termos')