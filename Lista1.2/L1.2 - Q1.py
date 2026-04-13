'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# Q1. Controle de Acesso por Altura e Idade
# Um parque de diversões tem uma regra de segurança: para andar na montanha-russa, a 
# criança deve ter pelo menos 12 anos e medir no mínimo 1.50m de altura. Escreva um 
# programa que leia a idade e a altura e informe se ela pode ou não subir no brinquedo.
# Dica: Use um if dentro de outro para verificar as duas condições.

idade = int(input("Por favor digite sua idade: "))
altura = float(input("Por favor digite sua altura: "))

if idade > 12:
    print()
    if altura > 1.50:
        print("Acesso liberado")
    else:
        print ("Acesso negado")    
else:
    print ("Acesso negado")