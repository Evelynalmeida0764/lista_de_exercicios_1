quantidade_feminino_altura_superior_170 = 0
quantidade_masculino_bom_status = 0
quantidade_masculino = 0

for i in range(50):
    matricula = input("Digite a matrícula do aluno: ")
    sexo = input("Digite o sexo do aluno (M/F): ")
    altura = float(input("Digite a altura do aluno (em cm): "))
    status_fisico = int(input("Digite o status físico do aluno (1-Bom, 2-Regular, 3-Ruim): "))

    if sexo == "F" and altura > 170:
        quantidade_feminino_altura_superior_170 += 1

    if sexo == "M":
        quantidade_masculino += 1
        if status_fisico == 1:
            quantidade_masculino_bom_status += 1

if quantidade_masculino > 0:
    percentual_masculino_bom_status = (quantidade_masculino_bom_status / quantidade_masculino) * 100
else:
    percentual_masculino_bom_status = 0

print("a) Quantidade de alunas do sexo feminino com altura superior a 170 cm: ", quantidade_feminino_altura_superior_170)
print("b) Percentual de alunos do sexo masculino com status físico bom: ", percentual_masculino_bom_status, "%")