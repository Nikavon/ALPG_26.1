def validar_nota(nota):
    return nota >= 0 and nota <= 10

def calcular_media(nota1, nota2, nota3):
    if not validar_nota(nota1) or not validar_nota(nota2) or not validar_nota(nota3):
        raise ValueError("Notas devem ser entre 0 e 10")
    return (nota1 + nota2 + nota3) / 3
