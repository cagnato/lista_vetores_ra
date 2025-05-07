# Fac ̧a um programa que leia um vetor de 8 posic ̧ ̃oes e, em seguida, leia tamb ́em dois va-
# lores X e Y quaisquer correspondentes a duas posic ̧ ̃oes no vetor. Ao final seu programa
# devera ́ escrever a soma dos valores encontrados nas respectivas posic ̧ ̃oes X e Y 

vetor = []
i = 0

while i < 8:
    numero = int(input(f"digite o {i+1}º número: "))
    vetor.append(numero)
    i += 1

X = int(input("Digite a poisção X (0 a 7): "))
Y = int(input("Digite a poisção Y (0 a 7): "))

if (0 <= X < 8) and (0 <= Y < 8):
    soma = vetor[X] + vetor[Y]
    print(f"A soma dos valores nas posições {X} e {Y} é: {soma}")
else:
    print("Posições inválidas! Devem estar entre 0 e 7.")