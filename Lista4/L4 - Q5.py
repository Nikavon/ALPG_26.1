'''
Q5. Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo de A! e o 
seu resultado. 
Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
Utilize o loop while para resolver esta questão.
'''

fatorial = int(input("Digite um número para calcular o fatorial: "))

valor_inicial = fatorial

resultado = 1
contador = fatorial

print(f"{valor_inicial}! = ", end="")

while contador >= 1:
    resultado = resultado * contador
    print(contador, end="")
    
    contador = contador - 1
    
print(f" = {resultado}")    