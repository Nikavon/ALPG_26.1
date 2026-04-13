'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# Q2. Classificação de Produtos (Peso)
# Crie um algoritmo que leia o peso de um produto (em gramas) e o classifique em:
# Leve: Até 250g.
# Médio: Acima de 250g até 500g.
# Pesado: Acima de 500g até 1000g.
# Carga Especial: Acima de 1000g.
# Nota: Se o peso for zero ou negativo, informe "Peso Inválido".


produto = float(input("Por favor digite o peso do produto (em gramas): "))

if produto <= 0:
    print("Peso inválido")

elif produto <= 250:
    print("Produto: Leve")
elif produto <= 500:
    print("Produto: Médio")
elif produto <= 1000:
    print("Produto: Pesado")
else:
    print ("Produto: Carga Especial")    