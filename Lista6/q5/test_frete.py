from . import frete
import pytest

def test_calcular_frete():
    assert frete.calcular_frete(2, 10) == 20.0

def test_calcular_frete_peso_invalido():
    with pytest.raises(ValueError):
        frete.calcular_frete(-1, 10)

def test_calcular_frete_distancia_invalida():
    with pytest.raises(ValueError):
        frete.calcular_frete(2, -1)
