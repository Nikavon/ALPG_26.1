# Q1. Um estudante só poderá participar do passeio escolar se estiver com
# bom comportamento e tiver a autorização dos pais. Elabore um algoritmo 
# com vários cenários e, ao final, mostre se o  estudante poderá ou não 
# ir ao passeio.


estudante = input("Digite o nome do estudante: ")
print("")
print("1 - Péssimo")
print("2 - Mal")
print("3 - Regular")
print("4 - Bem")
print("5 - Excelente")
comportamento = int(input("\nComo seu estudante tem se comportado? "))

print("")
print("1 - Sim")
print("2 - Não")
print("3 - Sim, mas não foi assinada")
autorizacao = int(input("\nO aluno entregou a autorização? "))

if estudante == 4 or 5 and autorizacao == 1:
    print("Estudante liberado para o passeio")
else:
    print("\nEstudante não poderá participar")