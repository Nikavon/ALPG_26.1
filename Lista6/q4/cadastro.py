def validar_idade(idade):
    if idade >= 0 and idade <= 120:
        return True
    
    raise ValueError("Idade inválida")

def classificar_idade(idade):
    validar_idade(idade)

    if idade <= 11:
        return "Criança"

    if idade <= 17:
        return "Adolescente"
    
    if idade <= 59:
        return "Adulto"
    
    return "Idoso"
  
