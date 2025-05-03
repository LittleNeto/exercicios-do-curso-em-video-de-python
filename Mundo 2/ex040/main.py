nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
while nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
  print('uma ou mais informações inválidas! tente novamente')
  nota1 = float(input('Primeira nota: '))
  nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
if media >= 7:
  print('O aluno está APROVADO.')
elif 5 <= media < 7:
  print('O aluno está em RECUPERAÇÃO.')
else:
  print('O aluno está REPROVADO.')