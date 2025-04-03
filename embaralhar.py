import random

valores = []

print("adicione seus 10 valores:")
for i in range(10):
    valor = input(f"valor {i+1}: ")
    valores.append(valor)

random.shuffle(valores)

valores.sort()

print("lista embaralhada:")
print(valores)
