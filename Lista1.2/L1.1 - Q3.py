'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# Q3. Calculadora de Reajuste Salarial
# Uma empresa dará aumento aos funcionários conforme o cargo informado via código:
# Código 1 (Estagiário): 10% de aumento.
# Código 2 (Analista): 7% de aumento.
# Código 3 (Gerente): 5% de aumento. Qualquer outro código deve ser tratado como "Código 
# não encontrado". O programa deve ler o código e o salário atual, exibindo o novo salário.


print("Bem-vindo(a) a calculadora de reajuste salarial")
print("Códigos disponíveis: ")
print("1 - Estagiário")
print("2 - Analista")
print("3 - Gerente")

salario_atual = float(input("Por favor, digite o seu salário atual: R$ "))
codigo = int(input("Por favor, digite o código de cargo: "))

if codigo == 1:
    aumento = salario_atual * 0.10
    salario_novo = salario_atual + aumento
    print(f"Seu aumento é de 10%.")
    print(f"Novo salário: R$ ", salario_novo)
    
elif codigo == 2:
    aumento = salario_atual * 0.07
    salario_novo = salario_atual + aumento
    print(f"Seu aumento é de 7%.")
    print(f"Novo salário: R$ ", salario_novo)
    
elif codigo == 3:
    aumento = salario_atual * 0.05
    salario_novo = salario_atual + aumento
    print(f"Seu aumento é de 5%.")
    print(f"Novo salário: R$ ", salario_novo)
    
else:
    print("Código não encontrado")