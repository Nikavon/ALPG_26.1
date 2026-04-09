'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Q4. Elabore um algoritmo para representar um sistema de compra de produtos agrícolas de
# uma feira, para isso, simule 3 produtos, e coloque o seu preço unitário. Depois 
# pergunte a quantidade que deseja comprar de cada produto.
# Calcule o valor a pagar. Mas no momento do pagamento, perguntar como o cliente irá pagar: em dinheiro
# ou Pix (terá 10% de desconto) ou cartão (sem desconto). Informe o valor final a pagar.

preco_maca = 0.50
preco_alface = 5.00
preco_batata = 0.30

print("¨¨¨¨ BARRACA DA FRUTA ¨¨¨¨")
print("Maçã - R$ 0,50 unidade")
print("Alface - R$ 5,00 unidade")
print("Batata - R$ 0,20 unidade")
print()

quantidade_maca = int(input("Quantas maçãs você deseja comprar? "))
quantidade_alface = int(input("Quantas cabeças de alface você deseja comprar? "))
quantidade_batata = int(input("Quantas batatas você deseja comprar? "))

total_maca = quantidade_maca * preco_maca
total_alface = quantidade_alface * preco_alface
total_batata = quantidade_batata * preco_batata
total_geral = total_maca + total_alface + total_batata

print("Total da compra: R$", total_geral)
print()

print("¨¨¨ FORMA DE PAGAMENTO ¨¨¨")
print("1 - Dinheiro ou Pix (10% de desconto)")
print("2 - Cartão")
valor = int(input("Escolha a forma de pagamento: "))

if valor == 1:
    valor_final = total_geral - (total_geral * 0.10)
    print("Valor final já com o desconto: ", valor_final)
    
elif valor == 2:
    valor_final = total_geral
    print("Valor final: ", valor_final)

else:
    print("Operação inválida")