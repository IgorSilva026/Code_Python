import random

nomes = [
    "Igor",
    "Pedro",
    "Luiz",
    "Fernando",
    "Emilly",
    "Thiago",
    "Lucas",
    "Pietro",
    "Thais",
    "Alef",
]

while nomes:
    input("Presione uma tecla para sortear um nome:")
    nomesorteado = random.choice(nomes)
    print(f"Nome sorteado é: {nomesorteado}")
    nomes.remove(nomesorteado)
    print(f"Nomes restantes:{nomes}")
