valores = []
for i in range(3):
    numeros = float(input(f"Digite o {i+1} numero: "))
    valores.append(numeros)


soma = sum(valores)
maior = max(valores)
menor = min(valores)
media = soma / len(valores)
valores_ordenados = sorted(valores)

print(f"resultado:")
print(f"soma da lista: {soma}")
print(f"Maior valor da lista: {maior}")
print(f"Menor valor da lista: {menor}")
print(f"valor medio da lista: {media}")
print(f"Os numeros da lista sao: {valores_ordenados}")
