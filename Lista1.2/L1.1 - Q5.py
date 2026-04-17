'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Q5. Simulador de Semáforo Inteligente
# Crie um programa que pergunte ao usuário o estado do semáforo (1-Verde, 2-Amarelo, ]
# 3-Vermelho) e se há pedestres atravessando (1-Sim, 2-Não).
# Se o sinal estiver Verde e não houver pedestres, exiba "Pode passar".
# Se o sinal estiver Verde, mas houver pedestres, exiba "Aguarde os pedestres".
# Se o sinal estiver Amarelo, exiba "Atenção, reduza a velocidade".
# Se o sinal estiver Vermelho, exiba "Pare o veículo".

semaforo = int(input("Qual a cor do semáforo?\n1 - Verde \n2 - Amarelo \n3 - Vermelho\n"))
pedestre = int(input("Tem pedestres na faixa?\n1 - Sim\n2 - Não\n"))

if semaforo == 1 and pedestre == 2:
    print("Pode passar")
elif semaforo == 1 and pedestre == 1:
    print("Aguarde os pedestres")
elif semaforo == 2:
    print("Atenção, reduza a velocidade")
else:
    print("Pare o veículo")