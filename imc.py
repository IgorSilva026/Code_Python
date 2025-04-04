peso = float(input("Seu peso: "))
alltura = float(input("Sua altura: "))

imc = peso / (alltura**2)

if imc >= 40:
    print(f"Obesidade de grau 3, seu IMC é {imc:.2f}")
elif imc >= 35.0:
    print(f"Obesidade de grau 2 seu IMC é {imc:.2f}")
elif imc >= 30.0:
    print(f"Obesidade de grau 1 seu IMC é {imc:.2f}")
elif imc >= 25.0:
    print(f"Levemente a cima do peso seu IMC é {imc:.2f}")
elif imc >= 18.6:
    print(f"Peso ideal(PARABENS) seu IMC é {imc:.2f}")
else:
    print(f"Abaixo do peso seu IMC é {imc:.2f}")
