# Q3. (3.0 pontos) Sistema de Avaliação de Projetos
# Um professor de Lógica precisa de um sistema rápido para classificar o desempenho de um
# estudante com base na prova e num projeto prático. Faça um programa que:
# 1) Solicite a nota da prova final (entre 0.0 e 10.0) e a porcentagem de frequência (inteiro de
# 0 a 100).
# 2) Solicite se o aluno entregou o projeto extra (Digite 1 para SIM, 2 para NÃO).
# 3) Se a frequência for menor que 75, exibir a mensagem ”Aluno reprovado por faltas”, inde-
# pendentemente das notas.
# 4) Se a frequência for maior ou igual a 75, o sistema deve avaliar a nota:
# - Se a nota da prova for maior ou igual a 7.0, exibir: ”Aprovado direto com nota = ” e
# apresentar a nota.
# - Se a nota for menor que 7.0 e o projeto extra foi entregue (opção 1), o programa
# deve somar 1.5 à nota da prova.
# - Após a soma, verificar novamente: se a nova nota passar a ser maior ou igual a 7.0,
# exibir ”Aprovado com a nota do projeto. Nova nota = ” e apresentar a nota atualizada.
# Caso contrário, exibir ”Reprovado mesmo com o projeto. Nota = ” e apresentar a nota
# atualizada.


nota_final = float(input("Digite a nota final: "))
frequencia = int(input("Digite a frequência: "))
projeto_extra = int(input("O aluno entregou o projeto extra?\n1 - Sim\n2 - Não\n"))

if frequencia < 75:
    print("Aluno reprovado por faltas")
else:
    if nota_final >= 7.0:
        print("Aprovado direto com nota = ", nota_final)
    elif nota_final < 7.0 and projeto_extra == 1:
        nota_final += 1.5
        if nota_final >= 7.0:
            print("Aprovado com a nota do projeto. Nova nota = ", nota_final)
        else:
            print("Reprovado mesmo com o projeto. Nota = ", nota_final)
    else:
        print("Reprovado. Nota = ", nota_final)