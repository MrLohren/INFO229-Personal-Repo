import pytest
from math import sqrt

#Creo mi propio algoritmo para detectar primos
def isprime(n):

    if n <= 1:
        return False

    for i in range(2, int(sqrt(n))):
        if n%i == 0:
            return False

    return True

@pytest.mark.parametrize("num", [3,5,7,13,17,131])
def test_isprime(num):
    assert isprime(num) == True
    