from polynomials import Polynomial

def test_print():
    p=Polynomial((2,3,0,1))
    assert str(p)=="x^3+3x+2"