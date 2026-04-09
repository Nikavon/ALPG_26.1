# Q3. Escreva um algoritmo que leia o nome e as três notas obtidas por um aluno durante o 
# semestre. Calcular a sua média (aritmética), informar o nome e o resultado final: Aprovado 
# (media >= 7), Reprovado (media <= 5), ou em Recuperação (media entre 5.1 a 6.9).

nome_aluno = input("Digite seu nome: ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
nota = nota_1 + nota_2 + nota_3
media_aritmetica = nota / 3

print("Aluno: ", nome_aluno)
print("Média: ", media_aritmetica)

if media_aritmetica >= 7:
    print("Aprovado")
elif media_aritmetica <= 5:
    print("Reprovado")
else:
    print("Em recuperação")