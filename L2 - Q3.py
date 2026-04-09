'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# Faça um algoritmo que irá fazer o cadastro de usuário. Para isso, solicita o nome do 
# usuário, e a senha. Depois, pede que o usuário confirme novamente a senha. O sistema 
# deverá verificar se as senhas digitadas são iguais e se o nome do usuário foi preenchido.
# Se forem iguais e o nome do usuário tiver sido preenchido, informar que o cadastro está 
# correto. Se não, pedir para verificar os dados digitados.


nome = input("Digite o usuário: ")
senha = input("Digite a senha: ")
confirma_senha = input("Confirme a senha: ")

if nome and senha == confirma_senha and nome != '':
    print("Cadastro realizado com sucesso")
    
else:
    print("Dados incorretos, verifique os dados digitados.")