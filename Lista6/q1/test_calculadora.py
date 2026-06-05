from . import calculadora
import pytest

def test_soma_simples():
    assert calculadora.somar(1, 2) == 3
    assert calculadora.somar(-1, 1) == 0
    assert calculadora.somar(0.5, 0.2) == pytest.approx(0.7)

def test_soma_retorna_erro():
    assert calculadora.somar(1, 2) != 4

def test_subtrair_simples():
    assert calculadora.subtrair(5, 3) == 2
    assert calculadora.subtrair(0, 1) == -1
    assert calculadora.subtrair(0.5, 0.2) == pytest.approx(0.3)

def test_multiplicar_simples():
    assert calculadora.multiplicar(2, 3) == 6
    assert calculadora.multiplicar(-1, 5) == -5
    assert calculadora.multiplicar(0.5, 0.2) == pytest.approx(0.1)

def test_dividir_simples():
    assert calculadora.dividir(10, 2) == 5
    assert calculadora.dividir(-10, 2) == -5
    assert calculadora.dividir(0.5, 0.2) == pytest.approx(2.5)

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        calculadora.dividir(10, 0)
