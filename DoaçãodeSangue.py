idade = int(input("Idade: "))

if idade > 16 and idade < 69:
    peso = float(input("Peso: "))
    if peso > 50:
        descanso = int(input("Horas de sono antes da doação: "))
        if descanso > 6:
            bebida = input("ingeriu bebidas alcolicas 12 horas antes? [S/N]: ").strip().upper()[0]
            if bebida == "N":
                print("Pode doar")
            else:
                print("Não poderia ter bebido")
        else:
            print("Precisa descansar mais de 6hr")
    else:
        print("Peso fora do normal")
else:
    print("idade não permitida")
