# Q2. (Sistema de RH) Cálculo de Bônus Anual
# Uma empresa vai distribuir bônus de fim de ano com base no tempo de casa e na nota de
# avaliação do funcionário (de 1 a 5). Escreva um programa que:
# 1) Solicite o salário atual do funcionário, o seu tempo de empresa (em anos) e a sua nota de
#avaliação.
# 2) Se a nota for igual a 5 e o tempo de casa for maior que 10 anos, o funcionário ganha um
#bônus de 20% sobre o salário.
# 3) Se a nota for igual a 5 ou (a nota for igual a 4 e o tempo de casa for maior que 5 anos),
#o bônus será de 10%.
# 4) Para qualquer outro cenário, o funcionário não tem direito a bônus (0%).
# 5) Exiba o valor do bônus calculado e o salário total a receber neste mês.


salario_atual = float(input("Digite seu salário atual: "))
tempo_empresa = int(input("Digite seu tempo de empresa (em anos): "))
nota_avaliacao = int(input("Digite sua nota de avaliação (de 1 a 5): "))

if nota_avaliacao == 5 and tempo_empresa > 10:
    bonus = salario_atual * 0.20
elif nota_avaliacao == 5 or (nota_avaliacao == 4 and tempo_empresa > 5):
    bonus = salario_atual * 0.10
else:
    bonus = 0.00       

print("O valor do bônus é: R$", bonus)
print("O salário total a receber neste mês é: R$", salario_atual + bonus)