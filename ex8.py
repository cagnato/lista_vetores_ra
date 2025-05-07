# Fac ̧a um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
# e imprima a m  ́edia geral.

vetor = []
i = 0
soma = 0

while i < 15:
    nota = float(input(f"Digite a {i+1}ª nota: "))
    vetor.append(nota)
    soma += nota
    i += 1

media = soma / 15
print(f"A média geral das notas informadas é {media:.2f}")
