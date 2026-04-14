# Q3. Para que um estudante seja aprovado, ele tem que ter a média maior ou igual a 6 ou ter
# sido aprovado na recuperação. Apresente o resultado final: se o estudante foi aprovado ou 
# reprovado.

media = float(input("Digite a média do aluno: "))

if media >= 6 or recuperacao == 1:
    print("Aluno aprovado!")
else:
    recuperacao = int(input("O aluno passou na recuperação? 1 - Sim 2 - Não "))
    if recuperacao == 1:
        print("Aluno aprovado!")  
    else:
        print("Aluno reprovado!")       

