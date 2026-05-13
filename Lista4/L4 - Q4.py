'''
Q4. Escreva um algoritmo que solicita a quantidade de alunos em uma turma de curso de pré-vestibular. 
Depois, solicita que seja informado para cada aluno, se este foi aprovado ou reprovado no vestibular. 
No final, o sistema deverá informar quantos alunos foram aprovados e quantos foram reprovados.
'''

aluno_aprovado = 0
aluno_reprovado = 0

alunos_quant = int(input("Quantos alunos há na turma? "))

for i in range (1, alunos_quant + 1):
    print(f"\n--- Aluno {i} ---")
    resposta = input("Foi aprovado? (S/N): ").upper()
    
    if resposta == "S":
        aluno_aprovado = aluno_aprovado + 1
        print("Registrado como aprovado.")
    else:
        aluno_reprovado = aluno_reprovado + 1
        print("Registrado como reprovado")
           
print("\nResultado final")  
print(f"Total de alunos: {alunos_quant}")
print(f"Aprovados: {aluno_aprovado}")
print(f"Reprovados: {aluno_reprovado}")         
        