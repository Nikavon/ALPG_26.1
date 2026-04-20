# Q1. (Sistema de E-commerce) Cálculo de Frete
# Escreva um programa que calcule o valor final de uma compra online, aplicando regras de frete
# grátis por região.
# 1) Crie no código uma lista com as siglas dos estados da região Sudeste: ["SP", "RJ", "MG",
# "ES"].
# 2) Solicite ao usuário o valor total dos produtos no carrinho (número real).
# 3) Solicite a sigla do estado para entrega.
# 4) Se a sigla digitada estiver na lista e o valor da compra for maior que R$ 150,00, o frete é
# grátis (R$ 0,00).
# 5) Se a sigla estiver na lista, mas a compra for menor ou igual a R$ 150,00, o frete custará R$
# 15,00.
#6) Se a sigla não estiver na lista, o frete fixo é de R$ 35,00, independentemente do valor da
# compra.
# 7) Exiba o valor do frete e o valor total final (produtos + frete) a ser pago.


carrinho = float(input("Digite o valor total dos produtos no carrinho: R$ "))
estado = input("Digite a sigla do estado para entrega: ").upper()
sudeste = ["SP", "RJ", "MG", "ES"]


if carrinho > 150 and estado in sudeste:
    frete = 0.00
elif estado in sudeste:
    frete = 15.00
else:
    frete = 35.00

print("Valor total final: R$120", carrinho + frete)    
