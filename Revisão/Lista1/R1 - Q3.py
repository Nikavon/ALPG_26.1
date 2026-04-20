# Q3. (Automação Residencial) Ar Condicionado Inteligente
# Escreva um programa que simula o cérebro de um sistema de ”Smart Home” que decide se deve
# ligar o ar condicionado.
# 1) Solicite a temperatura atual do ambiente.
# 2) Pergunte se há alguém no cômodo (1 para SIM, 2 para NÃO).
# 3) Pergunte se a janela está aberta (1 para SIM, 2 para NÃO).
# 4) O ar condicionado só deve ser ligado se: a temperatura for maior que 24 graus, e houver
# alguém no cômodo (opção 1), e a janela não estiver aberta (opção 2).
# 5) Se todas as condições acima forem verdadeiras, exiba: ”Ligando o ar condicionado.”
# 6) Se a janela estiver aberta (opção 1), exiba prioritariamente: ”Erro: Feche a janela antes de
# ligar o ar.”
# 7) Nos demais casos, exiba: ”O ar condicionado permanecerá desligado.”

temperatura_atual = int(input("Digite a temperatura atual: "))
pessoas_comodo = int(input("Há pessoas no cômodo? \n1 - Sim \n2 - Não\n"))
janela = int(input("Há janelas abertas? \n1 - Sim \n2 - Não\n"))

if temperatura_atual > 24 and pessoas_comodo == 1 and janela == 2:
    print("Ligando o ar condicionado.")
elif janela == 1:
    print("Erro: Feche a janela antes de ligar o ar.")
else:
    print("O ar condicionado permanecerá desligado.")    