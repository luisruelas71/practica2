from calculadora import calculadora

def test_add():
    calc = calculadora()
    assert calc.add(2, 3) == 5

def test_add_v2():
    calc = calculadora()
    assert calc.add_v2(2, 3) == 6

def test_add_v3():
    calc = calculadora()
    assert calc.add_v3(2, 3) == 8