# Q5. Elabore um algoritmo para representar um sistema de compra de produtos agrícolas de 
# uma feira, que só permite a compra se a pessoa tiver dinheiro para pagar à vista e 
# estiver com a anuidade da associação de produtor rural em dia. 

dinheiro_cliente = int(input("Você possui dinheiro para pagar à vista?\n 1 - Sim\n 2 - Não\nResposta: "))   
print()
anuidade = int(input("A anuidade da associação de produtores rural está em dia?\n 1 - Sim\n 2 - Não\nResposta: "))
print()

if dinheiro_cliente == 1:
    if anuidade == 1:
        print("Compra autorizada")
    else:
        print("Compra não autorizada, revise as informações")
 
