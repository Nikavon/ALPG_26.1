'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# Q4. Verificador de Ano Bissexto (Simplificado)
# Um ano é bissexto se ele for divisível por 400. Caso não seja, ele também é bissexto se 
# for divisível por 4, desde que não seja divisível por 100. Escreva um programa que leia 
# um ano e diga se ele é "Bissexto" ou "Não Bissexto" usando apenas lógica de if/else 
# aninhados.

ano = int(input("Digite o ano: "))

if ano % 400 == 0:
    print(ano , "é um ano bissexto")
else:
    if ano % 4 == 0:
        if ano % 100 != 0:
            print(ano , "é um ano bissexto")   
        else:
            print(ano , "não é um ano bissexto")
    else:
        print(ano , "não é um ano bissexto")
