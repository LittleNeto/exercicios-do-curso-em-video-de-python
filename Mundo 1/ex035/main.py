seg1 = float(input('primeiro segmento: '))
seg2 = float(input('segundo segmento: '))
seg3 = float(input('terceiro segmento: '))
if seg1 <= 0 or seg2 <= 0 or seg3 <= 0:
  print('segmentos inexistentes')
else:
  if seg1 < (seg2 + seg3) and seg2 < (seg1 + seg3) and seg3 < (seg1 + seg2):
    print('esses segmentos podem formar um triângulo')
  else:
    print('esses valores não podem formar um triângulo')