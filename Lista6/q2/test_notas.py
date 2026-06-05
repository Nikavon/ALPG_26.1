from . import notas
import pytest

def test_validar_nota():
    assert notas.validar_nota(0) == True
    assert notas.validar_nota(8) == True
    assert notas.validar_nota(10) == True
    assert notas.validar_nota(-1) == False
    assert notas.validar_nota(11) == False

def test_calcular_media_valida():
    assert notas.calcular_media(8, 7, 9) == 8.0

def test_calcular_media_invalida():
    with pytest.raises(ValueError):
        notas.calcular_media(8, 12, 9)
