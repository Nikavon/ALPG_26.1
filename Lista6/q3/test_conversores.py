from . import conversores

def test_celsius_para_fahrenheit():
    assert conversores.celsius_para_fahrenheit(0) == 32
    assert conversores.celsius_para_fahrenheit(100) == 212
    assert conversores.celsius_para_fahrenheit(-40) == -40

def test_fahrenheit_para_celsius():
    assert conversores.fahrenheit_para_celsius(32) == 0
    assert conversores.fahrenheit_para_celsius(212) == 100
    assert conversores.fahrenheit_para_celsius(-40) == -40
