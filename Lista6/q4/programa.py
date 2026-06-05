from cadastro import classificar_idade

if __name__ == "__main__":
    idade = input("Digite sua idade: ")

    if (not idade.isdigit()):
        print("Idade inválida")
        exit(1)

    try:
        classificacao = classificar_idade(int(idade))
        print(f"Classificação: {classificacao}")
    except ValueError as e:
        print(e)
        exit(1)
