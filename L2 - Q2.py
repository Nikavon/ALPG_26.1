'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Q2. Faça um algoritmo que lê dois números, e verifica se o primeiro número é maior ou 
# igual ao segundo número. Se for, escrever "O número {valor do número 1} é maior ou igual
# ao número {valor do número 2}". Se não, escrever "O número {valor do número 1} é menor 
# que número {valor do número 2}".

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 >= numero2:
    print("O número", numero1, "é maior ou igual ao número", numero2)
else:
    print("O número", numero1, "é menor que o número", numero2)