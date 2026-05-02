'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Q3. (2.0 pontos) Cinema: Bilheteria Automática
# Escreva um programa para validar a compra de ingressos de cinema com base na idade e no
# gênero de filme.
# 1) Tenha uma lista de gêneros restritos no código: ["terror", "guerra", "crime"].
# 2) Solicite ao usuário o gênero do filme que deseja assistir e a sua idade.
# 3) Se o gênero escolhido estiver na lista de restritos e a idade for menor que 18 anos, o
# programa deve exibir: ”Venda bloqueada: Filme não recomendado para a sua idade.”
# 4) Se o gênero escolhido estiver na lista, mas a idade for maior ou igual a 18 anos, exiba:
# ”Venda autorizada. Tenha uma boa sessão.”
# 5) Se o gênero não estiver na lista, exiba: ”Venda autorizada (Filme de classificação livre).”


genero_restrito = ["terror", "guerra", "crime"]
genero = input("Qual o gênero do filme que você deseja assistir? ").lower()
idade = int(input("Qual a sua idade? "))

if genero in genero_restrito and idade < 18:
    print("Venda bloqueada: Filme não recomendado para a sua idade.")
elif genero in genero_restrito and idade >= 18:
    print("Venda autorizada. Tenha uma boa sessão.")
else:
    print("Venda autorizada (Filme de classificação livre).")