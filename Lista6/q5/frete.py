def valida_peso(peso):
    if peso <= 0:
        raise ValueError("Peso inválido")
    
    return True

def valida_distancia(distancia):
    if distancia <= 0:
        raise ValueError("Distância inválida")
    
    return True

def calcular_frete(peso, distancia):
    valida_peso(peso)
    valida_distancia(distancia)

    return 10 + peso * 2.50 + distancia * 0.50

