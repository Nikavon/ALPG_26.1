'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''
Q2. Escreva um algoritmo que leia o nome e a altura de 10 pessoas, e imprima o nome da maior e da menor 
pessoa.
'''

maior_altura = 0
menor_altura = float('inf')
nome_maior = ""
nome_menor = ""

for n in range(1, 11): 
    nome = input(f"Digite o nome da {n}ª pessoa: ")
    altura = float(input(f"Digite a altura de {nome} em metros: "))
    
    if altura < 0:
        print("ERRO: Altura não pode ser negativa! Digite novamente.")
    else:
        break
    
    if altura > maior_altura:
        maior_altura = altura
        nome_maior = nome
        
    if altura < menor_altura:
        menor_altura = altura
        nome_menor = nome_menor
        
print("\n" + "=" * 40)
print(f"Pessoa mais alta: {nome_maior} com {maior_altura}m")
print(f"Pessoa mais baixa: {nome_menor} com {menor_altura}m")