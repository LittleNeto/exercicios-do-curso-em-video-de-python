s1 = float(input('primeiro segmento: '))
s2 = float(input('segundo segmento: '))
s3 = float(input('terceiro segmento: '))
if s1 <= 0 or s2 <= 0 or s3 <= 0:
  print('segmentos inexistentes')
else:
  if s1 > (s2 + s3) and s2 > (s1 + s3) and s3 > (s1 + s2):
    print('esses segmentos não podem formar um triângulo')
  else:
    if s1 == s2 == s3:
      print('Os segmentos acima podem formar um triângulo equilátero!')
    elif s1 != s2 != s3 != s1:
      print('Os segmentos acima podem formar um triângulo escaleno!')
    else:
      print('Os segmentos acima podem formar um triângulo isóceles!')