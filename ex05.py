alunos = int(input("Quantos alunos? "))
soma = 0 # acumulador

for i in range(1, alunos + 1):
    nota = float(input(f"Nota do aluno {i}: "))
    soma += nota
    media = soma / alunos
print(f"Média da turma: {media:.1f}")