# Crie um programa que leˆ 6 valores inteiros e, em seguida, mostre na tela os valores lidos.

numeros = [0,0,0,0,0,0]
indice = 0

while indice <= 5:
    numeros[indice] = int(input("Digite um número: "))
    indice += 1

print(numeros)