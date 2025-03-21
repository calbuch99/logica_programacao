alunos = []
qtd_alunos = int(input("Digite a quantidade de alunos :"))

for i in range(0,qtd_alunos):
    nome = input("Nome Aluno :")
    idade = input("Idade :")
    nota = input("Nota :")

    aluno = {"nome":nome , "idade":idade, "nota":nota}
    alunos.append(aluno)

    print("qtd alunos", len(alunos))

for aluno in alunos:
    print(aluno)