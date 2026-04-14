# Q4. Calcular a média entre duas notas e informar se o estudante foi ou não aprovado (para 
# ser aprovado, a média tem que ser maior ou igual a 6). Faça uso do not.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if not media <= 6:
    print("Aprovado")
else:
    print("Reprovado")    