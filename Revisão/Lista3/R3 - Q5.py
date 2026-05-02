'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Q5. (1.5 pontos) Simulador de Descontos VIP
# Escreva um programa para uma loja calcular descontos cumulativos.
# 1) Solicite o valor total das compras do cliente.
# 2) Pergunte se o cliente possui o cartão VIP da loja (Digite ”sim” ou ”nao”).
# 3) Se o valor da compra for maior que R$ 500,00 e o cliente for VIP (”sim”), aplique um des-
# conto de 20%.
# 4) Se o valor for maior que R$ 500,00 ou o cliente for VIP (mas não ambos simultaneamente),
# aplique um desconto de 10%.
# 5) Se nenhuma das condições anteriores for verdade, o desconto é de 0%.
# 6) Exiba o valor do desconto e o montante final a pagar.
    
    
valor_total = float(input("Valor total das compras: R$ "))
cartao_vip = input("Você possui cartão VIP da loja? (Digite ”sim” ou ”nao”): ").lower()
desconto = 0

if valor_total > 500.00 and cartao_vip == "sim":
    desconto = valor_total * 0.20
elif (valor_total > 500 or cartao_vip == "sim") and not (valor_total > 500 and cartao_vip == "sim"):
    desconto = valor_total * 0.10
else:
    desconto = 0

valor_final = valor_total - desconto    
    
print(f"O valor do desconto é R$ {desconto:.2f} e o valor final a pagar é R$ {valor_final:.2f}")    