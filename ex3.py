# Ler um conjunto de numeros reais, armazenando-o em vetor e calcular o quadrado das
# componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos tˆem 10
# elementos cada. Imprimir os conjuntos

A = []
B = []
i = 0

while i < 10:
    numero = float(input(f"Digite o {i+1}º número real: "))
    A.append(numero)
    B.append(numero ** 2)
    i += 1

print("\nVetor A (original):")
print(A)

print("\nVetor B (quadrados):")
print(B)
