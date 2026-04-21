# Q1. (1.5 pontos) Sistema de Mensalidades
# Escreva um programa para a secretaria do instituto que calcule o valor a pagar da mensalidade,
# considerando atrasos ou adiantamentos.
# 1) Solicite ao usuário o valor base da mensalidade (número real).
# 2) Solicite o número de dias de atraso (número inteiro). Se o aluno pagou adiantado, o usu-
# ário digitará um valor negativo (ex: -5).
# 3) Se os dias de atraso forem maiores que 0, calcule uma multa de 5% sobre o valor base e
# adicione ao total.
# 4) Se os dias de atraso forem menores que 0 (pagamento adiantado), calcule um desconto
# de 10% sobre o valor base e subtraia do total.
# 5) Se o dia de atraso for exatamente 0, o valor permanece inalterado.
# 6) Exiba o valor final a ser pago pelo aluno (em Reais).


mensalidade = float(input("Qual o valor da sua mensalidade? "))
atraso = int(input("Há quantos dias a mensalidade está atrasada (em caso de pagamento adiantado, informa o valor negativo): "))

if atraso > 0:
    multa = mensalidade * 0.05
    valor_final = mensalidade + multa
elif atraso < 0:
    desconto = mensalidade * 0.10
    valor_final = mensalidade - desconto
else:  # atraso == 0
    valor_final = mensalidade

print(f"O valor final a ser pago é: R$ {valor_final:.2f}")