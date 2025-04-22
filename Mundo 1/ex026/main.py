frase = input('digite uma frase: ').strip().lower()
print(f'''A leta A aparece {frase.count("a")} vezes na frase
A última letra A aparece na posição {frase.rfind('a') + 1}''')