from frete import calcular_frete

if __name__ == "__main__":
    peso = input("Digite o peso do produto: ")

    if (not peso.isdigit()):
        print("Peso inválido")
        exit(1)

    distancia = input("Digite a distância da entrega: ")

    if (not distancia.isdigit()):
        print("Distância inválida")
        exit(1)

    try:
        frete = calcular_frete(float(peso), float(distancia))
        print(f"O valor do frete é: R${frete:.2f}")
    except ValueError as e:
        print(e)
        exit(1)
