import random

inicio = int(input("Digite o inicio:"))
final = int(input("digite o final:"))

valorsorteado = random.randint(inicio, final)

lista = []
for i in range(5):
    aposta = int(input("digite um valor:"))
    lista.append(aposta)

if valorsorteado in lista:
    print("errou!!")

print(f"O valor sorteado foi: {valorsorteado}")
print(f"A lista de aposta foi: {lista}")
