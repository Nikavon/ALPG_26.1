'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Q6. (1.5 pontos) Monitoramento de Servidores
# A equipe de TI precisa de um alerta para a temperatura dos servidores. Escreva um programa que:
# 1) Solicite a temperatura atual do servidor principal (número real).
# 2) Se a temperatura for menor que 40 graus, exiba: ”Estado normal.”
# 3) Se a temperatura estiver entre 40 e 75 graus (inclusive), o sistema deve perguntar se o ar
# condicionado secundário está ligado (1 para SIM, 2 para NÃO).
# - Se estiver ligado (1), exiba: ”Estado de Atenção, mas sob controle.”
# - Se estiver desligado (2), exiba: ”Alerta: Ligar ar condicionado secundário imediatamente.”
# 4) Se a temperatura for maior que 75 graus, não pergunte nada, exiba apenas: ”PERIGO:
# Superaquecimento! Iniciando desligamento do sistema.”

temperatura_atual = float(input("Digite a temperatura atual: "))
if temperatura_atual < 40:
    print("Estado normal")
elif 40 <= temperatura_atual <= 75:    
    arcondicionado = int(input("O arcondicionado secundário está ligado? (1 para SIM, 2 para NÃO)"))
    if arcondicionado == 1:
        print("Estado de Atenção, mas sob controle.")
    else: 
        print("Alerta: Ligar ar condicionado secundário imediatamente.")
elif temperatura_atual > 75:
    print("PERIGO: Superaquecimento! Iniciando desligamento do sistema.")