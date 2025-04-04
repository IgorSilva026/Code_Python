import random

numeros = [3, 4, 7, 13, 19, 26, 31]
x = 3

numeros_escolhidos = random.sample(numeros, x)
numeros_escolhidos.sort()

print(f"Os seus números escolhidos foram: {numeros_escolhidos}")
