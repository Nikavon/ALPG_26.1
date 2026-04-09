# Q5. Dados três valores, verificar se eles podem ser os comprimentos dos lados de um triângulo e, se 
# forem verificar se é um triângulo equilátero, isósceles ou escalenos. Se eles não formarem um triângulo,
# escrever a mensagem "Esses lados não formam um triângulo". Se formarem um triângulo, informar qual o 
# tipo.
# Considere as seguintes propriedades: 
# O comprimento de cada lado em um triângulo é menor que a soma dos outros dois lados; 
# Equiláteros: tem os comprimentos dos três lados iguais;
# Isósceles: tem os comprimentos de dois lados iguais; 
# Escaleno: tem os comprimentos dos três lados diferentes.

lado_1 = int(input("Digite o primeiro lado: "))
lado_2 = int(input("Digite o segundo lado: "))
lado_3 = int(input("Digite o terceiro lado: "))

if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_1 + lado_2:
    print("Os lados formam um triângulo")
    if lado_1 == lado_2 == lado_3:
        print("Esse é um triângulo equilátero")
    elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3: 
        print("Esse é um triângulo isósceles")
    else:
        print("Esse é um triângulo escaleno")
else:
    print("Os lados não formam um triângulo")        