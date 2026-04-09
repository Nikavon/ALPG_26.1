# Q6. Elabore um algoritmo que verifica e informa se a pessoa pode concorrer à 
# vaga de cotista em uma universidade. Para isso, solicite duas informações do 
# usuário. A primeira: se a pessoa está cadastrada no Bolsa Família (S ou N); e a
# segunda: se possui mais de três filhos (S ou N). Para concorrer à vaga de 
# cotista, deve estar cadastrado no Bolsa Família ou ter mais de 3 filhos.

cadastro_bolsa_familia = input("É cadastrado no Bolsa Família? \nS - Sim\nN - Não\n")
quantidade_filhos = int(input("Quantos filhos você possui? "))

if quantidade_filhos >= 3 or cadastro_bolsa_familia == "S":
    print("Parabéns, você pode concorrer a cota!")

else:
    print("Sinto muito, mas você não está habilitado para essa modalidade de cota.")