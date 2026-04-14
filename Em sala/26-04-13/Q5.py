# Q5. Crie uma lista de frutas que possui na geladeira, e depois peça ao usuário para 
# escolher uma que deseja. Verifique se essa fruta está na geladeira ou não na geladeira e 
# informe ao usuário.

frutas = ["maçã", "banana", "melancia", "laranja", "uva"]
escolha = input("Escolha a fruta: ").lower()

if escolha in frutas:
    print("Essa fruta está na geladeira!")
else:
    print("Essa fruta NÃO está na geladeira!")    