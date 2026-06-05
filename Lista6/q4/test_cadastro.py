from . import cadastro
import pytest

def test_validar_idade_valida():
    assert cadastro.validar_idade(20) == True

def test_validar_idade_invalida():
    with pytest.raises(ValueError):
        cadastro.validar_idade(-1)

    with pytest.raises(ValueError):
        cadastro.validar_idade(150)

def test_classificar_idade_invalida():
    with pytest.raises(ValueError):
        cadastro.classificar_idade(-5)

def test_classificar_idade_crianca():
    assert cadastro.classificar_idade(5) == "Criança"

def test_classificar_idade_adolescente():
    assert cadastro.classificar_idade(15) == "Adolescente"

def test_classificar_idade_adulto():
    assert cadastro.classificar_idade(30) == "Adulto"

def test_classificar_idade_idoso():
    assert cadastro.classificar_idade(70) == "Idoso"
