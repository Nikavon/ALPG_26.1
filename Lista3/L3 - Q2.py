# Q2 O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
#Cachorro quente    100     1,20
# Bauru simples     101     1,30
# Bauru com ovo     102     1,50
# Hambúrger         103     1,20
# Cheeseburguer     104     1,30
# Refrigerante      105     1,00
# Escreva um algoritmo que leia o código do item pedido, a quantidade e calcule o valor a ser pago por 
# aquele lanche. Considere que a cada execução somente será calculado um item.
# Caso o valor do código seja inválido, informar.

print("Faça seu pedido!!!")
print("100 - Cachorro Quente")
print("101 - Bauru Simples")
print("102 - Bauru com ovo")
print("103 - Hamburguer")
print("104 - Cheeseburguer")
print("105 - Refrigerante")

pedido = int(input("Digite o código do seu produto: "))
quantidade = int(input("Digite a quantidade: "))
preco = 0

if pedido == 100:
    preco = 1.20
elif pedido == 101:
    preco = 1.30
elif pedido == 102:
    preco = 1.50
elif pedido == 103:
    preco = 1.20
elif pedido == 104:
    preco = 1.30
elif pedido == 105:
    preco = 1.00
else:
    print("Erro no código")

if preco > 0:
    pedido_total = preco * quantidade
    print("Valor total a pagar: ", pedido_total)