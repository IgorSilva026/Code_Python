import random


def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    print("Bem-vindo ao jogo de adivinhação!")
    print(
        "Tente adivinhar o número que estou imaginando. Ele pode ser de 1 a 100. Boa Sorte!!!"
    )

    while True:
        palpite = input("Digite o seu palpite: ")

        if not palpite.isdigit():
            print("Por favor, insira um número válido.")
            continue

        palpite = int(palpite)
        tentativas += 1

        if palpite < numero_secreto:
            print("O número é maior. Tente outro.")
        elif palpite > numero_secreto:
            print("O número é menor. Tente outro.")
        else:
            print(
                f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas."
            )
            break


jogo_adivinhacao()
