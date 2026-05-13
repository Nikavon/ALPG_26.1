'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''
Q3. Escreva um algoritmo que possui um número secreto de 1 a 100, e fica pedindo que o usuário digite um
número inteiro de 1 a 100 até acertar o número secreto. Quando acertar, informar com quantos chutes ele 
conseguiu acertar o número.
'''
import random

numero_secreto = random.randint(1, 100)

contador_chutes = 0
acertou = False

while not acertou:
    palpite = int(input("\nDigite seu palpite: "))
    contador_chutes = contador_chutes + 1
    
    if palpite == numero_secreto:
        acertou = True
        print(f"\nParabéns! Você acertou o número secreto!")
        print(f"O número secreto era {numero_secreto}")
        print(f"Você precisou de {contador_chutes} tentativas")
    elif palpite > numero_secreto:
        print("Tá quente, tente um número menor.")
    else:
        print("Tá frio, tente um número maior.")
