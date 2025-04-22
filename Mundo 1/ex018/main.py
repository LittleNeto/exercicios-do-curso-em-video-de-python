from math import sin, cos, tan, radians
angulo = float(input('digite o ângulo que você deseja: '))
print(f'o ângulo de {angulo} tem o seno de {sin(radians(angulo)):.2f}')
print(f'o ângulo de {angulo} tem o cosseno de {cos(radians(angulo)):.2f}')
print(f'o ângulo de {angulo} tem a tangente de {tan(radians(angulo)):.2f}')