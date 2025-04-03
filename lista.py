import random

nomes = []
print("Insira 10 nomes para a sua lista")

for i in range(10):
    nome = input(f"Digite o {i+1} nome: ")
    nomes.append(nome)

print("\nLista de nomes inseridos:")
for nome in nomes:
    print(nome)
