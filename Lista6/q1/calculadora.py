def exibir_mensagem():
    print("Calculadora simples em Python")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Não é possível dividir por zero.")
    
if __name__ == "__main__":
    exibir_mensagem()
