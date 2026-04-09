# Q4. Elabore um algoritmo que leia 5 valores inteiros e apresente na tela o maior e o menor deles.

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))
num_4 = int(input("Digite o quarto número: "))
num_5 = int(input("Digite o quinto número: "))

maior = 0
menor = 0

if num_1 > num_2:
    if num_1 > num_3:
        if num_1 > num_4:
            if num_1 > num_5:
                maior = num_1
 
if num_2 > num_1:
    if num_2 > num_3:
        if num_2 > num_4:
            if num_2 > num_5:
                maior = num_2

if num_3 > num_1:
    if num_3 > num_2:
        if num_3 > num_4:
            if num_3 > num_5:
                maior = num_3

if num_4 > num_1:
    if num_4 > num_2:
        if num_4 > num_3:
            if num_4 > num_5:
                maior = num_4

if num_5 > num_1:
    if num_5 > num_2:
        if num_5 > num_3:
            if num_5 > num_4:
                maior = num_5
                
if num_1 < num_2:
    if num_1 < num_3:
        if num_1 < num_4:
            if num_1 < num_5:
                menor = num_1
 
if num_2 < num_1:
    if num_2 < num_3:
        if num_2 < num_4:
            if num_2 < num_5:
                menor = num_2

if num_3 < num_1:
    if num_3 < num_2:
        if num_3 < num_4:
            if num_3 < num_5:
                menor = num_3

if num_4 < num_1:
    if num_4 < num_2:
        if num_4 < num_3:
            if num_4 < num_5:
                menor = num_4

if num_5 < num_1:
    if num_5 < num_2:
        if num_5 < num_3:
            if num_5 < num_4:
                menor = num_5
                
print("O maior número é o: ", maior)
print("O menor número é o: ", menor)